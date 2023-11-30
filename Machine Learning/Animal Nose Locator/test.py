import os
import torch
import argparse
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
from torchvision import transforms
from torch.utils.data import DataLoader, Dataset
from torchvision.models import resnet18
import torch.nn as nn
import numpy as np
import time

class CustomTestDataset(Dataset):

    def __init__(self, directory, transform=None):
        self.directory = directory
        self.transform = transform
        self.labels = []

        # Read the labels.txt file
        if not os.path.exists(directory):
            os.makedirs(directory)

        with open(os.path.join(directory, 'test_noses.txt'), 'r') as file:
            for line in file:
                image_file, label, _ = line.strip().split(sep="\"")
                image_file = image_file[:-1]
                coordinates = label.strip('()').split(', ')
                x, y = map(int, coordinates)
                self.labels.append((image_file, int(x), int(y)))

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, idx):
        image_file, x, y = self.labels[idx]
        image_path = os.path.join(self.directory, image_file)
        image = Image.open(image_path).convert('RGB')

        original_size = image.size  # Store the original size as a tuple
        # print(original_size)
        if self.transform:
            image = self.transform(image)

        return image, torch.tensor([x, y], dtype=torch.float32), original_size

def test(test_set, model, batch_size=1, pixel_range=50):
    device = torch.device('cpu')
    print(f"Using {device}")

    # Initialize the ResNet model with the modified last layer
    model = resnet18(weights=None)
    model.fc = nn.Linear(model.fc.in_features, 2)  # Modify fc layer to match the number of coordinates

    # Load the trained model weights
    model.load_state_dict(torch.load("./model_weights.pth"))  # Replace with the actual path
    model.to(device)
    model.eval()

    test_loader = DataLoader(test_set, batch_size=batch_size, shuffle=False)

    all_true_labels = []
    all_pred_labels = []

    image_test_time = []

    for data in test_loader:
        test_time_start = time.time()*1000
        inputs, labels, original_size = data

        #print("-------------------------")
        #print(len(inputs))
        #print(original_size)
        #print("-------------------------")

        resized_inputs = torch.nn.functional.interpolate(inputs, size=(original_size[1], original_size[0]),
                                                         mode='bilinear', align_corners=False)

        outputs = model(resized_inputs)
        all_true_labels.extend(labels.detach().numpy())
        all_pred_labels.extend(outputs.detach().numpy())
        test_time_end = time.time()*1000
        image_test_time.append(test_time_end - test_time_start)

    average_test_time = sum(image_test_time)/len(image_test_time)

    # Evaluate predictions based on pixel range
    correct_predictions = np.abs(np.array(all_true_labels) - np.array(all_pred_labels)) <= pixel_range
    accuracy = np.mean(correct_predictions)

    print(f"Accuracy within {pixel_range} pixels: {accuracy * 100:.2f}%")
    print(f"Average test time per image is: {average_test_time:.2f}")

    # Draw example pictures with predicted coordinates marked
    for i, (true_label, pred_label, is_correct) in enumerate(
            zip(all_true_labels, all_pred_labels, correct_predictions)):
        #if is_correct.any():
            image, _, original_size = test_set[i]

            print(original_size)
            resized_image = torch.nn.functional.interpolate(image.unsqueeze(0), size=(original_size[1], original_size[0]), mode='bilinear', align_corners=False)

            # Convert PyTorch tensor to PIL image
            image_pil = transforms.ToPILImage()(resized_image.squeeze(0))
            draw = ImageDraw.Draw(image_pil)
            draw.ellipse([true_label[0] - pixel_range/10, true_label[1] - pixel_range/10,
                    true_label[0] + pixel_range/10, true_label[1] + pixel_range/10], outline="red")
            draw.ellipse([true_label[0] - pixel_range, true_label[1] - pixel_range,
                            true_label[0] + pixel_range, true_label[1] + pixel_range], outline="red")
            draw.ellipse([pred_label[0] - pixel_range, pred_label[1] - pixel_range,
                            pred_label[0] + pixel_range, pred_label[1] + pixel_range], outline="blue")
            plt.imshow(image_pil)
            plt.title(f"Example {i + 1}")
            plt.show()

    #conf_matrix = confusion_matrix(all_true_labels, all_pred_labels)

    #plt.figure(figsize=(8, 8))
    #plt.imshow(conf_matrix, interpolation='nearest', cmap=plt.cm.Blues)
    #plt.title('Confusion Matrix')
    #plt.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Args for test")
    parser.add_argument("-test_set", required=True, default="/datasets/COCO100/",
                        help="Path to the content images directory")
    parser.add_argument("-b", type=int, default=32, help="Batch size for testing")
    parser.add_argument("-w", required=True, default="N", help="Weight path")
    args = parser.parse_args()

    # Set the path to your test dataset
    test_dataset_directory = args.test_set

    transform = transforms.Compose([
        transforms.Resize((400, 600)),  # Adjust size as needed
        transforms.ToTensor(),
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),  # Adjust normalization
    ])

    # Create a test dataset
    test_set = CustomTestDataset(directory=test_dataset_directory, transform=transform)

    # Initialize the ResNet model
    resnet_model = resnet18(weights=None)
    resnet_model.fc = torch.nn.Linear(resnet_model.fc.in_features, 2)  # Modify fc layer to match the number of coordinates

    # Test the model on the provided test dataset
    test(test_set, resnet_model)

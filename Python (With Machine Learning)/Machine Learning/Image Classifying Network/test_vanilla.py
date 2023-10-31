from vanilla_model import Vanilla_model
from vanilla_model import proper_encoder
from train_vanilla import train
import torch
import torchvision
import torchvision.transforms as transforms
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt
import numpy as np
import random as random

def imshow(img):
    img = img / 2 + 0.5     # unnormalize
    npimg = img.numpy()
    plt.imshow(np.transpose(npimg, (1, 2, 0)))
    plt.show()


def show_top_predictions(vanilla_model, testloader, classes):
    # Get some random images from the test loader
    dataiter = iter(testloader)
    images, labels = next(dataiter)

    # Get model predictions
    outputs = vanilla_model(images)
    _, predicted = torch.max(outputs, 1)

    # Display 5 random images and their top 5 predictions
    num_images_to_display = 5
    random_indices = random.sample(range(len(images)), num_images_to_display)

    for i in random_indices:
        image = images[i]
        label = labels[i].item()
        prediction = predicted[i].item()

        # Get the top 5 predictions and their percentages
        softmax_probabilities = torch.softmax(outputs, dim=1)[i]
        top5_prob, top5_class = softmax_probabilities.topk(5)

        fig, ax = plt.subplots(1, 2, figsize=(10, 4))
        ax[0].imshow(image.permute(1, 2, 0))  # Display the image
        ax[0].axis('off')

        predictions_text = [f'{classes[top5_class[j]]} ({top5_prob[j] * 100:.2f}%)' for j in range(5)]
        predictions_text = '\n'.join(predictions_text)
        ax[1].text(0, 0.5, f'Actual: {classes[label]}\nPredictions:\n{predictions_text}', fontsize=10)
        ax[1].axis('off')

        plt.show()

def test(batch_size, testloader, classes):
    print("Testing...")

    path_model = './cifar_net.pth'
    path_encoder = "./encoder.pth"

    encoder = proper_encoder.encoder
    encoder_weights = torch.load(path_encoder)  # Load the encoder weights
    encoder.load_state_dict(encoder_weights)  # Load the weights into the model

    num_classes = len(classes)
    vanilla_model = Vanilla_model(num_classes, encoder=encoder)  # Create an instance of the model
    model_weights = torch.load(path_model)  # Load the model weights
    vanilla_model.load_state_dict(model_weights)  # Load the weights into the model

    vanilla_model.eval()  # Set the model to evaluation mode


    dataiter = iter(testloader)
    images, labels = next(dataiter)

    # print images
    imshow(torchvision.utils.make_grid(images))
    print('GroundTruth: ', ' '.join(f'{classes[labels[j]]:5s}' for j in range(4)))

    outputs = vanilla_model(images)

    _, predicted = torch.max(outputs, 1)

    print('Predicted: ', ' '.join(f'{classes[predicted[j]]:5s}'
                                  for j in range(4)))

    correct = 0
    total = 0
    # since we're not training, we don't need to calculate the gradients for our outputs
    with torch.no_grad():
        for data in testloader:
            images, labels = data
            # calculate outputs by running images through the network
            outputs = vanilla_model(images)
            # the class with the highest energy is what we choose as prediction
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

    print(f'Accuracy of the network on the 10000 test images: {100 * correct // total} %')

    # prepare to count predictions for each class
    correct_pred = {classname: 0 for classname in classes}
    total_pred = {classname: 0 for classname in classes}

    # again no gradients needed
    with torch.no_grad():
        for data in testloader:
            images, labels = data
            outputs = vanilla_model(images)
            _, predictions = torch.max(outputs, 1)
            # collect the correct predictions for each class
            for label, prediction in zip(labels, predictions):
                if label == prediction:
                    correct_pred[classes[label]] += 1
                total_pred[classes[label]] += 1

    # print accuracy for each class
    for classname, correct_count in correct_pred.items():
        accuracy = 100 * float(correct_count) / total_pred[classname]
        print(f'Accuracy for class: {classname:5s} is {accuracy:.1f} %')

    top_errors = []
    with torch.no_grad():
        for data in testloader:
            images, labels = data
            outputs = vanilla_model(images)
            _, predictions = torch.max(outputs, 1)

            for i in range(batch_size):
                if len(top_errors) < 5:
                    if predictions[i] != labels[i]:
                        top_errors.append((images[i], labels[i], predictions[i]))
                else:
                    break

        # Display the top 5 error images
    fig, axes = plt.subplots(1, 5, figsize=(15, 3))
    for i, (image, true_label, predicted_label) in enumerate(top_errors):
        image = image / 2 + 0.5  # Unnormalize
        npimg = image.numpy()
        axes[i].imshow(np.transpose(npimg, (1, 2, 0)))
        axes[i].set_title(f'True: {classes[true_label]}, Predicted: {classes[predicted_label]}')

    plt.show()

    show_top_predictions(vanilla_model, testloader, classes)


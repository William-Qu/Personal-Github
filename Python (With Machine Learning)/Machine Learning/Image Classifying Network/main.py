from vanilla_model import Vanilla_model
from test_vanilla import test
from vanilla_model import proper_encoder
from train_vanilla import train
import torch
import torchvision
import torchvision.transforms as transforms
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt
import os

if (__name__ == "__main__"):
    training = 0
    batch_size = 10
    num_epochs = 5

    #Fixes linker issue
    os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

    transform = transforms.Compose(
        [transforms.ToTensor(),
         transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

    if(training == 1):
        #Load the train data
        trainset = torchvision.datasets.CIFAR100(root='./data', train=True,
                                                download=True, transform=transform)
        trainloader = torch.utils.data.DataLoader(trainset, batch_size=batch_size,
                                                  shuffle=True, num_workers=2)

        classes = trainset.classes
        num_classes = len(classes)

        encoder = proper_encoder.encoder
        path_encoder = "./encoder.pth"
        encoder_weights = torch.load(path_encoder)  # Load the model weights
        encoder.load_state_dict(encoder_weights)  # Load the weights into the model

        vanilla_model = Vanilla_model(num_classes, encoder=encoder)
        criterion = nn.CrossEntropyLoss()
        optimizer = optim.SGD(vanilla_model.parameters(), lr=0.001, momentum=0.9)
        train(vanilla_model=vanilla_model, num_epochs=num_epochs, criterion=criterion, optimizer=optimizer, trainloader=trainloader)


    if (training == 0):
        #Load the test data
        testset = torchvision.datasets.CIFAR100(root='./data', train=False,
                                               download=True, transform=transform)
        testloader = torch.utils.data.DataLoader(testset, batch_size=batch_size,
                                                 shuffle=False, num_workers=2)

        classes = testset.classes

        test(batch_size=batch_size, testloader=testloader, classes=classes)

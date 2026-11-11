from vanilla_model import Vanilla_model
import torch
import torchvision
import torchvision.transforms as transforms
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt
import datetime


def train(vanilla_model, num_epochs, criterion, optimizer, trainloader):
    print("Training...")
    epoch_train = []
    losses_train = []
    starting_time = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"Time at start of training is: {starting_time}")

    for epoch in range(num_epochs):  # loop over the dataset multiple times
        running_loss = 0.0
        for i, data in enumerate(trainloader, 0):
            # get the inputs; data is a list of [inputs, labels]
            inputs, labels = data

            # zero the parameter gradients
            optimizer.zero_grad()

            # forward + backward + optimize
            outputs = vanilla_model(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            # print statistics
            running_loss += loss.item()
            if i % 2000 == 1999:  # print every 2000 mini-batches
                timestamp = datetime.datetime.now().strftime("%H:%M:%S")
                print(f"[{epoch + 1}, {i + 1:5d}] loss: {running_loss / 2000:.3f}, Time: {timestamp}")
                running_loss = 0.0
        #Collect data to plot after tests are done
        losses_train.append(running_loss/4000)
        epoch_train.append(epoch + 1)

    plt.figure()
    plt.plot(epoch_train, losses_train)
    plt.xlabel('Epoch')
    plt.ylabel('Training Loss')
    plt.title('Training Loss vs Epoch')
    plt.savefig("./train_loss_fig")
    plt.close()

    ending_time = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"Time at end of training is: {ending_time}")

    PATH = './cifar_net.pth'
    torch.save(vanilla_model.state_dict(), PATH)




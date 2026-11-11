import torch
import torchvision
import torchvision.transforms as transforms
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import matplotlib.pyplot as plt

class proper_encoder:
    encoder = nn.Sequential(
        nn.Conv2d(3, 3, (1, 1)),
        nn.ReflectionPad2d((1, 1, 1, 1)),
        nn.Conv2d(3, 64, (3, 3)),
        nn.ReLU(),  # relu1-1
        nn.ReflectionPad2d((1, 1, 1, 1)),
        nn.Conv2d(64, 64, (3, 3)),
        nn.ReLU(),  # relu1-2
        nn.MaxPool2d((2, 2), (2, 2), (0, 0), ceil_mode=True),
        nn.ReflectionPad2d((1, 1, 1, 1)),
        nn.Conv2d(64, 128, (3, 3)),
        nn.ReLU(),  # relu2-1
        nn.ReflectionPad2d((1, 1, 1, 1)),
        nn.Conv2d(128, 128, (3, 3)),
        nn.ReLU(),  # relu2-2
        nn.MaxPool2d((2, 2), (2, 2), (0, 0), ceil_mode=True),
        nn.ReflectionPad2d((1, 1, 1, 1)),
        nn.Conv2d(128, 256, (3, 3)),
        nn.ReLU(),  # relu3-1
        nn.ReflectionPad2d((1, 1, 1, 1)),
        nn.Conv2d(256, 256, (3, 3)),
        nn.ReLU(),  # relu3-2
        nn.ReflectionPad2d((1, 1, 1, 1)),
        nn.Conv2d(256, 256, (3, 3)),
        nn.ReLU(),  # relu3-3
        nn.ReflectionPad2d((1, 1, 1, 1)),
        nn.Conv2d(256, 256, (3, 3)),
        nn.ReLU(),  # relu3-4
        nn.MaxPool2d((2, 2), (2, 2), (0, 0), ceil_mode=True),
        nn.ReflectionPad2d((1, 1, 1, 1)),
        nn.Conv2d(256, 512, (3, 3)),
        nn.ReLU(),  # relu4-1, this is the last layer used
    )
    fc = nn.Sequential(
        nn.Linear(512, 256),  # You can adjust the number of hidden units in this layer
        nn.ReLU(),
        nn.Linear(256, 10)  # Output layer with 10 being num_classes units
    )

class Vanilla_model(nn.Module):
    def __init__(self, num_classes, encoder):
        super(Vanilla_model, self).__init__()

        self.encoder = encoder
        for param in self.encoder.parameters():
            param.requires_grad = False

        self.fc = nn.Sequential(
            nn.Linear(8192, 2048),
            nn.ReLU(),
            nn.Linear(2048, 1024),
            nn.ReLU(),
            nn.Linear(1024, 256),  # You can adjust the number of hidden units in this layer
            nn.ReLU(),
            nn.Linear(256, num_classes)  # Output layer with num_classes units
        )

        self.mse_loss = nn.MSELoss()


    def init_encoder_weights(self, mean, std):
        for param in self.encoder.parameters():
            nn.init.normal_(param, mean=mean, std=std)

    def init_fc_weights(self, mean, std):
        for param in self.fc.parameters():
            nn.init.normal_(param, mean=mean, std=std)

    def forward(self, x):
        #print(("x size is: ") + str(x.size()))
        x = self.encoder(x)
        #print("\n\n\n")
        #print(("x size is: ") + str(x.size()))
        x = x.view(x.size(0), -1)  # Flatten the feature map
        x = self.fc(x)
        return x




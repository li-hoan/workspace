import torch
from torch import nn
import matplotlib.pyplot as plt
import torch.nn.functional as F

x = torch.unsqueeze(torch.arange(-10, 10), dim=1)
y = x.pow(3)


class Net(nn.Module):
    def __init__(self):
        super().__init__()

        self.w1 = nn.Parameter(torch.randn(1, 20))
        self.b1 = nn.Parameter(torch.zeros(20))
        self.w2 = nn.Parameter(torch.randn(20, 64))
        self.b2 = nn.Parameter(torch.zeros(64))
        self.w3 = nn.Parameter(torch.randn(64, 128))
        self.b3 = nn.Parameter(torch.zeros(128))
        self.w4 = nn.Parameter(torch.randn(128, 64))
        self.b4 = nn.Parameter(torch.zeros(64))
        self.w5 = nn.Parameter(torch.randn(64, 1))
        self.b5 = nn.Parameter(torch.zeros(1))

    def forward(self, x):
        fc1 = F.relu(torch.matmul(x, self.w1) + self.b1)
        fc2 = F.relu(torch.matmul(fc1, self.w2) + self.b2)
        fc3 = F.relu(torch.matmul(fc2, self.w3) + self.b3)
        fc4 = F.relu(torch.matmul(fc3, self.w4) + self.b4)
        fc5 = torch.matmul(fc4, self.w5) + self.b5
        return fc5


if __name__ == '__main__':
    net = Net()
    opt = torch.optim.Adam(net.parameters(),lr=0.1)
    loss_fun = nn.MSELoss()

    plt.ion()
    for i in range(10000):
        out = net(x.float())
        loss = loss_fun(out,y.float())

        opt.zero_grad()
        loss.backward()
        opt.step()

        if i%5==0:
            plt.cla()
            plt.scatter(x,y)
            plt.plot(x,out.detach().numpy(),'r')
            plt.pause(0.1)
            print(loss.item())



    plt.ioff()
    plt.show()
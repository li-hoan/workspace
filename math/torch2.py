import torch
from torch import optim
import matplotlib.pyplot as plt

xs = torch.arange(0, 1, 0.01)
ys = 3 * xs + 4 + torch.rand(100)


class line(torch.nn.Module):
    def __init__(self):
        super().__init__()

        self.w = torch.nn.Parameter(torch.rand(1))
        self.b = torch.nn.Parameter(torch.rand(1))

    def forward(self, x):
        return self.w * x + self.b

if __name__ == '__main__':
    line = line()

    opt  = optim.SGD(line.parameters(),lr = 0.1)#parameter要加s

    plt.ion()
    for epoch in range(30):
        for x,y in zip(xs, ys):
            z = line(x)
            loss = (z-y)**2

            opt.zero_grad()
            loss.backward()
            opt.step()

            print(line.w.item(), line.b.item(),loss.item())

        plt.cla()
        plt.plot(xs,ys,'.')
        v = [line.w *e +line.b for e in xs]
        plt.plot(xs,v)
        plt.pause(0.01)


    plt.ioff()
    plt.show()


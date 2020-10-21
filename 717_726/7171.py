import torch
from torch import nn

if __name__ == '__main__':

    conv = nn.Conv2d(3,16,3,1)
    x=torch.randn(1,3,16,16)
    y=conv(x)
    print(y.shape)
import torch
from torch import optim
import matplotlib.pyplot as plt

xs = torch.arange(0, 1, 0.01)
ys = 3 * xs + 4 + torch.rand(100)#torch.rand为0-1的均匀分布


# plt.plot(xs,ys,'.')
# plt.show()
class line(torch.nn.Module):#继承父类
    def __init__(self):
        super().__init__()  # 父类实列化。后调用。
        # 模型设计
        self.w = torch.nn.Parameter(torch.rand(1))  # 构建系统参数
        self.b = torch.nn.Parameter(torch.rand(1))

    def forward(self, x):  # 前向过程，将数据输入到模型中，返回结果。
        return self.w * x + self.b

if __name__ == '__main__':
    line = line()

    #定义优化器
    opt = optim.SGD(line.parameters(),lr=0.1)#优化，及学习率

    plt.ion()
    #定义损失函数
    for epoch in range(30):
        for _x,_y in zip(xs,ys):
            #将数据输入到模型中
            z = line(_x)#forward可直接传
            #print(z)

            #定义损失
            loss = (z-_y)**2

            #梯度清空
            opt.zero_grad()
            #自动求导
            loss.backward()
            #参数更新
            opt.step()

            print(line.w.item(),line.b.item(),loss.item())#item()调用其间的数值
        plt.cla()
        plt.plot(xs,ys,'.')
        v = [line.w*e+line.b for e in xs]
        plt.plot(xs,v)
        plt.pause(0.01)

    plt.ioff()
    plt.show()
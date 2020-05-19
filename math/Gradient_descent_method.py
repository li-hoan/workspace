# import torch
#
# x = torch.tensor([3.0],requires_grad=True)#更新梯度，自动求导为TRUE
# y = x**3+2
# # y.backward()#对y求导
# # print(x.grad)#求出x的梯度
#
# print(torch.autograd.grad(y,x))#求导

import random
import matplotlib.pyplot as plt

_x = [i / 100 for i in range(100)]
# print(_x)
_y = [3*e + 4 + random.random() for e in _x]
# print(_y)

w = random.random()
b = random.random()

for i in range(30):
    for x, y in zip(_x, _y):
        z = w * x + b
        o = z - y
        loss = o ** 2#求损失

        dw = -2 * o * x#求导
        db = -2 * o

        w = 0.1 * dw + w#梯度下降法
        b = 0.1 * db + b


        print(';w=', w, ';b=', b, ';loss=', loss)

plt.plot(_x, _y,'.')#绘点
v = [w * e + b for e in _x]
plt.plot(_x,v)
plt.show()

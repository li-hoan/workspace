import random
import matplotlib.pyplot as plt

_x = [i / 100 for i in range(100)]
# print(_x)
_y = [3*e + 4 + random.random() for e in _x]
# print(_y)

w = random.random()
b = random.random()

plt.ion()#开启会话
for i in range(30):
    for x, y in zip(_x, _y):#将数据x输入到构建好的线性模型中，得到输出z（前向过程，推理过程）
        z = w * x + b
        o = z - y
        loss = o ** 2#求损失

        dw = -2 * o * x#求导
        db = -2 * o

        w = 0.1 * dw + w#梯度下降法
        b = 0.1 * db + b


        print(';w=', w, ';b=', b, ';loss=', loss)

    v = [w * e + b for e in _x]
    plt.cla()#清空
    plt.scatter(_x, _y)  # 绘点
    plt.plot(_x, v)
    plt.title(loss)
    plt.pause(0.01)#睡眠0.01秒




plt.ioff()#结束会话
plt.show()

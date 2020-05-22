import random
import matplotlib.pyplot as plt
import numpy as np

_x = [i / 100 for i in range(0, 100)]
_y = [e ** 3 for e in _x]
# _v = [1 / (1 + np.exp(-e)) for e in _y]

w = random.random()
# b = random.random()

for i in range(30):
    for x, y in zip(_x, _y):
        z = x ** w
        o = z - y
        loss = o ** 2

        dw = 2 * o * ((x ** w) * np.log(x))

        w = -0.1 * dw + w

        print(w, loss)

plt.plot(_x, _y, '.')
v = [e ** w for e in _x]
plt.plot(_x, v)
plt.show()

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-100, 100, 0.1)
# print(x)
y = x ** 2
y1 = np.tile(np.array([0]), x.shape)  #广播应用

plt.plot(x, y)
plt.plot(x, y1)
plt.show()

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-1,1, 0.01)
y = 0.5 ** x
y1 = 2 ** x

plt.plot(x, y)
plt.plot(x,y1)
plt.show()

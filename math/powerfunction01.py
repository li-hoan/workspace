import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0.1,100)
y = x**0.5
y1 = np.tile(np.array([0]),x.shape)
y2 = x**(-1)

plt.plot(x,y)
plt.plot(x,y1)
plt.plot(x,y2)
plt.show()
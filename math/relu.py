import  numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10,0)
y = np.zeros_like(x)
j = np.arange(0,10)
k = j

plt.plot(x,y)
plt.plot(j,k)
plt.show()
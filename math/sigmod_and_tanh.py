import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10,10,0.1)
y= 1/(1+np.exp(-x))#sigmod
y1 = (np.exp(x)-np.exp(-x))/(np.exp(x)+np.exp(-x))#tanh

plt.plot(x,y)
plt.plot(x,y1)
plt.show()
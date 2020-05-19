import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0.1,100)
y = np.log(x)
y1 = np.log2(x)
y2 =np.zeros_like(x)#画y=0的轴
y3 = (np.log(x))/(np.log(0.5))#以0.5为底的Log函数

plt.plot(x,y)
plt.plot(x,y1)
plt.plot(x,y2)
plt.plot(x,y3)
plt.show()
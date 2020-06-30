import matplotlib.pyplot as plt
import numpy as np

x = np.random.randn(20)
y = np.random.randn(20)
x1 = np.random.randn(20)
y1 = np.random.randn(20)

#绘制点
plt.scatter(x,y,c="r",marker="p",s=20,label = "girl")
plt.scatter(x1,y1,c="b",marker="v",s=18,label = "boy")
plt.legend()#显示图列
plt.show()
#svr
import  numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVR

#种子
rng = np.random.RandomState(1)


x= 5*rng.rand(100,1)
y = np.sin(x).ravel()

y[::5] += 3*(0.5 -rng.rand(x.shape[0]//5))

svr= SVR(kernel="rbf",C=10,gamma=0.1)
svr.fit(x,y)

x_plot = np.linspace(0,5,100)
y_svr = svr.predict(x_plot[:,None])
plt.scatter(x,y)
plt.plot(x_plot,y_svr,color="red")
plt.show()
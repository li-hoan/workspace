import numpy as np
from sklearn.kernel_ridge import KernelRidge
import matplotlib.pyplot as plt
from sklearn.model_selection import GridSearchCV

# rng = np.random.RandomState(0)

x = 5*np.random.rand(100,1)#构成的形状为(100,1)
y = np.sin(x).ravel()

#add noise to target
y[::5]+=3*(0.5-np.random.rand(x.shape[0]//5))

# kr = KernelRidge(kernel='sigmoid',gamma=0.4)
kr = GridSearchCV(KernelRidge(),
                  param_grid={"kernel":["rbf","laplacian","polynomial","sigmoid"],
                              "alpha":[1e0,0.1,1e-2,1e-3],
                              "gamma":np.logspace(-2,2,5)})
kr.fit(x,y)
print(kr.best_score_,kr.best_params_)

x_plot = np.linspace(0,5,100)
y_kr = kr.predict(x_plot[:,None])

plt.scatter(x,y)
plt.plot(x_plot,y_kr,"r")
plt.show()
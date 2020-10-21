#kmeans的应用
from sklearn.cluster import KMeans
import numpy as np
from  mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

#生成数据
data = np.random.rand(100,3)

#创建模型
estim = KMeans(n_clusters=3)

#聚类训练
y  = estim.fit_predict(data)

#获取聚类中心
center = estim.cluster_centers_
#获取类别的标签
label_pre = estim.labels_

print(label_pre)
print(center)

fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(data[:,0],data[:,1],data[:,2],c =y,marker="*" )
ax.scatter(center[:,0],center[:,1],center[:,2],c = center[0],marker=">",s=120)
plt.show()

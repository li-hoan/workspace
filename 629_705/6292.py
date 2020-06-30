from sklearn import datasets,neighbors,preprocessing
from sklearn.model_selection import train_test_split
from  sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt

#加载数据
iris = datasets.load_iris()
# print(iris['data'].shape)

x,y = iris.data,iris.target

#设置k值为1到30，通过绘图来查看训练的分数
k_range = range(1,31)
k_socker = []
for k in k_range:
    knn = neighbors.KNeighborsClassifier(n_neighbors=k)
    scores = cross_val_score(knn,x,y,cv = 5,scoring="accuracy")
    k_socker.append(scores.mean())
plt.figure()
plt.plot(k_range,k_socker)
plt.show()
from sklearn import datasets,neighbors,preprocessing
from sklearn.model_selection import train_test_split
from  sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score

#加载数据
iris = datasets.load_iris()
# print(iris['data'].shape)

#划分为训练集和测试集
x,y = iris.data,iris.target
x_test,x_train,y_test,y_train = train_test_split(x,y,test_size=0.3)

#数据预处理
scaler = preprocessing.StandardScaler().fit(x_train)
x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)

#创建模型
knn= neighbors.KNeighborsClassifier(n_neighbors=5)
#模型拟合
knn.fit(x_train,y_train)

#交叉验证
score = cross_val_score(knn,x_train,y_train,cv=5,scoring="accuracy")
print(score)
print(score.mean())

#预测
y_pred = knn.predict(x_test)

#评估
print(accuracy_score(y_pred,y_test))
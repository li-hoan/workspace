#基本结构

from  sklearn import neighbors,datasets,preprocessing#最后一个用与数据预处理
from  sklearn.model_selection import train_test_split#用于数据切分·
from sklearn.metrics import  accuracy_score#用于评估
from  sklearn.model_selection import cross_val_score#用于验证

#加载数据
iris = datasets.load_iris()

#划分训练集和测试集
x,y = iris.data, iris.target
x_train,x_test,y_train,y_test = train_test_split(x,y,random_state=33)

#数据预处理
scaler = preprocessing.StandardScaler().fit(x_train)#标准化处理
x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)

#创建模型,k近邻
knn = neighbors.KNeighborsClassifier(n_neighbors=5)

#模型拟合
knn.fit(x_train,y_train)

#交叉验证
scores = cross_val_score(knn,x_train,y_train,cv=5,scoring='accuracy')
print(scores)#每组评分结果
print(scores.mean())

#预测
y_pred = knn.predict(x_test)

#评估
print(accuracy_score(y_test,y_pred))

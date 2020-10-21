#决策树

import numpy as np
from sklearn import tree,datasets,preprocessing
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import graphviz

np.random.RandomState(0)

#加载数据
wine = datasets.load_wine()

#划分
x,y = wine.data,wine.target
x_train,x_test,y_train,y_test= train_test_split(x,y,test_size=0.3)

#数据预处理
sca = preprocessing.StandardScaler().fit(x_train)
x_train = sca.fit_transform(x_train)
x_test=sca.fit_transform(x_test)

#创建模型
clf = tree.DecisionTreeClassifier()

#模型拟合
clf.fit(x_train,y_train)

#预测
y_pred= clf.predict(x_test)

#评估
print(accuracy_score(y_test,y_pred))

dot_data = tree.export_graphviz(clf,out_file=None,
                                feature_names=wine.feature_names,
                                class_names=wine.target_names,
                                filled=True,rounded=True,
                                special_characters=True)
grap = graphviz.Source(dot_data)
grap.render("wine")

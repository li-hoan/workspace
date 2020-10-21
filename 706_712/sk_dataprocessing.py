from sklearn import preprocessing
import numpy as np

import warnings
warnings.filterwarnings("ignore")

x = np.array([[1.,-1.,2.],
              [2., 0., 0.],
              [0.,1.,-3.]])

#标准化
#将每一列标准化，注意，针对每一列，而言
# x_scale = preprocessing.scale(x)
# print(x_scale)
# print(x_scale.mean(axis=0),x_scale.std(0))

#标准化
# scaler  =preprocessing.StandardScaler()
# x_scale = scaler.fit_transform(x)
# print(x_scale)

#min,max
# s = preprocessing.MinMaxScaler()
# xs = s.fit_transform(x)
# print(xs)

#maxabsscaler
# s = preprocessing.MaxAbsScaler()
# xs = s.fit_transform(x)
# print(x)

# #robuterscaler
# s = preprocessing.RobustScaler()
# xs = s.fit_transform(x)
# print(xs)
#

#normalizer
# s = preprocessing.Normalizer(norm="l2")
# xs = s.fit_transform(x)
# print(xs)

#二值化
# s = preprocessing.Binarizer(threshold=0)
# xs = s.fit_transform(x)
# print(xs)

#one-hot
# s = preprocessing.OneHotEncoder(n_values=3,sparse=False)
# n = s.fit_transform([[1],[2],[0],[1]])
# print(n)

#弥补缺失
# imp = preprocessing.Imputer(missing_values= "NaN",strategy ='mean',axis=0)
# data = np.array(([[np.nan,2],[6,np.nan],[7,6]]))
# y = imp.fit_tranform(data)
# print(data)
# print(y)

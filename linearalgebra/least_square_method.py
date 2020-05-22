# import torch
# import numpy as np
#
#
# a = torch.tensor([[1.,2.],[3.,4.]])
# print(torch.inverse(a))#torch求矩阵的逆
#
# b = np.array([[1.,2.],[3.,4.]])
# print(np.linalg.inv(b))#np里面求逆
#
# c = np.matrix(np.array([[1.,2.],[3.,4.]]))
# print(c.I)#即将淘汰的用法

import random
import numpy as np

x = np.array([[3],[1],[6]])
y = 4*x
# print(_x)
# print(_y)

print(np.linalg.inv(x.T@x)@x.T@y)
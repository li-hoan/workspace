import numpy as np
import torch

#实现one-hot
num_cla = 10

# arr =[1,2,3]
#
# one_hots  = np.eye(num_cla)[arr]
# print(one_hots)
#
# #返回
# # print(np.argmax(one_hot))
# data = [np.argmax(one_hot) for one_hot in one_hots ]
# print(data)


y  =torch.tensor([1,2,3,4])

one_hot = torch.zeros(y.size(0),num_cla).scatter(1,y.reshape(-1,1),1)
print(one_hot)
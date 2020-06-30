import torch
import numpy as np

# a = torch.tensor([[1.,2.],[3.,4.]])
# #求取特征值
# print(torch.eig(a))
# #特征值对应的特征向量
# print(torch.eig(a,eigenvectors=True))
a = torch.Tensor([[-1,1,0],[-4,3,0],[1,0,2]])
# print(torch.eig(a))
print(torch.eig(a,eigenvectors=True))

b=np.array([[-1,1,0],[-4,3,0],[1,0,2]])
print(np.linalg.eig(b))


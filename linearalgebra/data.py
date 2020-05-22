import numpy as np
import  torch

#0维标量
a = np.array(1)
print(a.shape)

b = torch.tensor(2)
print(b.shape)

#1维向量
c =np.array([1,2,3,4])
print(c.shape)

d = torch.tensor([1,2,3,4])
print(d.shape)

#2维矩阵
e = np.array([[1,2,3],[4,5,6]])
print(e.shape)

f = torch.tensor([[1,2,3],[4,5,6]])
print(f.shape)

#3维张量

g = np.array([[[1,2,3]]])
print(g.shape)

h = torch.tensor([[[1,2,3]]])
print(h.shape)
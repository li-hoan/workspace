import torch

a = torch.tensor([[1,2,3,4,5,6]])
print(a.shape)
print(a.reshape(3,2))
print(a.reshape(3,2,1))
b = a.reshape(3,2,1)
print(b.reshape(6))
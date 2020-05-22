import torch

a = torch.rand(1,4,5,3)
print(a)
b = a.permute((0,3,2,1))#torch 换轴
print(b.shape)


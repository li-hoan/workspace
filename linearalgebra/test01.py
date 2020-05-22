import torch

a = torch.tensor([[[1, 2, 3], [1, 3, 4]], [[1, 1, 2],[3, 1, 4]]])
b = torch.tensor([[[1, 2, 3], [1, 3, 4]], [[1, 1, 2],[3, 1, 4]]])

print(a)
print(a.shape)
print(a+b)

#张量叉乘只做最后两项的计算
c = torch.tensor([[[1],[2],[3]],[[2],[3],[4]]])
print(a@c)
print((a@c).shape)
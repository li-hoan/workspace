import torch

a = torch.tensor([[1,2],[3,4],[4,5]])
#b =torch.Tensor([2])#float
b = torch.tensor([[5,6],[7,8],[8,9]])
c = torch.tensor([[1,2],[3,4]])
print(a+b)
print(a-b)
print(a*b)
print(3*b)
print(a@c)#叉乘运算
print(torch.matmul(a,c))#叉乘函数

print(a.t())#转置

#向量叉乘，外积,格式只能如下
d = torch.tensor([1,2,3])
e = torch.tensor([2,3,4])
print(torch.cross(d,e))
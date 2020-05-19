import torch
import numpy

a = torch.tensor(1)
print(a, type(a))

b = numpy.array(1)
print(b, type(b))

# c = torch.tensor([[1, 2], [3, 4]])
# print(c)
#
# d = numpy.array([[1,2],[3,4]])
# print(d)

e = a.numpy()
print(e,type(e))
f = torch.from_numpy(b)
print(f,type(f))
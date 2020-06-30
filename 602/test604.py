import torch
import numpy as np


a = np.array([1,2,3],dtype=np.int8)
b = [1,2,3]
c = torch.tensor([1,2,3])
print(type(a))
print(a.dtype)
print(type(b))
print(type(c))
print(c.dtype)

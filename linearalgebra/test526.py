import numpy as np
import torch

#行列式的值，方正。
a = np.array([[1,2],[3,4]])
print(np.linalg.det(a))

b = torch.tensor([[1.,2.],[3.,4.]])
print(b.det())
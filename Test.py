import numpy as np
import torch

A = torch.arange(16 * 19 * 64 * 64 * 1).reshape(16,19,64,64,1)

B = A[:, -10:, :]

print(B.shape)

C = np.array([-2, -1, 0, 1, 2, -8, -7, 9, 2])
print(C)

C = np.maximum(C, 0)
print(C)
C = np.minimum(C, 1)
print(C)

print("============================================")
for i in range(1,18):
    print(i)
print("============================================")

arr = [1, 2, 2]

print(arr.count(2))


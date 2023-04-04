import torch

a = torch.arange(3).reshape((3,1))
b = torch.arange(2).reshape((1,2))

print(a)
print(b)
print(a + b)

print(a * b)

a = torch.arange(2).reshape((4,4))
b = torch.arange(1).reshape((1,1))

print(a)
print(b)

print(a * b)
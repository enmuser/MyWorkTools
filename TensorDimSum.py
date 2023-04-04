import torch


A = torch.arange(2 * 4 * 1 * 1).reshape(2,4,1,1)
B = torch.arange(2 * 4 * 1 * 1).reshape(2,4,1,1)
print("-------------------------------printA----------------------------")
print(A)
print("-------------------------------printB----------------------------")
print(B)
D = A * B
print("-------------------------------printD----------------------------")
print(D)
print("-------------------------------printD.shape----------------------------")
print(D.shape)
C = D.sum(dim=(1,2,3))
print("-------------------------------printC----------------------------")
print(C)
print("-------------------------------printC.shape----------------------------")
print(C.shape)
print("*****************************************************************************")

A = torch.arange(16 * 64 * 16 * 16).reshape(16,64,16,16)
B = torch.arange(16 * 64 * 16 * 16).reshape(16,64,16,16)
print("-------------------------------printA----------------------------")
print(A)
print("-------------------------------printB----------------------------")
print(B)
D = A * B
print("-------------------------------printD----------------------------")
print(D)
print("-------------------------------printD.shape----------------------------")
print(D.shape)
C = D.sum(dim=(1,2,3))
print("-------------------------------printC----------------------------")
print(C)
print("-------------------------------printC.shape----------------------------")
print(C.shape)
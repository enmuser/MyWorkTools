import torch
X = torch.tensor([[1.0,2.0,3.0],[4.0,5.0,6.0]])

rowSum = X.sum(0,keepdim=True)
print(rowSum)

colSum = X.sum(1,keepdim=True)
print(colSum)

# 指数平均值
def softmax(X):
    X_exp = torch.exp(X)
    partition = X_exp.sum(1,keepdim=True)
    return X_exp / partition
func = torch.nn.Softmax(dim=0)
print(func(X))

print(softmax(X))

Y = softmax(X)

print(Y.sum(dim=1))

print(func(X).sum(dim=0))


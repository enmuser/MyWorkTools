import torch

# 熟悉C字符串的同学们应该都用过strcat（）函数，这个函数在C/C++程序中用于连接2个C字符串。在pytorch中，同样有这样的函数，
# 那就是torch.cat()函数.
# 先上源码定义：torch.cat(tensors,dim=0,out=None)
#
# 第一个参数tensors是你想要连接的若干个张量，按你所传入的顺序进行连接，注意每一个张量需要形状相同，或者更准确的说，
# 进行行连接的张量要求列数相同，进行列连接的张量要求行数相同
# 第二个参数dim表示维度，dim=0则表示按行连接，dim=1表示按列连接

a=torch.tensor([[1,2,3,1],[1,2,3,2]])
b=torch.tensor([[1,2,3,4,1],[1,2,3,4,2]])
print(torch.cat((a,b),1))
#输出结果为：
# tensor([[1, 2, 3, 1, 1, 2, 3, 4, 1],
#         [1, 2, 3, 2, 1, 2, 3, 4, 2]])

print("--------------------------------------------------------------------------------")

# torch.cat()函数是把各个tensor连接起来，这里的torch.chunk（）的作用是把一个tensor均匀分割成若干个小tensor
# 源码定义:torch.chunk(intput,chunks,dim=0)
#
# 第一个参数input是你想要分割的tensor
# 第二个参数chunks是你想均匀分割的份数，如果该tensor在你要进行分割的维度上的size不能被chunks整除，则最后一份会略小（也可能为空）
# 第三个参数表示分割维度，dim=0按行分割，dim=1表示按列分割
# 该函数返回由小tensor组成的list

c=torch.tensor([[1,4,7,9,11],[2,5,8,9,13]])
print(torch.chunk(c,3,1))
# (tensor([[1, 4],
#         [2, 5]]), tensor([[7, 9],
#         [8, 9]]), tensor([[11],
#         [13]]))
c=torch.tensor([[1,4,7,9,11],[2,5,8,9,13]])
print(torch.chunk(c,3,0))
# (tensor([[ 1,  4,  7,  9, 11]]), tensor([[ 2,  5,  8,  9, 13]]))

print("--------------------------------------------------------------------------------")
# 这个函数可以说是torch.chunk（）函数的升级版本，它不仅可以按份数均匀分割，还可以按特定方案进行分割。
# 源码定义：torch.split(tensor,split_size_or_sections,dim=0)
#
# 第一个参数是待分割张量
# 第二个参数有两种形式。
# 一种是分割份数，这就和torch.chunk（）一样了。
# 第二种这是分割方案，这是一个list，待分割张量将会分割为len（list）份，每一份的大小取决于list中的元素
# 第三个参数为分割维度

section=[1,2,1,2,2]
d=torch.randn(8,4)
print(torch.split(d,section,dim=0))
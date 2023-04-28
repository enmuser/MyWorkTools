import csv

from matplotlib import pyplot as plt
#subdir = 'kth_channel_128'
#subdir = 'kth128'
#subdir = 'threemau_multidim_cross'
#subdir = 'mulmul_o_3x7'
#subdir = 'threemau_multidim_cache_cross'
#subdir = 'threemau_multidim_cache_cross_mul'

#subdir = 'kth128_40'
#subdir = 'kth_channel_128_40'
#subdir = 'ped_channel_cross'
#subdir = 'ped_channel'
subdir = 'taxibj_channel_fuse'


file = "plot/images/"+subdir+"/result.csv"
result_file = open(file)  # 打开csv文件
result_reader = csv.reader(result_file)  # 读取csv文件
result_data = list(result_reader)  # csv数据转换为列表
length_row = len(result_data)  # 得到数据行数
length_col = len(result_data[0])  # 得到每行长度

# for i in range(1,length_zu):
#     print(exampleData[i])

itrList = list()
mseList = list()
maeList = list()
psnrList = list()
ssimList = list()
lpipsList = list()

for i in range(0, length_row):
    print(i)# 从第二行开始读取
    itrList.append(int(result_data[i][0]))  # 将第一列数据从第二行读取到最后一行赋给列表x
    mseList.append(float("{:.3f}".format(float(result_data[i][1]))))
    maeList.append(float("{:.3f}".format(float(result_data[i][2]))))
    psnrList.append(float("{:.3f}".format(float(result_data[i][3]))))
    ssimList.append(float("{:.3f}".format(float(result_data[i][4]))))
    lpipsList.append(float("{:.3f}".format(float(result_data[i][5]))))

plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=1)
plt.subplot(5, 1, 1)
plt.plot(itrList, mseList,color='deepskyblue')
plt.title("mse")
plt.subplot(5, 1, 2)
plt.plot(itrList, maeList, color='orange')
plt.title("mae")
plt.subplot(5, 1, 3)
plt.plot(itrList, psnrList, color='green')
plt.title("psnr")
plt.subplot(5, 1, 4)
plt.plot(itrList, ssimList, color='red')
plt.title("ssim")
plt.subplot(5, 1, 5)
plt.plot(itrList, lpipsList, color='aquamarine')
plt.title("lpips")
plt.savefig("plot/images/"+subdir+"/allresult.svg", format="svg", dpi=3600)

plt.close()

plt.plot(itrList, mseList,color='deepskyblue')
plt.title("mse")
for a,b in zip(itrList,mseList):
    plt.text(a, b, '%.2f' % b, ha='center', va= 'bottom',fontsize=7)
plt.savefig("plot/images/"+subdir+"/mseresult.svg", format="svg", dpi=3600)

plt.close()

plt.plot(itrList, maeList, color='orange')
plt.title("mae")
for a,b in zip(itrList,maeList):
    plt.text(a, b, '%.2f' % b, ha='center', va= 'bottom',fontsize=7)
plt.savefig("plot/images/"+subdir+"/maeresult.svg", format="svg", dpi=3600)

plt.close()

plt.plot(itrList, psnrList, color='green')
plt.title("psnr")
for a,b in zip(itrList, psnrList):
    plt.text(a, b, '%.2f' % b, ha='center', va= 'bottom',fontsize=7)
plt.savefig("plot/images/"+subdir+"/psnrresult.svg", format="svg", dpi=3600)

plt.close()

plt.plot(itrList, ssimList, color='red')
plt.title("ssim")
for a,b in zip(itrList, ssimList):
    plt.text(a, b, '%.3f' % b, ha='center', va= 'bottom',fontsize=7)
plt.savefig("plot/images/"+subdir+"/ssimresult.svg", format="svg", dpi=3600)

plt.close()

plt.plot(itrList, lpipsList, color='aquamarine')
plt.title("lpips")
for a,b in zip(itrList, lpipsList):
    plt.text(a, b, '%.3f' % b, ha='center', va= 'bottom',fontsize=7)
plt.savefig("plot/images/"+subdir+"/lpipsresult.svg", format="svg", dpi=3600)

plt.close()
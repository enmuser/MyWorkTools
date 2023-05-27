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
#subdir = 'taxibj_channel_fuse'
#subdir = 'ped_channel_val_random'
#subdir = 'taxibj_channel_fuse_2'
#subdir = 'taxibj_channel_fuse_2_1'
#subdir = 'taxibj_channel_fuse_1'
#subdir = 'synpick_channel'
#subdir = 'taxibj_channel_fuse_1_1'
#subdir = 'taxibj_spacenet2'
#subdir = 'taxibj_cross'
#subdir = 'kitti_channel'
#subdir = 'spacenet2_cross'
#subdir = 'threemau_multidim_cross2'
#subdir = 'threemau_multidim_cross2_KL_5000'
#subdir = 'threemau_multidim_cross2_KL_10000'
#subdir = 'synpick_channel2'
#subdir = 'threemau_multidim_cross2_KL_5000_1'
#subdir = 'threemau_multidim_cross2_KL_UW'
#subdir = 'threemau_multidim_cross2_KL_UW_Origin'
#subdir = 'threemau_multidim_cross2_KL_20000'
subdir = 'compare_cross_MSE_UW'
file = "plot/images/"+subdir+"/result.csv"
result_file = open(file)  # 打开csv文件
result_reader = csv.reader(result_file)  # 读取csv文件
result_data = list(result_reader)  # csv数据转换为列表
length_row = len(result_data)  # 得到数据行数
length_col = len(result_data[0])  # 得到每行长度

# for i in range(1,length_zu):
#     print(exampleData[i])
flag = False
itrList = list()
mseList = list()
maeList = list()
psnrList = list()
ssimList = list()
lpipsList = list()

itrList2 = list()
mseList2 = list()
maeList2 = list()
psnrList2 = list()
ssimList2 = list()
lpipsList2 = list()

index = 0
for i in range(0, length_row):
    print(i)# 从第二行开始读取
    if int(result_data[i][0]) == 0:
       index += 1
    if index == 1:
        itrList.append(int(result_data[i][0]))  # 将第一列数据从第二行读取到最后一行赋给列表x
        mseList.append(float("{:.3f}".format(float(result_data[i][1]))))
        maeList.append(float("{:.3f}".format(float(result_data[i][2]))))
        psnrList.append(float("{:.3f}".format(float(result_data[i][3]))))
        ssimList.append(float("{:.3f}".format(float(result_data[i][4]))))
        lpipsList.append(float("{:.3f}".format(float(result_data[i][5]))))
    if index == 2:
        itrList2.append(int(result_data[i][0]))  # 将第一列数据从第二行读取到最后一行赋给列表x
        mseList2.append(float("{:.3f}".format(float(result_data[i][1]))))
        maeList2.append(float("{:.3f}".format(float(result_data[i][2]))))
        psnrList2.append(float("{:.3f}".format(float(result_data[i][3]))))
        ssimList2.append(float("{:.3f}".format(float(result_data[i][4]))))
        lpipsList2.append(float("{:.3f}".format(float(result_data[i][5]))))

plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=1)
plt.subplot(5, 1, 1)
plt.plot(itrList, mseList, color='deepskyblue')
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

plt.plot(itrList, mseList,color='deepskyblue',label='up')
plt.plot(itrList2, mseList2, color='sandybrown',label='down')
plt.legend(['up', 'down'])
plt.title("mse")
if flag:
    for a,b in zip(itrList, mseList):
        plt.text(a, b, '%.2f' % b, ha='center', va= 'bottom',fontsize=7)
plt.savefig("plot/images/"+subdir+"/mseresult.svg", format="svg", dpi=3600)

plt.close()

plt.plot(itrList, maeList, color='orange',label='up')
plt.plot(itrList2, maeList2, color='slategray',label='down')
plt.legend(['up', 'down'])
plt.title("mae")
if flag:
    for a,b in zip(itrList,maeList):
        plt.text(a, b, '%.2f' % b, ha='center', va= 'bottom',fontsize=7)
plt.savefig("plot/images/"+subdir+"/maeresult.svg", format="svg", dpi=3600)

plt.close()

plt.plot(itrList, psnrList, color='green',label='up')
plt.plot(itrList2, psnrList2, color='steelblue',label='down')
plt.legend(['up', 'down'])
plt.title("psnr")
if flag:
    for a,b in zip(itrList, psnrList):
        plt.text(a, b, '%.2f' % b, ha='center', va= 'bottom',fontsize=7)
plt.savefig("plot/images/"+subdir+"/psnrresult.svg", format="svg", dpi=3600)

plt.close()

plt.plot(itrList, ssimList, color='red',label='up')
plt.plot(itrList2, ssimList2, color='springgreen',label='down')
plt.legend(['up', 'down'])
plt.title("ssim")
if flag:
    for a,b in zip(itrList, ssimList):
        plt.text(a, b, '%.3f' % b, ha='center', va= 'bottom',fontsize=7)
plt.savefig("plot/images/"+subdir+"/ssimresult.svg", format="svg", dpi=3600)

plt.close()

plt.plot(itrList, lpipsList, color='aquamarine',label='up')
plt.plot(itrList2, lpipsList2, color='palegoldenrod',label='down')
plt.legend(['up', 'down'])
plt.title("lpips")
if flag:
    for a,b in zip(itrList, lpipsList):
        plt.text(a, b, '%.3f' % b, ha='center', va= 'bottom',fontsize=7)
plt.savefig("plot/images/"+subdir+"/lpipsresult.svg", format="svg", dpi=3600)

plt.close()
import codecs
import os

from PIL import Image

file_list = []
new_file_list = []
set_file_list = []
path= r"E:\papercode\STRPM\datasets\ucfsports\test.txt"
with codecs.open(path) as f:
    file_list = f.readlines()

for fileItem in file_list:
    new_file_list.append(fileItem.split(",")[0])

set_file_list = list(set(new_file_list))


for fileItem in set_file_list:
    innerfiles = os.listdir(fileItem)
    need_files = []
    for file in innerfiles:
        if not os.path.isdir(file) and os.path.splitext(file)[-1][1:] == 'jpg':
            need_files.append(fileItem + file)

    need_files.sort()
    # print(need_files)
    # print("dir: ", fileItem)
    # print("size: ",len(need_files))
    # print("-----------------------------------")

    for index in range(len(need_files)):
        im = Image.open(need_files[index])
        resize_im = im.resize((512,512))
        new_path = fileItem + str(index + 1) + '.png'
        resize_im.save(new_path)
        os.remove(need_files[index])

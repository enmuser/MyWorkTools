from PIL import Image, ImageSequence

im = Image.open("GIF/1.gif")  # 使用Image的open函数打开test.gif图像

index = 1
for frame in ImageSequence.Iterator(im):  # for循环迭代的取im里的帧
    cropped = frame.crop((0, 0, 585, 585))  # (left, upper, right, lower)
    cropped.save("GIF/frame%d.png" % index)  # 取到一个帧调用一下save函数保存，每次保存明明为frameX.png
    index += 1  # 序号依次叠加

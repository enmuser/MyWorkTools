from PIL import Image

img = Image.open("GIF/frame1.png")
print(img.size)
cropped = img.crop((0, 0, 585, 585))  # (left, upper, right, lower)
cropped.save("GIF/frame1crop.png")
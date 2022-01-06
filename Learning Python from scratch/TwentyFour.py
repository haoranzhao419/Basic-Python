from PIL import Image, ImageFilter

im = Image.open("D:\Camera\IMG_20190714_082446.jpg")
im2 = im.filter(ImageFilter.BLUR)
im2.save("blur.jpg")

from PIL import Image, ImageFilter, ImageFont, ImageDraw

import random


# 随机字母
def rndChar():
    return chr(random.randint(65, 90))  # 这个函数是生成一个随机字母的，用的是ASCLL码中字母的编号


# 随机颜色：
def rndColor():  # 背景的颜色
    return (random.randint(64, 255), \
            random.randint(64, 255), \
            random.randint(64, 255))


# 随机颜色2：
def rndColor2():  # 文字的颜色
    return (random.randint(37, 127), \
            random.randint(37, 127), \
            random.randint(37, 127))


# 240*60的图片：
width = 60 * 4  # 每个字母占位都是60px*60px
height = 60
image = Image.new("RGB", (width, height), (255, 255, 255))  # 颜色模型是RGB, 宽高， 底色颜色是白色
# 创建Font对象：
font = ImageFont.truetype("Arial.ttf", 36)
# 创建Draw对象：
draw = ImageDraw.Draw(image)
# 填充每个像素：
for x in range(width):
    for y in range(height):
        draw.point((x, y), rndColor())

# 输出文字：
for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), rndColor2(), font)

# 模糊:
image = image.filter(ImageFilter.BLUR)
image.save("code.jpg", "jpeg")

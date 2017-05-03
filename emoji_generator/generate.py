# -*- coding: utf-8 -*-


from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


def generate_emoji(text, fonttype="Ricty-Bold.ttf", fontsize=64):

    # Specify TrueType font and Fontsize
    font = ImageFont.truetype(fonttype, fontsize)
    image = Image.new("RGB", (128, 128), (255, 255, 255))
    draw = ImageDraw.Draw(image)

    draw.text((0, 0), "{}\n{}".format(text[0:3], text[2:4]), font=font, fill="#000000")
    image.save("emoji_{}.png".format(text), "PNG")

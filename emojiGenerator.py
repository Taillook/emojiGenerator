# -*- encoding:utf8 -*-

from PIL import Image, ImageDraw, ImageFont
import sys

def emoji_generate(text):
    #TureTypeFont and FontSize
    font = ImageFont.truetype("RictyDiminished-Bold.ttf", 64)

    image = Image.new('RGB', (128, 128), (255, 255, 255))
    draw = ImageDraw.Draw(image)

    #(xPoint, yPoint) String FontColor
    draw.text((0, 0), text[0:3] + "\n" + text[2:5], font = font, fill='#000000')

    image.save('emoji.png', 'PNG')

emoji_generate(sys.argv[1])


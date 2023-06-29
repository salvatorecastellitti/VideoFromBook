import os
from PIL import ImageFont, ImageDraw, Image
import textwrap

PATH_FONT = 'Fonts/'

PATH_IMAGE = "Images/"
subfolders = [ f.name for f in os.scandir(PATH_IMAGE) if f.is_dir() ]
subfolders = [eval(i) for i in subfolders]

if(len(subfolders) == 0):
    folder_name = '1'
else:
    folder_name = str(max(subfolders)+1)

os.mkdir(PATH_IMAGE + folder_name)
PATH_IMAGE = PATH_IMAGE + folder_name + '/'



def create_image_from_text(text: str, num: str):
    width = 405
    height = 240

    img = Image.new('RGB', (width, height), color='white')
    #font = ImageFont.truetype(PATH_FONT +"Roboto-Black.pil",15)
    font = ImageFont.truetype(PATH_FONT + "Roboto-Black.ttf", size=22)
    imgDraw = ImageDraw.Draw(img)

    lines = textwrap.wrap(text, width=35)
    y_text = height/2
    for idx,line in enumerate(lines):

        widthFont, heightFont = font.getsize(line)
        if(idx == 0):
            y_text =  y_text - heightFont
        imgDraw.text(((width - widthFont) / 2, y_text), line, font=font, fill=(0, 0, 0))
        y_text += heightFont

    img.save(PATH_IMAGE + f"img{num}.png")

    return PATH_IMAGE

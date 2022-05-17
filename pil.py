from PIL import Image, ImageDraw, ImageFont
import os
new_size = (1080,1080)
images = [image for image in os.listdir()]

for i in os.listdir():
        img = Image.open(i)
        width,height = img.size 
        x = width - width / 5
        y = height - height / 7 
        
        fn, fext = os.path.splitext(i)
        new_img = img.convert('L')
        new_img.thumbnail(new_size)
        draw = ImageDraw.Draw(new_img)
        draw.text((x, y), "Sardar", font = ImageFont.truetype("arial.ttf", 30), fill='#000000')
        new_img.show()
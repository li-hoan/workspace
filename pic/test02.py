#生成验证码
import random
from PIL import Image,ImageDraw,ImageFont

class Generatecode:
    def getcode(self):#A-Z
# print(chr(65))#A-Z为65-90
        return  chr(random.randint(65,90))
    def bg_color(self):
        return (random.randint(0,160),
                random.randint(0,160),
                random.randint(0,160)
                )
    def fr_color(self):
        return (
            random.randint(120, 255),
            random.randint(120, 255),
            random.randint(120, 255))
    def gen_pic(self):
        #画板
        w,h = 240,60
        img = Image.new(size=(w,h),mode="RGB",color=(255,255,255))
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(font="Lobster-Regular.ttf",size=30)
        for y in range(h):
            for x in range(w):
                draw.point((x,y),fill=self.bg_color())

        for i in range(4):
            draw.text((60*i+20,15),text=self.getcode(),fill=self.fr_color(),font=font)
            draw.rectangle((10,10,50,50))#画框
        img.show()
        img.save("test.jpg")

g  =Generatecode()
g.gen_pic()
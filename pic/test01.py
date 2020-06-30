from PIL import Image,ImageFilter
import matplotlib.pyplot as plt

img = Image.open(r'image/minons.jpg')#相对路径,r取消转义
img.show()
# plt.imshow(img)
# plt.title("earth")
# plt.show()

w,h = img.size
print(w,h)
bands = img.getbands()
print(bands)
mode = img.mode
print(mode)

# #缩放
# # img = img.resize((300,300))
# # img.show()
#
# #等比缩放
# # img.thumbnail((w//2,h//2),resample=Image.ANTIALIAS)#抗锯齿
# # img.show()
#
# #抠图
# # img = img.crop((100,100,400,400))
# # img.show()
# #
# # #旋转
# # img = img.rotate(90)
# # img.show()
#
# #滤波器
# # img = img.filter(ImageFilter.CONTOUR)
# # img.show()
# # img = img.filter(ImageFilter.BLUR)
# # img.show()
# # img = img.filter(ImageFilter.BoxBlur(radius=20))
# # img.show()
# # img = img.filter(ImageFilter.DETAIL)
# # img.show()
# # img = img.filter(ImageFilter.EMBOSS)
# # img.show()
# # img = img.filter(ImageFilter.EDGE_ENHANCE)
# # img.show()
#
# #加logo
#
# logo = Image.open('image/earth.jpg')
# logo = logo.resize((60,60),resample=Image.ANTIALIAS)
# img.paste(logo,(100,100))
# img.show()
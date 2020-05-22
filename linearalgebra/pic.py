from PIL import Image
import numpy as np

img  = Image.open("pic.jpg")#打开图片
img_data = np.array(img)#将图片数组化
print(img_data.shape)
print(img_data)
img_data = img_data.reshape(300*533*3)#重塑造型
print(img_data)
print(img_data.shape)

img_data = img_data.reshape(300,533,3)
img_data = img_data.transpose(1,0,2)#转置，换轴
img = Image.fromarray(img_data)#从数组转为图片fromarray
img.show()


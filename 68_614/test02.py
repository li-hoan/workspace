import numpy as np
from PIL import Image

img = Image.open("image/p1.jpg")
img_data = np.array(img)
w,h,c = img_data.shape
print(w,h,c)
img_data = img_data.reshape(2,w//2,2,h//2,c)#对应切割
print(img_data.shape)
img_data = img_data.transpose(0,2,1,3,4)
img_data = img_data.reshape(-1,w//2,h//2,c)
print(img_data.shape)
img_arr = np.split(img_data,4,axis=0)#split切分，支持维度切分
for i,img_d in enumerate(img_arr):#enumerate枚举，返回索引和值
    img = Image.fromarray(img_d[0],"RGB")#取出批次，给它模式
    # img.show()
    img.save("image/s{}".format(i)+".jpg")


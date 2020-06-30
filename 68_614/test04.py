import numpy as np
import cv2

# img = np.random.randint(0,255,(200,300,3),np.uint8)#定义范围，大小，和数据类型
img = np.zeros((200,300,3),np.uint8)
# img[:,:,2]=255
img[...,1]=255
img[...,0]=255
img[...,2]=255
cv2.imwrite("img_save.jpg",img)
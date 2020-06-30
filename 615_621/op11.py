#车牌提取
import cv2
import numpy as np

orimg = cv2.imread("image/23.jpg")
#高斯模糊，将图片平滑化，去掉干扰噪声
img = cv2.GaussianBlur(orimg,(3,3),1)
#图片灰度化
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#Sobel算子X
sobel_x = cv2.Sobel(img,cv2.CV_16S,1,0)
# sobel_y = cv2.Sobel(img,cv2.CV_16S,0,1)

absx  = cv2.convertScaleAbs(sobel_x)#转为uint8


img = absx


ret,img = cv2.threshold(img,0,255,cv2.THRESH_OTSU)

k = cv2.getStructuringElement(cv2.MORPH_RECT,(17,5))
img = cv2.morphologyEx(img,cv2.MORPH_CLOSE,k)

#膨胀腐蚀
kx = cv2.getStructuringElement(cv2.MORPH_RECT,(20,1))
ky = cv2.getStructuringElement(cv2.MORPH_RECT,(1,19))
img = cv2.dilate(img,kx)
img = cv2.erode(img,kx)
img = cv2.erode(img,ky)
img = cv2.dilate(img,ky)

#中值滤波
img = cv2.medianBlur(img,15)

#查找轮廓
contour,_ = cv2.findContours(img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

for item in contour:
    rect = cv2.boundingRect(item)
    x = rect[0]
    y  =rect[1]
    weight = rect[2]
    height = rect[3]
    if weight>(height*2) and height>6:
        #剪裁区域图片
        chepai = orimg[y:y+height,x:x+weight]
        cv2.imshow('chepai'+str(x),chepai)
#绘制轮廓
img = cv2.drawContours(orimg,contour,-1,(0,0,255),3)


cv2.imshow("1",img)
cv2.waitKey(0)
exit()
cv2.destroyAllWindows()


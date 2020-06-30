#草地分割
import cv2
import numpy as np

r = cv2.imread('image/10.jpg')
h = cv2.cvtColor(r,cv2.COLOR_BGR2HSV)

t = cv2.imread("image/9.jpg")
ht = cv2.cvtColor(t,cv2.COLOR_BGR2HSV)

rht = cv2.calcHist([h],[0,1],None,[180,255],[0,180,0,255])
dst = cv2.calcBackProject([ht],[0,1],rht,[0,180,0,255],1)#直方图反投影

dis = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
dst = cv2.filter2D(dst,-1,dis)


ret,thresh = cv2.threshold(dst,50,255,0)

thresh= cv2.merge((thresh,thresh,thresh))#通道融合，融合成三通道

res = cv2.bitwise_and(t,thresh)

res = np.hstack((t,thresh,res))#堆叠函数水平堆叠，垂直堆叠vstack

cv2.imshow('img',res)
cv2.waitKey(0)

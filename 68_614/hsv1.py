import cv2
import numpy as np

img = cv2.imread("image1/11.jpg")
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
lower_blue = np.array([0,110,100])
upper_blue = np.array([200,255,200])
mask = cv2.inRange(hsv, lower_blue,upper_blue)#在范围内取255，其他为0
res = cv2.bitwise_and(img,img,mask=mask)
cv2.imshow("frame",img)
cv2.imshow("mask",mask)
cv2.imshow("1",res)
cv2.waitKey(0)
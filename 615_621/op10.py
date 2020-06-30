#边界检测
import cv2
import numpy as np

img = cv2.imread("image/16.jpg")

imggray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,th = cv2.threshold(imggray,127,255,0)

contour,_ = cv2.findContours(th,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

#边界矩形
x,y,w,h = cv2.boundingRect(contour[0])
i = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

#最小矩形
rect = cv2.minAreaRect(contour[0])
box = cv2.boxPoints(rect)
box = np.int0(box)
i = cv2.drawContours(img,[box],0,(0,0,255),2)

#最小外切圆
(x,y),radius = cv2.minEnclosingCircle(contour[0])
center = (int(x),int(y))
radius = int(radius)
i = cv2.circle(img,center,radius,(255,0,0),2)

cv2.imshow("1",i)
cv2.waitKey(0)





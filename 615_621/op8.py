#近似轮廓
import cv2

img = cv2.imread('image/26.jpg')

imggray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,th = cv2.threshold(imggray,127,255,0)

cntours,_ = cv2.findContours(th,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

e = 60#偏差度
approx = cv2.approxPolyDP(cntours[0],e,True)

img_contour = cv2.drawContours(img,[approx],-1,(0,0,255),3)


cv2.imshow("img_contour",img_contour)
cv2.waitKey(0)

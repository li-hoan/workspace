#凸包性
import cv2

img = cv2.imread('image/16.jpg')

imggray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,th = cv2.threshold(imggray,127,255,0)

contour,_ = cv2.findContours(th,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

hull = cv2.convexHull(contour[0])#不光可以判断，还可以纠正

print(cv2.isContourConvex(contour[0]),cv2.isContourConvex(hull))

img_contour = cv2.drawContours(img,[hull],-1,(0,0,255),3)

cv2.imshow("1",img_contour)
cv2.waitKey(0)
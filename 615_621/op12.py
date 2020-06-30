#形状匹配
import cv2

img1 = cv2.imread('image/16.jpg',0)
img2 = cv2.imread('image/17.jpg',0)

ret,th1 = cv2.threshold(img1,127,255,0)
contour,h = cv2.findContours(th1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
c1 = contour[0]

ret,th2 = cv2.threshold(img2,127,255,0)
contour,h = cv2.findContours(th2,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
c2 = contour[0]

ret = cv2.matchShapes(c1,c2,cv2.CONTOURS_MATCH_I2,0.0)
print(ret)
import cv2
import numpy as np

img = cv2.imread("image/wheel.jpg",0)
# cv2.imshow("img",img)

# kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], np.float32)
# img = cv2.filter2D(img,-1,kernel)
# img = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
cv2.imshow("img1",img)


img = cv2.convertScaleAbs(img,alpha=5,beta=0)
cv2.imshow("abs",img)
# img = cv2.GaussianBlur(img,(5,5),1)
# k = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
# img = cv2.morphologyEx(img,cv2.MORPH_CLOSE,k,iterations=1)
# img = cv2.morphologyEx(img,cv2.MORPH_OPEN,k,iterations=1)
canny = cv2.Canny(img,100,150)
cv2.imshow("canny",canny)

cv2.waitKey(0)

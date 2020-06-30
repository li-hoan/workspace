import cv2
import numpy as np

scr = cv2.imread("image/1.jpg")
k = np.array([[1,1,0],[1,0,-1],[0,-1,-1]],np.float32)
dst = cv2.filter2D(scr,-1,kernel=k)

cv2.imshow("scr", scr)
cv2.imshow("dst",dst)

cv2.waitKey(0)
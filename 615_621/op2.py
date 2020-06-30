import cv2
import numpy as np

scr = cv2.imread("image/25.jpg")

#均值滤波
# dst = cv2.blur(scr,(5,5))
#高斯滤波
# dst = cv2.GaussianBlur(scr,(5,5),1)
#中指滤波
# dst = cv2.medianBlur(scr,5)
#双边滤波,保持边缘，降噪平滑
dst = cv2.bilateralFilter(scr,9,75,75)


cv2.imshow("scr",scr)
cv2.imshow("dst",dst)
cv2.waitKey(0)

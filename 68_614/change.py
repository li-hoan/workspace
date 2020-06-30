import cv2
import numpy as np

scr = cv2.imread("image1/1.jpg")
rows,cols,channel = scr.shape

# # dst = cv2.resize(scr,(cols*2,rows*2),interpolation=cv2.INTER_CUBIC)
# # dst = cv2.resize(scr,(cols//2,rows//2))
# # dst = cv2.transpose(scr)#翻转
# dst = cv2.flip(scr,1)#翻转，按数字来
# cv2.imshow("1",scr)
# cv2.imshow("2",dst)
# cv2.waitKey(0)

#仿射变换
src = cv2.imread('image1/1.jpg')

rows, cols, channel = src.shape

# M = np.float32([[1, 0, 50], [0, 1, 80]])
# M = np.float32([[0.5, 0, 0], [0, 0.5, 0]])
# M = np.float32([[-0.5, 0, cols // 2], [0, 0.5, 0]])
# M = np.float32([[1, 0.5, 0], [0, 1, 0]])
M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 0, 0.7)
dst = cv2.warpAffine(src, M, (cols, rows))

cv2.imshow('src pic', src)
cv2.imshow('dst pic', dst)

cv2.waitKey(0)
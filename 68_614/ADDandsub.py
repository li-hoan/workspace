import cv2
import numpy as np

# x = np.uint8([250])
# y = np.uint8([10])
# print(cv2.add(x,y))#大于255，都按255处理
# print(cv2.subtract(x,y))

img1 = cv2.imread("image1/1.jpg")
img2 = cv2.imread("image1/6.jpg")

# dst = cv2.addWeighted(img1,0.7,img2,0.3,0)
#
# cv2.imshow("dst",dst)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

rows,cols,channelsn=img2.shape
roi = img1[0:rows,0:cols]
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray,10,255,cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)
# cv2.imshow("mask_inv",mask_inv)
img1_bg = cv2.bitwise_and(roi,roi,mask=mask_inv)#按照mask对图像进行镂空
# cv2.imshow("1",img1_bg)
img2_fg = cv2.bitwise_and(img2,img2,mask=mask)
# cv2.imshow("2",img2_fg)
dst = cv2.add(img1_bg,img2_fg)
img1[0:rows, 0:cols]=dst
cv2.imshow("3",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
#图像金字塔
import cv2

# img = cv2.imread("image/13.jpg")
# for i in range(3):
#     cv2.imshow(f"img{i}",img)
#     # img = cv2.pyrDown(img)#下采样
#     img = cv2.pyrUp(img)#上采样
#
# cv2.waitKey(0)
#拉普拉斯金字塔,用于提轮廓
img = cv2.imread("image/12.jpg")
img_down = cv2.pyrDown(img)
img_up = cv2.pyrUp(img_down)
img_new = cv2.subtract(img,img_up)
#为了看清除,做了个提高对比度的操作
img_new = cv2.convertScaleAbs(img_new,alpha=5,beta=0)
cv2.imshow('1',img_new)
cv2.waitKey(0)
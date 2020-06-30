import cv2

#单目标匹配
# img = cv2.imread('image/9.jpg', 0)
# template = cv2.imread('image/18.jpg', 0)
# h, w = template.shape
#
# res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF)
# min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
#
# bottom_right = (max_loc[0] + w, max_loc[1] + h)
# cv2.rectangle(img, max_loc, bottom_right, 255, 2)
#
# cv2.imshow("img", img)
# cv2.waitKey(0)

#多目标匹配
import numpy as np

img_rgb = cv2.imread('image/19.jpg')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('image/20.jpg', 0)
h, w = template.shape

res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)

loc = np.where(res >= 0.8)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

cv2.imshow('img', img_rgb)
cv2.waitKey(0)
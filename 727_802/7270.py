import cv2

img = cv2.imread("cat.jpg")
cv2.imshow('1',img)
img = img.resize(300,300)
cv2.imshow('2',img)
cv2.waitKey()
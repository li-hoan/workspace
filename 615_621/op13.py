#统计直方图
import  cv2
import matplotlib.pyplot as plt

img=cv2.imread("image/8.jpg",0)
cv2.imshow("1",img)


# img = cv2.imread("image/1.jpg")
#
# cv2.imshow('1',img)
#
# img_b = cv2.calcHist([img],[0],None,[255],[0,255])
# plt.plot(img_b,label="B",color = 'r')
# img_g = cv2.calcHist([img],[1],None,[255],[0,255])
# plt.plot(img_g,label="G",color = 'g')
# img_r = cv2.calcHist([img],[2],None,[255],[0,255])
# plt.plot(img_r,label="R",color = 'r')
#均衡化
# dst = cv2.equalizeHist(img)
# cv2.imshow("2",dst)
# img_c = cv2.calcHist([dst],[0],None,[255],[0,255])
# plt.plot(img_c,label="g",color = 'g')
#自适应均衡化
d = cv2.createCLAHE(clipLimit=2.0,tileGridSize=(8,8))
ds = d.apply(img)
cv2.imshow("2",ds)


cv2.waitKey(0)
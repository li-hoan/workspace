import cv2

img = cv2.imread("image/14.jpg")
imggray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret, th = cv2.threshold(imggray,127,255,0)

#findcontour包含canny
contours, ha = cv2.findContours(th,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)#retr_tree得到轮廓树，后面为提取轮廓的方式
print(len(contours[0]))#contour以list给出

M = cv2.moments(contours[0])#得到矩
print("M",M)

cx,cy = int(M['m10']/M['m00']),(M['m01']/M['m00'])
print('重心',cx,cy)

area = cv2.contourArea(contours[0])
print("面积：",area)

p = cv2.arcLength(contours[0],True)
print("周长",p)


img_contour = cv2.drawContours(img, contours,-1,(0,0,255),2)

cv2.imshow("im",img_contour)
cv2.waitKey(0)
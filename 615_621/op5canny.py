import cv2

img = cv2.imread("image/25.jpg",0)
cv2.imshow("canny2",img)

img = cv2.convertScaleAbs(img,alpha=6,beta=0)
cv2.imshow("abs",img)
img = cv2.GaussianBlur(img,(5,5),1)
k = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
img = cv2.morphologyEx(img,cv2.MORPH_CLOSE,k,iterations=1)
img = cv2.morphologyEx(img,cv2.MORPH_OPEN,k,iterations=1)
canny = cv2.Canny(img,100,150)
canny = cv2.resize(canny,dsize=(500,500))
cv2.imshow("canny",canny)
cv2.waitKey(0)
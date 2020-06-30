import cv2

img = cv2.imread("image1/1.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,binary = cv2.threshold(gray,0,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
cv2.imshow("1",gray)
cv2.imshow("2",binary)
cv2.waitKey(0)
cv2.destroyAllWindows()

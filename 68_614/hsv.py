import cv2

arc = cv2.imread("image/p3.jpg")
dst = cv2.cvtColor(arc,cv2.COLOR_BGR2HSV)
cv2.imshow("1",arc)
cv2.imshow("2",dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
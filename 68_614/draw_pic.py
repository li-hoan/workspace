import cv2
import numpy as np

img = cv2.imread("image1/1.jpg")
# cv2.line(img,(100,30),(210,180),color=(0,0,255),thickness=3)#绘制直线
# cv2.circle(img,(100,100),60,(0,255,0),thickness=3)#画圆
# cv2.rectangle(img,(100,30),(210,180),(255,0,0),thickness=3)#画矩形
# cv2.ellipse(img,(150,150),(100,50),50,0,360,(0,255,255),thickness=3)#画椭圆
#画多边形
# pts = np.array([[10,20],[100,50],[90,10],[20,40]])
# cv2.polylines(img,[pts],False,(0,0,255),thickness=3)
#写汉字
cv2.putText(img,"hello world",(100,100),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),lineType=cv2.LINE_AA)#后面为抗锯齿
cv2.imshow("1",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

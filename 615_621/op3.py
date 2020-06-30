import cv2
import numpy as np

src = cv2.imread("image/1.jpg")

#锐化
# kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], np.float32)
# dst = cv2.filter2D(src,-1,kernel)
#USM锐化
# dst = cv2.GaussianBlur(src,(5,5),0)#高斯模糊去噪
# dst = cv2.addWeighted(src,2,dst,-1,0)
#拉普拉斯，高通滤波，提取轮廓
dst = cv2.Laplacian(src,-1)



cv2.imshow("src",src)
cv2.imshow("dst",dst)
cv2.waitKey(0)



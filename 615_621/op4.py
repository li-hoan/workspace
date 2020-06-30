#梯度算子,sobel和scharr
import  cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("image/2.jpg",0)
la = cv2.Laplacian(img,cv2.CV_64F)
# sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
# sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
sobelx = cv2.Scharr(img,cv2.CV_64F,1,0)
sobely = cv2.Scharr(img,cv2.CV_64F,0,1)


plt.subplot(2,2,1),plt.imshow(img,cmap='gray')
plt.title("original"),plt.xticks([]),plt.yticks([])
plt.subplot(2,2,2),plt.imshow(la,cmap="gray")
plt.title("la"),plt.xticks([]),plt.yticks([])
plt.subplot(2,2,3),plt.imshow(sobelx,cmap='gray')
plt.title("sobelx"),plt.xticks([]),plt.yticks([])
plt.subplot(2,2,4),plt.imshow(sobely, cmap='gray')
plt.title('sobely'),plt.xticks([]),plt.yticks([])
plt.show()











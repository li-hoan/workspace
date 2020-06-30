import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('image/9.jpg',0)

f = np.fft.fft2(img)#傅里叶变换
# print(f.shape)
fshift = np.fft.fftshift(f)#把中点移到中间去


magnitude_specturm = 20*np.log(np.abs(fshift))#计算每个频率的成分多少
# cv2.imshow("1",magnitude_specturm)
# cv2.waitKey(0)
# exit()
plt.figure(figsize=(10,10))
plt.subplot(221),plt.imshow(img,cmap='gray')
plt.title("input image"),plt.xticks([]),plt.yticks([])
plt.subplot(222),plt.imshow(magnitude_specturm,cmap="gray")#亮的是频率小的
plt.title("ma"),plt.xticks([]),plt.yticks([])
# plt.show()

#去掉低频,留下高频

row,col = img.shape
crow,ccol = row//2,col//2
fshift[crow-30:crow+30,ccol-30:ccol+30]=0

#傅里叶逆变换

f_i = np.fft.ifftshift(fshift)
img_back = np.fft.ifft2(f_i)
img_back = np.abs(img_back)

plt.subplot(223),plt.imshow(img_back,cmap="gray")
plt.title("im"),plt.xticks([]),plt.yticks([])
plt.subplot(224),plt.imshow(img_back)
plt.title("re"),plt.xticks([]),plt.yticks([])

plt.show()
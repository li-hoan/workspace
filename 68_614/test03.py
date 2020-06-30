#print(bin(255))#bin转二进制
import cv2
from PIL import Image


img = cv2.imread("image/p2.jpg")#0代表模式,返还的是ndarray的模式
# img = img[...,::-1]#将BGR改为RGB
# img = Image.fromarray(img)
# img.show()
cv2.imshow("pic show",img)#使用opencv自带的窗口显示图片，是个非阻塞方法
cv2.waitKey(0)#0等待，其他为时间ms
cv2.destroyAllWindows()#摧毁掉所有窗口，非必须
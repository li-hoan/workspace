import cv2
import numpy as np

# l = cv2.imread("cat.jpg")
# data = np.zeros((200,200,3),dtype=np.uint8)
# data[...,0]=255
# data[...,1]=255
# cv2.imwrite("pic.jpg",data)
# cv2.imshow("cat",l)
# cv2.waitKey(0)

vi = cv2.VideoCapture("http://ivi.bupt.edu.cn/hls/cctv1hd.m3u8")
while True:
    ret,frame =vi.read()
    cv2.imshow("ha",frame)
    cv2.waitKey(21)



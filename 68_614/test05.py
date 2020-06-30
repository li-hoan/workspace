import cv2

# 创建视频对象
cap = cv2.VideoCapture("http://ivi.bupt.edu.cn/hls/cctv1.m3u8")#0为摄像头
while True:
    ret, frame = cap.read()#ret:bool型，表示视频是否读取成功：frame每帧的画面
    cv2.imshow("frame",frame)
    if cv2.waitKey(41)& 0xFF == ord('q'):
        break
cap.release()#释放视频资源
cv2.destroyAllWindows()#关闭窗口

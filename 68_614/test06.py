import cv2
from PIL import Image


src = cv2.imread(r"image/p3.jpg")
dst = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)
img = Image.fromarray(dst,'RGB')
img.show()
# dst = cv2.cvtColor(src,cv2.COLOR_BGR2YUV)
cv2.imshow("src show",src)
cv2.imshow("dst show",dst)
cv2.waitKey(0)
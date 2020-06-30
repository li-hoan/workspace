import  cv2
import numpy as np

a = cv2.imread("image/21.jpg")
b = cv2.imread("image/22.jpg")

#generate Gaussian pyramid for a
g = a.copy()
gpa = [g]
for i in range(6):
    g = cv2.pyrDown(g)
    gpa.append(g)

g = b.copy()
gpb = [g]
for i in range(6):
    g = cv2.pyrDown(g)
    gpb.append(g)

#拉普拉斯金字塔
lpa = [gpa[5]]
for i in range(5,0,-1):
    ge = cv2.pyrUp(gpa[i])
    l = cv2.subtract(gpa[i-1],ge)

    lpa.append(l)


lpb = [gpb[5]]
for i in range(5,0,-1):
    ge = cv2.pyrUp(gpb[i])
    l = cv2.subtract(gpb[i-1],ge)
    lpb.append(l)

#将两半相加
LS = []
for i,(la,lb) in enumerate(zip(lpa,lpb)):
    row,col,dpt = la.shape
    ls = np.hstack((la[:,0:col//2],lb[:,col//2:]))
    LS.append(ls)

#重新构建
ls_ = LS[0]
for i in range(1,6):
    ls_ = cv2.pyrUp(ls_)#对原始的苹果橘子图做上采样
    ls_ = cv2.add(ls_,LS[i])
    cv2.imshow(f"xxx{i}",ls_)

real = np.hstack((a[:,:col//2],b[:,col//2:]))

cv2.waitKey(0)
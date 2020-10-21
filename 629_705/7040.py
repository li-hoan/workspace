import numpy as np

wine = open("winedata.txt")
winedata = wine.readlines()#按行读取
print(winedata)

x=[]
y=[]
for l in winedata:
    str = l.strip().split(",")#先去空格strip，切割，号。
    _y = np.float64(str[0])
    _x = np.float64(str[1:])
    x.append(_x)
    y.append(_y)
x = np.stack(x)#组装list和array,成array
y = np.stack(y)
print(type(x))
print(y)

#用numpy
z = np.loadtxt("winedata.txt",delimiter=",")
print(z)
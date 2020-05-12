a = float(input("圆的半径："))
pi = 3.1415926
b  = pi*(a*a)
print("圆的面积为：%f"%b)
def area(r):
    pi = 3.1415926
    return pi*(r**2)
print("圆的面积为%f"%area(9))
# num = int(input("输入一个数："))
# if num % 2==0:
#     print("偶数")
# else:
#     print('奇数')
y = int(input("输入一个年份："))
if y % 4 == 0:
    if y%100 ==0:
        if y%400 ==0:
            print('{0}是闰年'.format(y))
        else:
            print('{0}不是闰年'.format(y))
    else:
        print('{0}是闰年'.format(y))

else:
    print('{0}不是闰年'.format(y))
import cmath
a = [1, 2,3,4]
print(len(a))
print(a[2])

#修改第三个元素
a[2] = 5
print(a)
#删除第四个元素
a.remove(a[3])
print(a)
#在尾部添加一个元素
a.append(9)
print(a)
#在第二个元素前面添加一个元素
a.insert(2, 7)
print(a)
#在集合后面添加一个集合
a.extend([1,2,3])
print(a)
#查看7的索引
print(a.index(7))
#排序
a.sort()
print(a)
a.sort(reverse=True)
print(a)
#清除
a.clear()
print(a)
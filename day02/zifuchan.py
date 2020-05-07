a = "hello"
b ="world"
c = a + " " + b
print(c)

d = a + "\n" +b#zhuanzhe
print(d)
#普通字符串和r字符串
print("hello\nworld")
print(r"hello\nworld")
#字符串切片
print(a[1:])

#查找字符串
print(a.index("llo"))#若不纯在，会报错
print(a.find("llo"))#若不存在，返回-1

#格式化字符串
print("{} {}!".format(a, b))
print(f"{a} {b}!")
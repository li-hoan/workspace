# a = 1
# print(type(a),a)
# a = 1.23
# print(type(a),a)
# a = True
# print(type(a),a)
# b = "hello"
# print(type(b), b)
# c = "world"
# d = b + "\n" + c
# print(d)
a = [1, 2, 3, 5, 6]
# print(type(a),a[0:3])
# print(a[::2])
a.append(7)
print(a)
a.insert(2,9)
print(a)
a.remove(9)
print(a)
print(tuple(a))
print(a.index(2))
a.append(2)
print(a)

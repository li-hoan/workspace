a = [1, 2, 3, 4]
print(len(a))
print(a[2])

a.remove(a[2])
print(a)

a.extend([0, 1, 3])
print(a)

a.insert(4, 7)
print(a)

a.append(9)
print(a)

a.pop(0)
print(a)

print(a.index(9))

a.sort()
print(a)
a.sort(reverse=True)
print(a)
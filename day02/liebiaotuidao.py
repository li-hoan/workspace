a_li = [1, 2, 3]
b_li = []
for a in a_li:
    b_li.append(a*2)
print(b_li)

c_li = [x*2 for x in a_li]
print(c_li)
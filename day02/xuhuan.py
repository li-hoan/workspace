for i in range(10):
    print(i, end=" ")
for i in range(10):
    print(i)

a_list = [1, 2, 3, 4, 5, 6, 7]
for i in a_list:
    print(i, end=" ")

for i , a in enumerate(a_list):
    print(i, ":", a)

b_dict = {"name":"zhang","sex":"nan","height":"1.75"}
for key, value in b_dict.items():
    print(key, ":", value)
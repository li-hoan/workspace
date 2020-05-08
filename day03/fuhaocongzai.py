class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __add__(self, other):
        return self.age + other.age

li = person("xiao",25)
wang  = person("da", 29)
print(li+wang)
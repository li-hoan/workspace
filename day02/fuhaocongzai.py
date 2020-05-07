class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __add__(self, other):
        return self.age + other.age

zhang = person("z",321)
li = person("l", 452)
print(zhang + li)
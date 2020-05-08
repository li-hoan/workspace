class person:
    def __init__(self, name):
        self.name = name
        self.height = 1.75
        self.sex = "m"
    def show(self):
        print(self.name)
        print(self.height)
        print(self.sex)

p = person("xiaoming")
p.show()
#继承
class f(person):
    def __init__(self, name):
        super().__init__(name)

l = f("lili")
l.show()
#组合
class man:
    def __init__(self, person):
        self.person = person
    def show(self):
        print(self.person.sex)
p = person("xiaommei")
s = man(p)
s.show()
class person:
    def __init__(self, name, sex, height):
        self.name = name
        self.sex = sex
        self.height = height

    def show(self):
        print(self.name)
        print(self.sex)
        print(self.height)


# p = person("haha","nv",1.99)
# p.show()
class fmale(person):
    def __init__(self, name, sex, height):
        super().__init__(name, sex, height)

# liang = fmale("xiaohong","nv",1.78)
# liang.show()

class man:
    def __init__(self,ren):
        self.ren = ren
    def show(self):
        print(self.ren.name)

p = person("xiaohei","nv",1.66)
l = man(p)
l.show()
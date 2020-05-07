class person:
    def __init__(self, name):
        self.name = name
        self.height = 1.72
        self.sex = "man"

    def show(self):
        print(self.name)
        print(self.height)
        print(self.sex)

p = person("zhang")
p.show()

p.height = 1.77
p.show()
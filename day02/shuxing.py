class person:
    def __init__(self, name):
        self.name = name
        self.height = 1.73
        self.sex = "nan"

    def show(self):
        print(self.name)
        print(self.height)
        print(self.sex)

p = person("zhang")
p.show()
p.height = 1.88
p.show()
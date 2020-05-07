class animal:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(self.name)

class cat(animal):
    def __init__(self, name):
        super().__init__(name)

cat1 = cat("dabai")
cat1.show()

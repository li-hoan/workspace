class person:
    def say(self,content):
        print(content)

p = person()
p.say("haah")

class cat:
    def get(self, obj):
        return obj

cat1 = cat()
print(cat1.get("miaomiao"))

class bird:
    def __init__(self):
        print("rensena")

b = bird()

class dog:
    def __call__(self):
        print("wangwang")

d = dog()
d()
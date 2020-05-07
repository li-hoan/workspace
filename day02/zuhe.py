class Eye:
    def __init__(self, color):
        self.color = color

class per:
    def __init__(self, eye):
        self.eye = eye

    def show(self):
        print(self.eye.color)

eye = Eye("black")
p = per(eye)
p.show()
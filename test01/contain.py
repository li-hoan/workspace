class Eye:
    def __init__(self, color):
        self.color = color

class face:

    def __init__(self, eye):
        self.eye = eye

    def show(self):
        print(self.eye.color)

eye = Eye("hei")
p = face(eye)
p.show()
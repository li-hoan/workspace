class person:
    def __call__(self):
        print("yingyongcall")

p = person()
p()
p.__call__()
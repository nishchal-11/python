class something:
    a=1
    @classmethod
    def call(cls):
        print(f"the value of class attribute {cls.a}")

e=something()
e.a=2
e.call()

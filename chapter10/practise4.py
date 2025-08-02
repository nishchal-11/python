class calculator:

    def  __init__(self,n):
        self.n=n

    def square(self):
        print(f"sqaure is {self.n*self.n}")

    def cube(self):
        print(f"sqaure is {self.n*self.n*self.n}")

    def squareroot(self):
        print(f"sqaure is {self.n**1/2}")

    @staticmethod
    def some():# dont need slef
        print("hello bhai sab")

p=calculator(4)
p.square()
p.cube()
p.squareroot()
p.some()
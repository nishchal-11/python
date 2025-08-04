class something:
    a=1
    @classmethod
    def call(cls):
        print(f"the value of class attribute {cls.a}")


    @property 
    def name(self):
        return f"{self.fname}{self.lname}"
    
    @name.setter
    def name(self,value):
        self.fname=value.split(" ")[0]
        self.lname=value.split(" ")[1]


e=something()
e.a=2
e.name="nishchal p"
print(e.fname,e.lname)

e.call()

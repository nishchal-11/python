class Employee:
    language="python"
    salary=120000

    def getInfo(self): # see getInfo is the instance of an class 
        print(f"the language is {self.language}. The salary is {self.salary}")
    @ staticmethod # if it is given as static method then u dont need to call slef
    def greet(self): # the slef u hace written can be removed if u use @static method
        print("good morning")
        #when th program creates the objects on the class is called instance

harry=Employee() # here harry is an object of employee class 
harry.language="Java script"# this is object or "instance" attribute
print(harry.language)

harry.getInfo()

Employee.getInfo(harry)

harry.greet()

nishchal=Employee()
nishchal.greet()

# self refres to the instance of the class .it is automatically passes with a function call from an object 

# @static method is called decorator (idk what is this lets study this later)

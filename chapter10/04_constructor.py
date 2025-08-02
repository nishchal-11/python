class Employee:
    language="python"
    salary=120000

    def __init__ (self,name,salary,language): # dunder method which is automatically called
        self.name=name
        self.salary=salary
        self.language=language
        print("i am creating an object")

    def getInfo(self):  
        print(f"the language is {self.language}. The salary is {self.salary}")
    
    @staticmethod 
    def greet(self): 
        print("good morning")
        

harry=Employee("nishchal",1200000,"java")
# harry.language="Java script"
print(harry.name,harry.salary,harry.language)

#nishchal=Employee() # again dunder method is automatically called  , when the object is created



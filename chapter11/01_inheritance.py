class Employee:
    company="ITC"
    def show(self):
        print("the name is {self.name} and the salary is {self.salary}")


# class Programmer:
#     company="ITC Infotech"
#     def show(self):
#         print("the name is {self.name} and the salary is {self.salary}")

#     def showLanguage(self):
#         print("the name is {self.name} and he is good with {self.language}")



class Programmer(Employee):
    company= "ITC Infotech"
    def showLanguage(self):
        print(f"the name is {self.name} and he is good with {self.language}")



a=Employee()
b=Programmer()
print(a.company)
print(b.company)
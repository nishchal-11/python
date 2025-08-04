class Employee:
    company="ITC"
    name="Default name"
    def show(self):
        print(f"the name is {self.name} and the salary is {self.language}")


class Coder:
    language="python"
    def printLanguages(self):
        print(f"out of all languge this is urs {self.language}")

class Programmer(Employee,Coder):
    company= "ITC Infotech"
    def showLanguage(self):
        print(f"the name is {self.company} and he is good with {self.language}")



a=Employee()
b=Programmer()
b.show()
b.printLanguages()
b.showLanguage()
print(a.company)
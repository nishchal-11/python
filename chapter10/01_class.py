class Employee:
    name="harry" # this is class attribute
    language="python"
    salary=120000

harry=Employee()
harry.name="Harry"# this is object or "instance" attribute
print(harry.salary,harry.language,harry.name)

nishchal=Employee()
nishchal.name="Chintu"
print(nishchal.salary,nishchal.name)
#  here name (nishchal.name and harry.name) is objects attributes and salary and language is class attributes
class programmer:
    company="Microsoft"
    def __init__ (self,name,salary,pincode):
        self.name=name
        self.salary=salary
        self.pincode=pincode
    
p=programmer("harry",120000,563401)
print(p.name,p.salary,p.pincode)
p=programmer("nishchal",120000,563201)
print(p.name,p.salary,p.pincode)
p=programmer("soham",120000,563104)
print(p.name,p.salary,p.pincode)

class demo:
    a=4

o=demo()
print(o.a)# printing class attribute bcoz instance attribute is not still created 
o.a=0
print(o.a) # now printing instance attribute
print(demo.a) # from this u can undertsmd class attribute is not chnaged but th einstance attribute is changed

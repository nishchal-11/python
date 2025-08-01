a1=int(input("enter no"))
a2=int(input("enter no"))
a3=int(input("enter no"))
a4=int(input("enter no"))

if( a1>a2 and a1>a3 and a1>a4):
    print("a1 is greater",a1)
elif( a2>a1 and a2>a3 and a2>a4):
    print("a2 is greater",a2)
elif( a3>a2 and a3>a1 and a3>a4):
    print("a3is greater",a3)
elif( a4>a1 and a4>a3 and a4>a2):
    print("a4 is greater",a4)
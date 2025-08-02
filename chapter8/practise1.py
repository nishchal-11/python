def greatest():
    a=int(input("enter"))
    b=int(input("enter"))
    c=int(input("enter"))

    if ( a>b and a>c):
        print(a)
    elif ( b>a and b>c):
        print(b)
    elif ( c>a and c>b):
        print(c)
    
greatest()
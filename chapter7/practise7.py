n=int(input("enter n"))
for i in range(1,n+1):
    print(" "*(n-i),end="") # if we writ end="" this doesnt autoimatically give new line,bcoz print automatically gives new lines
    print("*"*(2*i-1),end="")
    print("\n")

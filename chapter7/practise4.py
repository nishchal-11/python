n=int(input("enter n"))
for i in range(2,n):
    if n%i == 0:
        print('not a prime')
        break
else: # remembered else can also be used in after for loops
    print("prime")
        
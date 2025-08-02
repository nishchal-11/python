def factorial(n):
    if(n==1 or n==0):
        return 1
    return n * factorial(n-1)

n=int(int(input("enter a number")))
print(f"the factorial of {n} is {factorial(n)}")
#  programmers need to be careful while adding recursion bcoz the function will go in infinite loop infinite loop if we dont add base condition
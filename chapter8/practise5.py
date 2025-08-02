def pattern(n):
    if (n==0):
        return # if only this is return then the function ends khatam tata bye bye
    print("*"*n)
    pattern(n-1)

print(pattern(3))
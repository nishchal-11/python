def rem(l,word):
    n=[]
    for item in l:
        if not(item==word):
            n.append(item.strip(word))
    
    return n
l=["harry","rohan","sohan","an"]
print(rem(l,"an"))
# seriously even i dont know what this mmeans
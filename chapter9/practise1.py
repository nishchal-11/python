f= open("poems.txt")
content=f.read()
if("twinkle" in content):
    print("yes it is present")
else:
    print("not present in the contnet")
f.close()
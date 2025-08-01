marks={
    "harry":57,
    "shubam":99,
    0:"nishchal"
}
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"harry":90})# its mutable fuking geeks
print(marks.items())
marks.update({"renuka":100})
print(marks.items())

# the differnc ebetween this two is if the key does present the first ine gives none but the one with square barckets gives error 
print(marks.get("harry"))# print noone
print(marks["harry"]) # returns error


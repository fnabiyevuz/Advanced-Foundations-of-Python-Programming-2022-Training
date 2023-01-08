names = ["Ali", "Vali", "G'ani"]

new_enum = enumerate(names)
print(new_enum.__next__())
print(new_enum.__next__())
print(new_enum.__next__())

print(type(new_enum))
print(list(new_enum))

for index, name in enumerate(names):
    print(index, name)


# enumerate function
# enumerate(iterable, start=0)
l1 = ["eat", "sleep", "repeat"]
s1 = "geek"

# creating enumerate objects
obj1 = enumerate(l1)
obj2 = enumerate(s1)

print ("Return type:", type(obj1))
print (list(enumerate(l1)))

# changing start index to 2 from 0
print (list(enumerate(s1, 2)))

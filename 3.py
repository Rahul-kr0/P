# How to use List
# 

simpleList = ["red", "green", "blue", 4, 5, 6]
# [] brackets used for list. Since lists are changable
# () brackets used for tuples. Tuples are immutable or unchangable

print(simpleList) 
print(type(simpleList))

# print any strr or number by index number of list
print("Simplelist[1] = ", simpleList[1]) 

# print any strr or number in between list by index number
print("SimpleList[0:3] = ", simpleList[0:3])

# print after any index number
print("SimpleList[3:] = ", simpleList[3:])

# change any value in list
# tuples are not changable 
simpleList[2] = 3
print("changed value ", simpleList)

# to get last value of list
print("SimpleList[-1] = ", simpleList[-1])

# to add new value in list
# Tuple will not insert any value
simpleList.insert(6,"new value")
# 6 is a index number where u want to have new value.
print("New item added to list ", simpleList)

# to remove value in list
# Tuple will not remove any value
simpleList.remove("new value")
print("one item remove in a list ", simpleList)

# to remove value by index number
simpleList.pop(2)
print("Removed item by index number ", simpleList)

# loop in a list
# loop will work on tuple
for x in simpleList:
    print(x)

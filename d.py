# Set used in Python 
# Set is a collection of unordered, unchangable and unique item.
# No duplicate values will allowed in a set
simpleSet ={4,5,6,7,8,9}
print(type(simpleSet))
print(simpleSet)

# we can run loop on set
for x in simpleSet:
    print(x)

# we can add or remove values in a set
simpleSet.add(10)
print(simpleSet)

simpleSet.remove(10)
print(simpleSet)

# set can be used for mathematic set operations
# union
setA = {1,2,3,4,5,6}
setB = {4,5,6,7,8,9}
print(setA.union(setB))

# intersaction
print(setA.intersection(setB))

# difference
print(setA.difference(setB))

#Symmetric  difference
print(setA.symmetric_difference(setB))
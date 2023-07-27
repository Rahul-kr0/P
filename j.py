# function in python

def add(a,b):
    sum = a+b
    sub = a-b
    return sum,sub

result1,result2 = add(4,5)
print(result1 ,result2)


# in python there is no pass by value or pass by reference concept

def update(x):
# before changing value of x, 
# it will pass as call by value as it has same location id
    print(id(x))

    x = 8
# but after changing value of x, 
# it will pass as call by reference as it has new location id
    print(id(x))
    print("x ", x)

a = 10
print(id(a))
update(a)


# but list is changable or mutable means it will change the original value also

def update(x):
# before changing value of x, 
# it will pass as call by value as it has same location id
    print(id(x))

    x[3] = 8
# but after changing value of x, 
# it will pass as call by reference as it has new location id
    print(id(x))
    print("x  ", x)

a = [2,4,5,6,7]
print(id(a))
update(a)
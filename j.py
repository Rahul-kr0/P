from array import *

# function in python


def add(a, b):  # a and b are formal argument
    sum = a + b
    sub = a - b
    return sum, sub


result1, result2 = add(4, 5)  # whereas 4 and 5 are Actual argument
print(result1, result2)


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
    print("x ", x)


a = [2, 4, 5, 6, 7]
print(id(a))
update(a)


# Argument in function

def person(name,age=18):
# if the age do not get the value, it will pass default value is 18
    print(name)
    print(age)

person('rahul',22)


# variable length is used when actual argument is not fixed

def sum(*b):
    print(b)
# *b is used as tuple to store more than one value
    c = 0
    for i in b:
        c = c + i
    print(c)
sum(5,6,8,9)


# Keword variable length argument in this a value is passed in the form of key:value

def person(name, **data):
    print(name)
    for i,j in data.items():
        print(i,j)

person('rahul',age=22,city='Ranchi', mob=43375745)

# using local variable as global variable
a = 10
def something():
    global a
    a = 15
    print("fun ", a)
something()

print("outside", a)

# global and local variable in same function
b = 10
def something():
    b = 9

    x = globals()['b']
    print("new fun ", b)

    globals()['b'] = 15

something()

print("new outside", b)


# function in an array


arr = array('i',[])

print("Enter 10 numbers you want in a array : ")

for i in range(10):
    x = int(input("Enter your numbers : "))
    arrname = arr.append(x)


print(arrname)
# initialize array
from array import *

# arrname = array ('datatype', [3,5,6,7])
arrname = array('i', [5, 6, -7, 8, 9])

# to copy array
# arrname = array(arname.typecopde, (a for a in arrname))
newarr = array(arrname.typecode, (a for a in arrname))

for i in newarr:
    print(i)

# take input from user

arrname = array('i', [])

n = int(input(" Enter length of an array : "))

for i in range(n):
    x = int(input("Enter next number : "))
    arrname.append(x)

print(arrname)

# long method to search element in an array

s = int(input("Enter a number to search in an array : "))
k = 0
for i in arrname:
    if i == s:
        print(k)
        break
    k += 1

# short method to search element in an array
print(arrname.index(s))


# To reverse an array

vals = array('i',[7,4,6,7,8,9])
vals.reverse()
print(vals)


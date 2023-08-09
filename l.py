# use multi dimension array
# import numpy
from numpy import *

arr = array([2,5,6,1,4,3])
print(arr)

# two dimensional array

arr1 = array([
               [1,2,3],
               [4,5,6]
            ])

print(arr1)
# to get the rows and coloumn
print(arr1.shape)
# to convert 2d array in 1d array
# arr2 = arr1.flatten()
# to get the size of an array
print(arr1.size)
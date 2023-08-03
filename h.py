# loop example in python
print("normal example")
color = ["Red", "Green", "blue"]
for x in color:
    print(x)

# break is used to stop the program
print("break statement")
color = ["Red", "Green", "blue "]
for x in color:
    break
    print(x)

# continue in python program
# used to skip value or string
a,b = 1,100
for i in range(a,b):
    if (i % 2) != 0:
        continue
    print(i)
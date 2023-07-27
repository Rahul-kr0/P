# Mapping Type: Dictionary(dict)
# Dictonaries are used to store data values in key:value pairs.

person = {
    "name": "Rahul Kumar",
    "age": 22,
    "location": "Ranchi"
}
print(type(person))
print(type(person["name"]))
print(type(person["age"]))

# get values in the dictionary by key
print(person["name"])

# we can check key exist ina dictionary or not
print("name" in person)

# change the value of dictionary
person["age"] = 23
print(person["age"]) 

person.update({"age":22})
print(person["age"])

# adding value of a dictionary
person["Blood_group"] = "A+"
print(person)

person.update({"hair_color": "black"})
print(person)

# delete particular key from dictionary
person.pop("hair_color")
print(person)

# delete last item from directory
person.popitem()
print(person)

# delete particular key from dictionary using del keyword
del person["age"]
print(person)

# empty directory using clear method
person.clear()
print(person)

person = {
    "name": "Rahul Kumar",
    "age":  22,
    "location": "Ranchi"
}
print(person)
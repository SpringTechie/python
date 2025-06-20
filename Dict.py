person = {
    "id":1, 
    "name":"arun", 
    "age":23,
    "lucky_number":56,
    "hobbies": ["listeing music","playing chess"],
    "exp": {
        "wipro": 2,
        "TCS": 3
    }

}

# to copy from one dic to another
# person2 = person.copy() 
# 2nd way to copy
# person2 = dict(person)
# print(person2)
# person["country"] = "india" # adding country key is not present inside a person dic
# person["name"] = "pavan"  # if the key is present means updating the dic.
# print(person)

# person.update({"x":"arun kumar"})
# print(person)

# print(person.pop("name")) # this removes the name entry from dict and returns removed value.
# print(person.popitem())
# person.clear()
# del person
# print(person) 





#object = dict(product_name="pen",price=23.7)

# print(type(object))
# print(len(object))
# print(object)

# print(person['name'])
# print(person.get("age"))
# keys = person.keys()
# print(keys)
# print(person.values())

# print(person.items()) # this returns tuple of each entry


# print("name" in person)
# loop
# for key in person:
#     print(key,":", person.get(key))

# for value in person.values():
#     print(value)


# for key,value in person.items():
#     print(key,"=",value)









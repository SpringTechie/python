# s = {"raja","pawan","raja","arun",1,True,False,0}
# print(type(s))
# print(len(s)) # 3

# t = set(("apple","banana"))
# print(type(t))
#removing duplicates

# we can add new elements to set object
# s.add(34)

# s1 = {2,3,4,5}
# s.update(s1)
# s.remove("pawan") # if specifed element is not present inside a set then it throws keyError.
# s.discard("charan") # if specifed element is not present inside a set then it wont throws keyError.
# s.pop() # by this method we can remove some random value or element.
# s.clear() : complete values are removed.
# del s : it deletes the entire set object from memory.


s1 = {7,8,9,0}
s2 = {3,4,0,6}
# print(s1.union(s2))
print(s1.intersection_update(s2))
print(s1)

ss = {"a"}
print(type(ss))






# l = [] # empty list
# list1 = [1,2,3,4,5] # with values.
# list2= [1,"ar",1.8,'c'] # with diff type values.
# print(list2)
# print(len(list2))
# print(type(list2))

# ll = list(("arun","pawan"))
# to access the list values based on index.
# print(list1[0])
# # negative index
# print(list1[-1])

l = [5,3,4,12,34,56]
# range(starting_value,ending_value,step): if we dont speicify the step value bydefaut range function increments value by 1

# for i in range(0,len(l)): # 0 to 6(exlcuded)
#     print(l[i])
# i = 0
# while(i<len(l)):
#     print(l[i])
#     i=i+1

# for i in range(0,100,2):
#     print(i)
#l = [5,3,4,12,34,56]
#   -6 -5-4-3 -2 -1
# slicing
# print(l[2:5]) 
# print(l[2:]) 
# print(l[:5])
# print(l[:]) 
# print(l[-5:-1]) # forward direction
# print(l[-2:-5:-1]) # backword direction
# slicing : [start:stop:direction] = if we dont provide any value for direction then it consider or slice in forward direction , if we provide direction = -1 then it consider the backword direction

# l[2]= 34 # to replace a single value.
# l[2:4]= [66,77] # to replace a range of values.
# if we want to add new element at specified index , and the old element should not be replaced.
# l.insert(2,88)
# to add new value to existing list
#l.append(6)
# to concat two list

#print(l)

# l1 = [1,2,3]
# l2 = [4,5,6]
# # l1+l2
# l1.extend(l2) # add at the end
# l1.append(l2) # appends the list at the end of list as single value.
# print(l1)


# List comprehesion used to shorter the syntax to create list object.
# syntax: l = [expression for item in iterable if condition == True]

# ll = [1,2,3,4,5,6]

# even_list = [x for x in range(0,100) if(x%2==1)]
# print(even_list)

# by usinng list compreshion 

# ll = [int(x) for x in input("Enter a number").split()]
# #ll.sort() # ascending order
# # to sort reverse
# ll.sort(reverse=True)
# print(ll)

ll = [1,2,3,4]
print(ll[10])










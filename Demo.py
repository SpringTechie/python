# max number inside list
# l = [2,80,10,6,110,5]

# max_num = l[0] # 2

# for x in l: # [2,80,1,6,110,5]
#     # x = 5
#     if(x>max_num): # 5>110
#         max_num = x # max_num = 110

# print(max_num)

# Reverse a list
# l = [2,80,10,6,110,5]
# output = [5,110,6,10,80,2]


# rev_list = []
# for i in range(len(l)-1,-1,-1):
#     rev_list.append(l[i]) # rev_list[0] = l[5]

# print(rev_list)
# 2nd way to reverse a list
# print(l[::-1])

# count of each number inside a list
# l =[2,3,4,5,1,2,3,6,7,8,4,4,5,5,5,90,4]
# num_count = {2:2,3:2,4:4,5:4,1:1,6:1,7:1,8:1,90:1}
# key = a number inside list
# value = correspoding number count
# l =[2,3,4,5,1,2,3,6,7,8,4,4,5,5,5,90,4]
# num_count = {}

# for x in l:
#     if(x in num_count):
#         count = num_count.get(x) # 3
#         num_count.update({x:count+1}) 
#     else:
#         num_count.update({x:1}) # {2:2,3: 1,4:4,5:1,1:1}
# print(num_count)


# remove duplicates
# l = [1,2,3,2,3,4,5,6,7,8,9]
# dr = [1,2,3,4,5,6,7,8,9]

# l = [1,2,3,2,3,4,5,6,7,8,9]
# dr = []

# for x in l:
#     if(x not in dr):
#         dr.append(x)

# print(dr)
# 2nd way to remove duplicates
# dr = set(l)
# print(dr)
        
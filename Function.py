# def add(a,b):
#     c = a+b
#     return c

# result = add(2,3)
# print(result)
# Arbitary Arguments *args:
# def add(*args):
#     print(type(args))
#     print(args[0])
#     print(args[1])
#     print(args)

# add(2,3)
# keyword Arguments

# def add(a,b,c):
#     print(a+b+c)

# add(b=2,a=3,c=45)


# def prepareFullName(**keys):
#     fullname = keys["firstname"] + keys["lastname"] + keys.get("middlename")
#     print(fullname)

# prepareFullName(firstname = "raja",lastname= "mamini",middlename = "arun")

# def function(country= "USA"):
#     print("my country==",country)

# function("india")
# function()

# def printList(items):
#     for x in items:
#         print(x)

# printList(["pen","ball"])


# def myFunc(x):
#     return x.upper()
# print(myFunc("arun"))


# def myFunc():
#     pass

# recursion: A method calling itself

def myFunc(x):
      global y
      y = 2
      
    
      if(x<10):
        myFunc(x+1)

myFunc(1)
print(y)




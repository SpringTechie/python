# t = ("apple",)
# tt = tuple(t)
# print(type(tt)) # (a','a')
# print(tt)
# print(tt[100])

# t = ("apple","banana")
# print(t[0])

# t = (1,2,3,45)
# l = list(t)
# l.append(34)
# t = tuple(l)
# print(t)

# unpacking
t=(1,2,3,45,60,3)
(odd,even,*remain) = t
# print(remain)

# print(t.index(600)) # index(60)
# print(t[200])

print(t.count(3))






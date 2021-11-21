#string--->imutable(can't change in s ....change save in different variable)

s = "vermaNidhi"
t = s.title()
print(t)
print(s)

#List--->mutable(can change in orignal list)

l = ['world1','world2','world3']
l.pop()
print(l)
l.append("word3")
print(l)
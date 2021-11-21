string = "She is beautiful and she is good dancer"
print(string.find("is")) #s1,h2,e3,space4
string1 = "is She is beautiful and she is good dancer"
print(string1.find("is",1)) # second "is" on 7th place

#7+1=8 because 0n place of 7 and 8 "is" avlaible next on 28

is_pos1 = string.find("is")
is_pos2 = string.find("is",is_pos1+1) #second is position in string
print(is_pos2)




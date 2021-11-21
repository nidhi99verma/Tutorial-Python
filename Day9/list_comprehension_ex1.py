#turn all items in -ve
#list comprehension

new_negative = [-i  for i in range(1,11)]
print(new_negative)

#simple way

negative = []
for i in range(1,11):
    negative.append(-i)
print(negative)    
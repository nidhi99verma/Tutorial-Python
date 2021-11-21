#seprate even numbers
#simple way

numbers = list(range(1,11))
nums = []
for i in numbers:
    if i%2 == 0:
        nums.append(i)
print(nums)

#with comprehension   [append part  for loop part   if statement part]

even_nums = [i  for i in numbers if i%2 == 0]
print(even_nums)

#or

even_nums = [i  for i in range(1,11) if i%2 == 0]
print(even_nums)

#odd numbers

odd_nums = [i  for i in range(1,11) if i%2 != 0]
print(odd_nums)




# Define a function that list of numbers as argument and return two list even and odd number list:
def filter_oddeven(l):
    odd_nums = []
    even_nums = []
    for i in l:
       if i%2 == 0:
           even_nums.append(i)
       else:
           odd_nums.append(i)
    output = [even_nums,odd_nums]
    return output
nums = [1,2,3,4,5,6,7,8,9,10]
print(filter_oddeven(nums))               
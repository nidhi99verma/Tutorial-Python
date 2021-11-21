#key value pair of number and it's cube of numbers
# simple way

def cub_finder(n):
    cubes = {}
    for i in range(1,n+1):
        cubes[i] = i**3
    return cubes
print(cub_finder(10))        

#comprehension way {conditipn for key value pair    for loop}

cub = {num:num**3   for num in range(1,11)}
print(cub)
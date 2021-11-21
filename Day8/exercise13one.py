#define a function that takes a number(n) return a dictionary containg cub of nembers from 1 to n
def cub_finder(n):
    cubes = {}               #dict
    for i in range (1,n+1):
        cubes[i] = i**3      #dict
    return cubes
print(cub_finder(10))        

#define a function which will take list containing numbers as input and return list containing square of every elements:
def square_list(l):
    square = []
    for i in l :
       square.append(i**2)
    return square
numbers = list(range(1,11))
print(square_list(numbers))       
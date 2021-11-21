import pdb                               #import for debugging

pdb.set_trace()                          #we can write any where but before those line who genrate error
name = input('Please type your name : ')
age = input('Please type your age : ')
print(f'hello {name} your age is {age}')
age2 = int(age) + 5                      #age = age + 5
print(f'{name} your will be {age2} in next five years')

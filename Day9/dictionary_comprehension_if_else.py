#make a dictionary of number as key and value in print even or odd
#{key  : value in if else condition   for loop}
odd_even = {i : ('even' if (i%2==0)  else 'odd') for i in range(1,11)}
print(odd_even)
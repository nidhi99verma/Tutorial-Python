"""define a function that take list of string and in output give reverse of string in list
use list comprehension"""
#list comprehension

def reverse_string(l):
    return[name[::-1]   for name in l] 
print(reverse_string(['abc','tuv','xyz']))
    
#simple way

def reverse_elements(l):
    elements = []
    for i in l:
        elements.append(i[::-1])
    return elements
words = ['abc','tuv','xyz']
print(reverse_elements(words))            
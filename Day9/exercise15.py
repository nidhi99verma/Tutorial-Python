#define a function which change list items in present int or float into string

def num_to_string(l):
    return[str(i)   for i in l  if type(i) == int or type(i) == float]
print(num_to_string([True,False,1,1.0,3]))    
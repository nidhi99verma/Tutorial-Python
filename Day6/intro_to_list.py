numbers = [1,2,3,4,5,6]                            #list of number
print(numbers)
print(numbers[1])
words = ["word1","word2","word3","word4","word5"]  #list of string
print(words[:2])
mixed = [1,2,3,"five","two",2.0,None]              #list of mixed datatype
print(mixed)
print(mixed[-1]) 
mixed[1] = "two"                                   #change  one element
print(mixed)
mixed[1:] = "three"
print(mixed)
mixed[1:] = ["four","five"]                        #change more then one element
print(mixed)
mixed[1] = ["N","V"]
print(mixed)

#define a function which will take list as a argument and this function will return a reversed list:
#(1)
print(".............using reverse function............")
def revers_list(l):
    l.reverse()                     #return l.reverse()
    return l
numbers = [1,2,3,4,5]
print(revers_list(numbers))   

#(2)
print("..............using [::-1]......................")

def revers_list(l): 
    return l[::-1]
numbers = [1,2,3,4,5]
print(revers_list(numbers))   


#(3)
print("...............using for loop....................")

def revers_list(l): 
    revers_list = []
    for i in range(1,len(l)+1):                #range(len(l))
        popped_item = l.pop()
        revers_list.append(popped_item)
    return revers_list    
numbers = [1,2,3,4,5]
print(revers_list(numbers))   




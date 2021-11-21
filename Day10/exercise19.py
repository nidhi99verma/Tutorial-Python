#define a function take any no of list containg number [1,2,3],[4,5,6],[7,8,9]return average same index
#ex(1+4+7)/3,---,*try to make this anonymos function in one line using lambda

#if we do this with only two list 
def avg_finder(l1,l2):
    avg =[]
    for pair in zip(l1,l2):
        avg.append(  sum(pair)/len(pair))
    return avg
print(avg_finder([1,2,3],[4,5,6]))
        
# ......more then two lists....
print("----------------------")

def avg_finders(*args):
    avg = []
    for pair in zip(*args):
        avg.append(sum(pair)/len(pair))
    return avg
print(avg_finders([1,2,3],[4,5,6],[7,8,9]))    

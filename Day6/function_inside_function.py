# pro for find greatest number between 3 number using two function

def greater (a,b):     # 1 function for 2 no
   if a>b :
     return a
   return b

def greatest (a,b,c):   # 2 function for 3 no
   if a>b and a>c:
       return a
   elif b>a and b>c:
        return b
   else:
         return c
# using 1 function two time and work like 2 function
def new_greatest(a,b,c):
   bigger = greater(a,b)
   return greater(bigger,c)     # return greater(greater(a,b),c)
print(new_greatest(99,9,999))   
        
           
matrix = [[1,2,3],[4,5,6],[7,8,9]]  #2D array
print(matrix[0])
print("-----------")
for i in matrix:
    print(i)
print("-----------")    
for sublist in matrix:   #loop 1bar chalega...phr 3 bar
    for i in sublist:    #loop 3bar chalega...phr 3 bar
        print(i)
print("-----------")         
print(matrix[1][1])      #get element by index      
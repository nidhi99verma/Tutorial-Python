f = open("file1.txt")   
                     #r for read and defalt set read and w for write
print(f'cursor position - {f.tell()}')
print(f.tell())

print(f.read())
print(f'cursor position - {f.tell()}')       #f.tell() we can use this too
print("Before seek method")
f.seek(0)       
                             #seek() set cursor position
print("After seek method")
print(f'cursor position - {f.tell()}')
#print(f.read())                              #already read this file so cursor set in last in file

print("below readline method")
print(f.readline())
print(f.readline())
print(f.readline(),end="")                    #end remove empty line
print(f.readline())

print("below readlines method")
f.seek(0)
lines = f.readlines()
print(lines)
print(len(lines))
for line in lines:
    print(line,end="")

print("-----")

print(f.name)
print(f.closed)

f.close()

print(f.closed)                       #true

f = open(r"F:\testpy.txt")            #we can open txt file which is in different drive

for line in f:                        #we can use without readlines or readline method
    print(line,end="")

for line in f.readlines()[:2]:        #for slicing
    print(line,end="")    

#with block in no need to close file(context manager)

with open('file2.txt') as f:
    data = f.read()
    print(data)

print(f.closed)                       #automatically close  
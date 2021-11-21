# Common elements find function , define a function which takes 2 lists as input & return a list which contain common elements of both lists:
def common_finder(l1,l2):
    output = []
    for i in l1:
        if i in l2:
            output.append(i)
    return output
print(common_finder([1,2,3,4,5,6],[1,0,2,9,3,8]))            
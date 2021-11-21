import os
#os.getcwd()                              #currebt working directry                                #1  

#os.chdir(r"F:\CV")                       #change working directory               
     
#print(os.getcwd())                                                                                #2
#os.mkdir("test")                                                                                  #3

#print(os.path.exists('test'))            #check folder exist or not                               #4
# if os.path.exists('test'):                                                                       #5
#     print('alredy exist')
# else:
#      os.mkdir("test")   

#open('file.txt','a').close()               #does't throw error and not make duplecat               #6
#os.mkdir(r'F:\CV\just_test')               #in diffrent dir

#print(os.listdir())                        # check folders in dir
#print(os.listdir(r'F:\CV'))                # check folders in different dir

# for item in os.listdir():                 # get path of given dir (this is not right way because in mac or linux \\ not work_)
#     print(r'G:\Python\Day14\OS_Module'+'\\'+item)

# for item in os.listdir():                   # work on all os
#     path = os.path.join(os.getcwd(),item)
#     print(path)

for item in os.listdir(r'F:\CV'):             # in diff dir
    path = os.path.join(r'F:\CV',item)
    print(path)




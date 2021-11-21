import os
import shutil    # use to delet folder which is not empaty

os.chdir(r'G:\Python\Day14\OS_Module_Shutil_module')
#print(os.listdir())

file_iter = os.walk(r'G:\Python\Day14\OS_Module_Shutil_module')                 #for folder in files path
for current_path, folder_names, file_names in file_iter:
    print(f'Current Path : {current_path}')
    print(f'Folder Names : {folder_names}')
    print(f'File Names : {file_names}')

#os.rmdir('Delet_folder')     # delet only empaty folder                              
#directory and folder is same things
 
#os.makedirs('new/movies')   #create folder inside folder

#shutil.rmtree('new')     # parmanentally delet not avlable  in recycle bin

# shutil.copytree('new','G:\Python\Day14\OS_Module_Shutil_module/new_new')   # new :copyfolder , place where u want to paste(and rename origenal dolder)

# shutil.copytree('new.txt','G:\Python\Day14\OS_Module_Shutil_module/new_ew.txt')  # same with folder

# shutil.move('file.txt','new/file2.txt')   # move file (cut : paste)

# shutil.move('file','new/new_file')   # move folder (cut : paste)

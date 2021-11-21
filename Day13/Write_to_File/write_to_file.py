with open('file3.txt','w') as f:       #we can write any thing in place of f 
        f.write("hello")
with open('file3.txt','a') as f:       #append method     
    f.write(' append more data ')
    f.write(' \n again append more data ')
    f.write(' 1 again append more data \n')
    f.write(' 2 again append more data ')

print("if file not present then created by with same with 'a' and 'w'")  

with open('file4.txt','w') as f:        
        f.write("hello")

# r+ override files data frpom start...ex: hello there \n subscribe to my channel--- in change ----please do it

with open('file5.txt','r+') as f:             # r+ file can't create file it self like append and write function
        f.write("please do it")               # use this to create file by terminal-   echo -e "hello there \n subscribe to my channel" >> file5.txt


#if u want to add data in last like append by r+ function then

with open('file6.txt','r+') as f:  
        f.seek(len(f.read()))                 #seek & len fun use to set cursor in last 
        f.write(" add by r+ ")
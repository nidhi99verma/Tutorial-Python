user_info = {
    'name' : 'Nidhi',
    'age' : 25,
    'fav_movies' : ['coco','kimi no na wa'],
    'fav_tunes'  : ['awakening','fairy tale']
}
for key,value in user_info.items():                   #u can take any name in place of key and value
    print(f"key is {key} and value is {value}")       
print("--------------------------------------")  
for i in user_info.items():
    print(i)
print(type(i))             #type tupel 

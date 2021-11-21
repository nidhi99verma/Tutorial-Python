user_info = {
    'name' : 'Nidhi',
    'age' : 25,
    'fav_movies' : ['coco','kimi no na wa'],
    'fav_tunes'  : ['awakening','fairy tale']
}
pop_items = user_info.popitem()   # popitmes randomly delet any one pair of key values 
print(user_info)
print(pop_items)
print(type(pop_items))            #tuples
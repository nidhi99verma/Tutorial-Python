user_info = {
    'name' : 'Nidhi',
    'age' : 25,
    'fav_movies' : ['coco','kimi no na wa'],
    'fav_tunes'  : ['awakening','fairy tale']
}
if 'name' in user_info:        #check key
    print('present')
else:
    print('not present')
if 25 in user_info.values():  #check value
    print('present')
else:
    print('not present')
    
    

user_info = {
    'name' : 'Nidhi',
    'age' : 25,
    'fav_movies' : ['coco','kimi no na wa'],
    'fav_tunes'  : ['awakening','fairy tale']
}
pop_items = user_info.pop('fav_tunes')
print(f"poped items is {pop_items}")
print(user_info)
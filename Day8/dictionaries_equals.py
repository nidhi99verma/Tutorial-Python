d = {
    'name' : 'Nidhi',
    'age' : 25,
    'fav_movies' : ['coco','kimi no na wa'],
    'fav_tunes'  : ['awakening','fairy tale']
}
d1 = d
print(d1.popitem())
print(d)
print(d1)
print("----------diff b/w copy and '=' -----------")
d2 = d.copy()
print(d2 is d)               #check memory same or diff
print(d2 == d)               #check key value
d3 = d
print(d3 is d)
print(d3 == d)
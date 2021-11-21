d = {'name':'Nidhi','age':'Unknown'}
print(d.get('name'))
print(d.get('names'))
if 'name' in d:           #one more way---> if d.get('name'):
    print('present')
else:
    print('not present')

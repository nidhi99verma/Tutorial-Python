import json
a = {
    'name': 'max',
    'age': 22,
    'marks': [90,50,80,40],
    'pass': True,
    'obj': {
        'color':('red', 'blue')
    }
}
# print(json.dumps(a))             # dict-->>only set can't sent to json
# print(json.dumps(['1', '2']))    # list
# print(json.dumps(('1', '2')))    # tuple
# print(json.dumps('hello'))       # string
# print(json.dumps(100))           # int
# print(json.dumps(12.9))          # float
# print(json.dumps(False))         # boolean
# print(json.dumps(True))
# print(json.dumps(None))
#
# print(json.dumps(a, indent=4))  #space
# print(json.dumps(a, indent=2, separators=('.', '='))) # replace , & :
# print(json.dumps(a,sort_keys=True))   # shorted in alphabetical order

# with open('Json_Test_file.json', 'w') as fh:
#     fh.write(json.dumps(a, indent=2))

with open('Json_Test_file.json', 'r') as fh:
    # print(fh.read())                          # print(type(fh.read())
    json_str = fh.read()
    json_value = json.loads(json_str)
    print(type(json_value))
    print(json_value['name'])
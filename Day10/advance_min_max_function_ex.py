student = [
 {'name': 'Nidhi','score':90,'age':25},
 {'name': 'Ajai','score':80,'age':30},   
 {'name': 'Verma','score':70,'age':15}   
] #list in dict
print(max(student,key = lambda item: item.get('age'))['name'])#(......get(key))[value]

#dict in dict

students = {
    'Nidhi':{'score':100,'age':25},
    'Ajai':{'score':90,'age':30},
    'Verma':{'score':80,'age':15}
}
print(max(students,key=lambda item: students[item]['score']))# [key][value in value]
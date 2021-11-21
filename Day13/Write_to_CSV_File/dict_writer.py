from csv import DictWriter
with open('file_dict_cvs.csv','w') as f:
    csv_writer = DictWriter(f,fieldnames = ['firstname','lastname','age'])
    csv_writer.writeheader()
    csv_writer.writerow({
        'firstname':'Nidhi',
        'lastname':'Verma',
        'age': 25
    })
    csv_writer.writerow({
        'firstname':'A',
        'lastname':'V',
        'age': 35
    })
    csv_writer.writerows([
        {'firstname':'NIDHI','lastname':'VERMA','age': 26},
        {'firstname':'T','lastname':'V','age': 5}
    ])
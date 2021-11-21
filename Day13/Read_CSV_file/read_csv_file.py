
from csv import reader

with open('filec.csv','r') as f:
    csv_reader = reader(f)
    next(csv_reader)             #itrator(skip first line "header")
    for row in csv_reader:
        print(row)
#delimiter (,,|,*,:,:,+-------anything)        
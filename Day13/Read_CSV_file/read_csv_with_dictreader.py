
from csv import DictReader

with open('filec.csv','r') as f:
    csv_reader = DictReader(f)    #if delimiter change then pass here ex:(f,delimiter ='|')
    for row in csv_reader:
        print(row)
        print(row['name'])
#delimiter (,,|,*,:,:,+-------anything)        
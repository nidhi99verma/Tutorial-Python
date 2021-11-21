from csv import writer
with  open('file_csv_w.CSV','w',newline = '') as f:
    csv_writer = writer(f)
    csv_writer.writerow(['name','country'])
    csv_writer.writerow(['Nidhi','India'])
    csv_writer.writerow(['Ajai','Netherlands'])
    csv_writer.writerows([['name','country'],['Nidhi','India'],['Ajai','Netherlands']])    #writerow's'

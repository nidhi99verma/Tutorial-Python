import mysql.connector #pip install

# conn = mysql.connector.connect(host='localhost', username='root', password='root1210')
conn = mysql.connector.connect(host='localhost', username='root', password='root1210', database='new_database_vs')

#print(conn)
my_cursor = conn.cursor()
# query = "CREATE DATABASE new_database_vs"
# query = "SHOW DATABASES"
# query = "CREATE TABLE students_vs(name VARCHAR(255), age INT)"

# query = "INSERT INTO students_vs(name, age) VALUES(%s, %s)" # placeholder %s other db in use diff
# values = ('Nidhi',24)

# values = [
#     ('Ajai', 31),
#     ('Amit', 29),
#     ('Ravi', 32),
#     ('Asha', 55),
#     ('Om', 60)
# ]
query = "SELECT * FROM students_vs"
my_cursor.execute(query)
# my_cursor.executemany(query, values)  #bulk entry
# my_cursor.execute(query, values)

# for print databases

# for datadase_name in my_cursor:
#     print(datadase_name)
# above 2 line and below 1 line both works same
# print(my_cursor.fetchall())

#for print table in data

# for row in my_cursor:
#     print(row)
# above 2 line and below 1 line both works same
print(my_cursor.fetchall())

conn.commit()
conn.close()
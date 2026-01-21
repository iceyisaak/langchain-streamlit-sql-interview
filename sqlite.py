import sqlite3

connection=sqlite3.connect("student.db")

cursor=connection.cursor()

table_info="""
CREATE TABLE student(student_id SERIAL PRIMARY KEY, name VARCHAR(25), subject VARCHAR(25), grade VARCHAR(25), marks INT)
"""

cursor.execute(table_info)


cursor.execute("""INSERT INTO student VALUES(1,'Ann','Science','A',90)""")
cursor.execute("""INSERT INTO student VALUES(2,'Bob','Science','A',100)""")
cursor.execute("""INSERT INTO student VALUES(3,'Claire','Maths','B',85)""")
cursor.execute("""INSERT INTO student VALUES(4,'Dennis','Maths','B',82)""")
cursor.execute("""INSERT INTO student VALUES(5,'Emma','German','C',77)""")
cursor.execute("""INSERT INTO student VALUES(6,'Frank','German','C',79)""")


print("The inserted records are: ")
data=cursor.execute("""SELECT * FROM student""")
for row in data:
    print(row)




connection.commit()
connection.close()


# run: `python sqlite.py`
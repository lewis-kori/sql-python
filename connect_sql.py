import mysql.connector 

my_db= mysql.connector.connect(host="localhost",user="root",password="",database='world')
my_cursor=my_db.cursor()

# adding the Info column to the city table
# my_cursor.execute("ALTER TABLE city ADD Information INT(11) ")

# copying the contents of Population column to Info column within city table
# my_cursor.execute("UPDATE city  SET Information=info ")
# my_db.commit()

# altering the Population column to store float datatype
# my_cursor.execute("ALTER TABLE city MODIFY COLUMN Information FLOAT(30,2) ")
# my_db.commit()

# Increasing the population by 20%
# my_cursor.execute("UPDATE city SET Information=Information * 1.1")
# record=my_cursor.fetchone()
my_cursor.execute("SELECT Information FROM city")
record=my_cursor.fetchone()
while record is not None:
    print(record)
    record = my_cursor.fetchone()

# print(record)
# my_db.commit()



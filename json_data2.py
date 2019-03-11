import json
import mysql.connector

db=mysql.connector.connect(host="localhost",user="root",password="",database='world_x')
my_cursor=db.cursor()
"""start here and comment out each section as you go forward
make sure to leave back the comments after each step to avoid duplicates.
You can exclude the comments if you want the entire script to alter the database
in a single step as opposed to step by step altering."""


# creating a new column called population
# my_cursor.execute("ALTER TABLE city ADD Population INT(25) ")

# copying info content values to Population column
# my_cursor.execute("UPDATE city  SET Population=JSON_EXTRACT(info,\"$.Population\")")


# altering the Population column to store float datatype
# my_cursor.execute("ALTER TABLE city MODIFY COLUMN Population FLOAT(30,2)")

"""my_cursor.execute("SELECT Population FROM city")
record=my_cursor.fetchone()
print("Population before increase ")
while record is not None:
    print(record)
    record = my_cursor.fetchone()
"""

# Increasing the population by 10%
# my_cursor.execute("UPDATE city SET Population=Population * 1.1")
# db.commit()


"""
print("Population After 10% increase")
record=my_cursor.fetchone()
while record is not None:
    print(record)
    record = my_cursor.fetchone()
"""
import csv
import sqlite3

with sqlite3.connect("new.db") as connection, open("employees.csv","rU") as f:
    cursor = connection.cursor()
    employees = csv.reader(f)

    cursor.execute('''CREATE TABLE employees (
                        firstname TEXT,
                        lastname TEXT)''')

    cursor.executemany('''INSERT INTO employees VALUES (?,?)''', employees)

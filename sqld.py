import sqlite3

with sqlite3.connect("new.db") as connection:
    cursor = connection.cursor()

    cursor.execute('''SELECT * FROM employees''')
    employees =  cursor.fetchall()
    for employee in employees:
        print "firstname = {0[0]}, lastname = {0[1]}".format(employee)

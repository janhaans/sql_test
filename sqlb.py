import sqlite3

with sqlite3.connect("new.db") as connection:
    cursor = connection.cursor()
    cursor.execute('''INSERT INTO population VALUES ('New York', 'NY', 8200000)''')
    cursor.execute('''INSERT INTO population VALUES ('San Francisco', 'CA', 800000)''')

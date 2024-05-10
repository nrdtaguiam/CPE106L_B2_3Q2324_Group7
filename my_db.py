"""
Python program to create employees database.
All columns are TEXT, except for age and gender that are INTEGER.
With 0=male and 1=female for the gender.
"""

import sqlite3

conn = sqlite3.connect('employees.db')

c = conn.cursor()

c.execute("""CREATE TABLE employees (
            first_name TEXT,
            last_name TEXT,
            age INTEGER,
            gender INTEGER,
            department TEXT,
            address TEXT,
            username TEXT,
            password TEXT,
            confirm_password TEXT
)""")

# c.execute("INSERT INTO employees VALUES ('Sander', 'Demdam', 20, 0, 'Finance', 'Manila City', 'Sander123', 'Sander123', 'Sander123')")

all_employees = [
    ('Mark', 'Ford', 20, 0, 'Finance', 'Manila City', 'Mark123', 'Mark123', 'Mark123'),
    ('Angela', 'Mush', 20, 1, 'Marketing', 'Cavite City', 'Angela123', 'Angela123', 'Angela123'),
    ('Dustin', 'Tey', 19, 0, 'Operations', 'Tacloban City', 'Dustin123', 'Dustin123', 'Dustin123')
]

c.executemany("INSERT INTO employees VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", all_employees)

c.execute("SELECT * FROM employees")
my_data = c.fetchall()

for i in my_data:
    print(i)

conn.commit()
conn.close()
# import sqlite3
# with sqlite3.connect('profile.db') as con:
#     cur = con.cursor()
#     cur.execute('''CREATE TABLE users (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT NOT NULL,
#         summa REAL,
#         date BLOB
    
# )''')

# cur.execute("DROP TABLE users")

import sqlite3

with sqlite3.connect('users.db') as con:
    cur = con.cursor()
    #  cur.execute('''CREATE TABLE IF NOT EXISTS person (
    #     id INTEGER PRIMARY KEY AUTOINCREMENT,
    #     name TEXT NOT NULL,
    #     phone BLOB DEFAULT "+79990000000",
    #     age INTEGER NOT NULL CHECK (age >= 0 AND age <=100),
    #     email TEXT UNIQUE NOT NULL
    #     )''')
    #  cur.execute('''
    #     ALTER TABLE person_table
    #     ADD COLUMN surname TEXT NOT NULL DEFAULT "fio"
    #     ''')
    # cur.execute('''
    #     ALTER TABLE person_table
    #     RENAME COLUMN address TO home_address
    #     ''')
    # cur.execute('''
    #     DROP TABLE person_table
    #     ''')

import sqlite3

conn = sqlite3.connect('user.db')
print ("Opened database successfully")

# create tables users, products
conn.execute('''
CREATE TABLE IF NOT EXISTS users 
    (
    id integer PRIMARY KEY,
    name text NOT NULL,
    password text NOT NULL
    );
''')

conn.execute('''
CREATE TABLE IF NOT EXISTS products 
    (
    id integer PRIMARY KEY,
    name text NOT NULL,
    price float NOT NULL
    );
''')

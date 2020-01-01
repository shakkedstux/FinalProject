
import sqlite3

# connect to data base - if not exist - creating it
conn = sqlite3.connect('user.db')

# create tables users, products - if they're not exist - necessary?
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


# add to tables
conn.execute('''
INSERT INTO users
    (name, password) \
    VALUES ('shakked', 'aaaa')
''')

conn.execute('''
INSERT INTO users
    (name, password) \
    VALUES ('nathan', 'bbbb')
''')

conn.execute('''
INSERT INTO products
    (name, price) \
    VALUES ('shirt', 50)
''')

conn.execute('''
INSERT INTO products
    (name, price) \
    VALUES ('shoes', '100')
''')

conn.execute('''
INSERT INTO products
    (name, price) \
    VALUES ('hat', '36')
''')


conn.commit() # ?
conn.close() # closing the connection

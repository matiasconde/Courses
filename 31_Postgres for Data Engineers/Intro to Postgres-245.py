## 2. Connecting to Postgres ##

import psycopg2

conn = psycopg2.connect("dbname=dq user=dq")
print(conn)
conn.close()

## 3. Interacting with the Database ##

import psycopg2

conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
cur.execute("SELECT * FROM notes")
notes = cur.fetchall()
conn.close()

## 4. Creating a Table ##

conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS users")
cur.execute("CREATE TABLE users(\
            id integer PRIMARY KEY,\
            email text,\
            name text,\
            address text);")



## 5. SQL Transactions ##

conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS users")
cur.execute("CREATE TABLE users(\
             id integer PRIMARY KEY,\
             email text,\
             name text,\
             address text);")

conn.commit()
conn.close()

## 6. Inserting the Data ##

import csv
import psycopg2

conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS users")
cur.execute("CREATE TABLE users(\
             id integer PRIMARY KEY,\
             email text,\
             name text,\
             address text);")

conn.commit()

with open("user_accounts.csv",'r') as f:
    reader = csv.reader(f)
    next(reader)  # esto es para que no tome la primer linea
    rows = [row for row in reader]
    
for row in rows: 
    cur.execute("INSERT INTO users VALUES (%s,%s,%s,%s)",row)
conn.commit()            

cur.execute("SELECT * FROM users")
users = cur.fetchall()
conn.close()
print(type(users))

## 7. Copying the Data ##

conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
with open('user_accounts.csv') as f:
    next(f)  # Skip header.
    cur.copy_from(f, 'users', sep=",")
conn.commit()

cur.execute('SELECT * FROM users')
users = cur.fetchall()
conn.close()
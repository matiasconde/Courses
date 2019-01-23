## 1. Introduction ##

import psycopg2
conn = psycopg2.connect("dbname=dq user=hud_admin password=eRqg123EEkl;")
print(conn)

## 2. Investigating the Tables ##

conn = psycopg2.connect(dbname="dq", user="hud_admin", password="eRqg123EEkl")
cur = conn.cursor()
cur.execute("SELECT table_name FROM information_schema.tables ORDER BY table_name;")
table_names = cur.fetchall()
for table in table_names:
    print(table)

## 3. Working with Schemas ##

conn = psycopg2.connect(dbname="dq", user="hud_admin", password="eRqg123EEkl")
cur = conn.cursor()
cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public' ORDER BY table_name;")
for table_name in cur.fetchall(): print(table_name)

## 4. Describing the Tables ##

from psycopg2.extensions import AsIs

conn = psycopg2.connect(dbname="dq", user="hud_admin", password="eRqg123EEkl")
cur = conn.cursor()

cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public'")
for table in cur.fetchall(): 
    proper_interpolation = cur.mogrify("""SELECT * FROM %s LIMIT 0""",[AsIs(table[0])])
    cur.execute(proper_interpolation)
    print(cur.description[0][0])
    print(cur.description)
    
    print(" ")
    

## 5. Type Code Mappings ##

conn = psycopg2.connect(dbname="dq", user="hud_admin", password="eRqg123EEkl")
cur = conn.cursor()
type_mappings = {}

cur.execute("SELECT oid,typname FROM pg_catalog.pg_type")
for oid,typname in cur.fetchall(): 
    key = int(oid)
    value = typname
    type_mappings[key]=value

## 6. Readable Description Types ##

from psycopg2.extensions import AsIs
conn = psycopg2.connect(dbname="dq", user="hud_admin", password="eRqg123EEkl")
cur = conn.cursor()
# You have `table_names` and `type_mappings` provided for you.
readable_description = {}
for table in table_names:
    proper_interpolation = cur.mogrify("""SELECT * FROM %s LIMIT 0""",[AsIs(table)]) 
    cur.execute(proper_interpolation)
    tupla = cur.description
    columns = []
    for column in tupla:
        dict_column = {'name':column[0],'type':type_mappings[column[1]],'internal_size':column[3]}
        columns.append(dict_column)

    readable_description[table] = columns
    
print(readable_description)

## 7. Number of Rows ##

from psycopg2.extensions import AsIs
conn = psycopg2.connect(dbname="dq", user="hud_admin", password="eRqg123EEkl")
cur = conn.cursor()
for k,v in readable_description.items():
    dic = readable_description[k]
    proper = cur.mogrify("SELECT COUNT(*) FROM %s",[AsIs(k)])
    cur.execute(proper)
    tot = cur.fetchone()
    dic['total']=tot
    readable_description[k] = dic
print(readable_description)

## 8. Sample Rows ##

from psycopg2.extensions import AsIs
conn = psycopg2.connect(dbname="dq", user="hud_admin", password="eRqg123EEkl")
cur = conn.cursor()
for key in readable_description.keys():
    proper = cur.mogrify("SELECT * FROM %s LIMIT 100",[AsIs(key)])
    cur.execute(proper)
    readable_description[key]['sample_rows'] = cur.fetchall() 
print(readable_description)
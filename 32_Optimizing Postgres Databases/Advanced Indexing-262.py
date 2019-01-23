## 1. Querying with Multiple Filters ##

conn = psycopg2.connect(dbname="dq", user="hud_admin", password="abc123")
cur = conn.cursor()
cur.execute("""CREATE INDEX state_idx ON homeless_by_coc(state);""")
conn.commit()

cur.execute("""EXPLAIN (FORMAT json, ANALYZE) SELECT * FROM homeless_by_coc WHERE state = 'CA' AND  year > '1991-01-01'""")

pp.pprint(cur.fetchall())



## 3. Adding Another Index ##

conn = psycopg2.connect(dbname="dq", user="hud_admin", password="abc123")
cur = conn.cursor()
cur.execute("DROP INDEX IF EXISTS state_idx")
cur.execute("DROP INDEX IF EXISTS state_year_idx")

conn.commit()
cur.execute("""CREATE INDEX state_idx ON homeless_by_coc(state)""")
conn.commit()
cur.execute("""EXPLAIN (FORMAT json, ANALYZE) SELECT * FROM homeless_by_coc WHERE state='CA' AND year>'1991-01-01'""")
pp.pprint(cur.fetchall())
pp.pprint(" ")
cur.execute("CREATE INDEX state_year_idx ON homeless_by_coc(state,year)")
conn.commit()
cur.execute("""EXPLAIN (FORMAT json,ANALYZE) SELECT * FROM homeless_by_coc WHERE state='CA' AND year>'1991-01-01'""")
pp.pprint(cur.fetchall())

## 4. Multiple Indexes ##

conn = psycopg2.connect(dbname="dq", user="hud_admin", password="abc123")
cur = conn.cursor()
cur.execute("CREATE INDEX state_year_coc_number_idx ON homeless_by_coc(state,year,coc_number)")
conn.commit()

## 5. The Tradeoff of Using Indexes ##

import time
conn = psycopg2.connect(dbname="dq", user="hud_admin", password="abc123")
cur = conn.cursor()
cur.execute("""DROP INDEX IF EXISTS state_year_idx; DROP INDEX IF EXISTS state_idx;""")
conn.commit()
with open('homeless_by_coc.csv','r') as f:
    start_time = time.time()
    cur.copy_expert("""COPY homeless_by_coc FROM STDIN WITH CSV HEADER""",f)
    end_time = (time.time() - start_time)
    print(end_time)
    print(" ")
conn.commit() 

cur.execute("DELETE FROM homeless_by_coc")

cur.execute("CREATE INDEX state_year_idx ON homeless_by_coc(state,year);")
conn.commit()

with open('homeless_by_coc.csv','r') as f:
    start_time = time.time()
    cur.copy_expert("""COPY homeless_by_coc FROM STDIN WITH CSV HEADER""",f)
    end_time = (time.time() - start_time)
    print(end_time)
    print(" ")
conn.commit() 


## 6. Order By Index ##

conn = psycopg2.connect(dbname="dq", user="hud_admin", password="abc123")
cur = conn.cursor()
cur.execute("DROP INDEX state_year_idx")
conn.commit() 

cur.execute("""CREATE INDEX state_year_idx ON homeless_by_coc(state,year ASC);""")
conn.commit()

cur.execute("""SELECT DISTINCT year FROM homeless_by_coc WHERE state='CA' AND year> '1991-01-01'""")

ordered_years = cur.fetchall()

pp.pprint(ordered_years)

## 7. Index on Expressions ##

conn = psycopg2.connect(dbname="dq", user="hud_admin", password="abc123")
cur = conn.cursor()
cur.execute("DROP INDEX measures_idx")
cur.execute("CREATE INDEX measures_idx ON homeless_by_coc(lower(measures))")
conn.commit()

cur.execute("""SELECT * FROM homeless_by_coc WHERE lower(measures) = 'unsheltered homeless people in families' LIMIT 1;""")
unsheltered_row = cur.fetchone()

## 8. Partial Indexes ##

conn = psycopg2.connect(dbname="dq", user="hud_admin", password="abc123")
cur = conn.cursor()

cur.execute("""CREATE INDEX state_count_idx ON homeless_by_coc(state) WHERE count>0""")
conn.commit()

cur.execute("""EXPLAIN (FORMAT json, ANALYZE) SELECT * FROM homeless_by_coc WHERE state='CA' AND count>0""")

pp.pprint(cur.fetchall())
          



## 9. Building a Multi-Column Index ##

conn = psycopg2.connect(dbname="dq", user="hud_admin", password="abc123")
cur = conn.cursor() 

cur.execute("""CREATE INDEX compuesto ON homeless_by_coc(state,year,lower(measures)) WHERE year>'2007-01-01'""")
conn.commit()

cur.execute("""EXPLAIN (FORMAT json, ANALYZE) SELECT hbc.year, si.name, hbc.count FROM homeless_by_coc hbc, state_info si WHERE hbc.state = si.postal AND hbc.year > '2007-01-01' AND hbc.measures != 'total homeless'""")

pp.pprint(cur.fetchall())
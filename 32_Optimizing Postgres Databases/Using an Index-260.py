## 1. Alternate Table Scans ##

import pprint as pp

conn = psycopg2.connect(dbname="dq", user="hud_admin", password="abc123")
cur = conn.cursor()
proper = cur.mogrify("""EXPLAIN (format json) SELECT * FROM homeless_by_coc WHERE id=10;""")
cur.execute(proper)
pp.pprint(cur.fetchall())

## 2. Index Scan ##

conn = psycopg2.connect(dbname="dq", user="hud_admin", password="abc123")
cur = conn.cursor()

cur.execute("""EXPLAIN (FORMAT json) SELECT * FROM homeless_by_coc WHERE homeless_by_coc.id = 5;""")
homeless_query_plan = cur.fetchall()

cur.execute("""EXPLAIN (FORMAT json) SELECT * FROM state_info WHERE state_info.name = 'Alabama';""")
state_query_plan = cur.fetchall()

cur.execute("""EXPLAIN (FORMAT json) SELECT * FROM state_household_incomes WHERE state_household_incomes.state = 'Georgia';""")
incomes_query_plan = cur.fetchall()

pp.pprint(homeless_query_plan)
pp.pprint(state_query_plan)
pp.pprint(incomes_query_plan)


## 4. Indexing ##

import pprint as pp

conn = psycopg2.connect(dbname="dq", user="hud_admin", password="abc123")
cur = conn.cursor()
cur.execute("DROP TABLE state_idx")
conn.commit()
cur.execute("""CREATE TABLE state_idx(\
                            id INT,\
                            name TEXT,\
                            primary key (id,name));\
 INSERT INTO state_idx SELECT id, state FROM homeless_by_coc;""")
conn.commit()

cur.execute("""SELECT h.state, h.year, h.coc_number FROM homeless_by_coc as h, state_idx WHERE state_idx.id = h.id AND state_idx.name = 'CA';""")

pp.pprint(cur.fetchall())
                                

## 5. Comparing the Queries ##

conn = psycopg2.connect(dbname="dq", user="hud_admin", password="abc123")
cur = conn.cursor()
cur.execute("""EXPLAIN  (FORMAT json, ANALYZE)
SELECT hbc.id, hbc.year, hbc.coc_number FROM homeless_by_coc hbc, state_idx
WHERE state_idx.state = 'CA' AND state_idx.homeless_id = hbc.id
""")

pp.pprint(cur.fetchall())

cur.execute("""EXPLAIN (FORMAT json, ANALYZE) SELECT * FROM homeless_by_coc WHERE state = 'CA'""")
pp.pprint(cur.fetchall())

## 6. Create an Index ##

conn = psycopg2.connect(dbname="dq", user="hud_admin", password="abc123")
cur = conn.cursor()

cur.execute("""CREATE INDEX state_idx ON homeless_by_coc(state)""")
conn.commit()

cur.execute("""EXPLAIN (FORMAT json, ANALYZE) SELECT * FROM homeless_by_coc WHERE state = 'CA'""")

pp.pprint(cur.fetchall())

## 7. Dropping Indexes ##

conn = psycopg2.connect(dbname="dq", user="hud_admin", password="abc123")
cur = conn.cursor()
cur.execute("DROP INDEX IF EXISTS state_idx")
conn.commit()
cur.execute("CREATE INDEX state_idx ON homeless_by_coc(state)")
conn.commit()
cur.execute("EXPLAIN (ANALYZE, format json) SELECT * FROM homeless_by_coc WHERE state='CA'")
pp.pprint(cur.fetchall())
pp.pprint(" ")
cur.execute("DROP INDEX IF EXISTS state_idx")
conn.commit()
cur.execute("EXPLAIN (ANALYZE, format json) SELECT * FROM homeless_by_coc WHERE state='CA'")
pp.pprint(cur.fetchall())


## 8. Index Performance on Joins ##

conn = psycopg2.connect(dbname="dq", user="hud_admin", password="abc123")
cur = conn.cursor()
cur.execute("DROP INDEX IF EXISTS state_idx")
conn.commit()
cur.execute("""EXPLAIN (FORMAT json, ANALYZE) SELECT hbc.state, hbc.coc_number, hbc.coc_name, si.name FROM homeless_by_coc as hbc, state_info as si WHERE hbc.state = si.postal""")
pp.pprint(cur.fetchall())
pp.pprint(" ")
cur.execute("CREATE INDEX state_idx ON homeless_by_coc(state)")
conn.commit()

cur.execute("""EXPLAIN (FORMAT json, ANALYZE) SELECT hbc.state, hbc.coc_number, hbc.coc_name, si.name FROM homeless_by_coc as hbc, state_info as si WHERE hbc.state = si.postal""")
pp.pprint(cur.fetchall())


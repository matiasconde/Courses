## 1. Augmenting Pandas With SQLite ##

import sqlite3
import pandas as pd
conn = sqlite3.connect('moma.db')
moma_iter = pd.read_csv('moma.csv', chunksize=1000)
for chunk in moma_iter:
    chunk.to_sql("exhibitions", conn, if_exists='append', index=False)

## 2. Pandas Types vs. SQLite Types ##

results_df = pd.read_sql('PRAGMA table_info(exhibitions);',conn)
print(results_df)

## 3. Setting Appropriate Types ##

moma_iter = pd.read_csv("moma.csv",chunksize=1000)

for chunk in moma_iter:
    chunk["ExhibitionSortOrder"] = chunk["ExhibitionSortOrder"].astype('int16')
    chunk.to_sql("exhibitions",conn,index=False,if_exists='append')
    
results_df = pd.read_sql("PRAGMA table_info(exhibitions);",conn)
print(results_df)

## 4. Computing Primarily in SQL ##

eid_counts = pd.read_sql("SELECT exhibitionid, COUNT(*) as counts FROM exhibitions GROUP BY exhibitionid ORDER BY counts DESC;",conn)

## 5. Computing Primarily in Pandas ##

df = pd.read_sql("SELECT ExhibitionID FROM exhibitions;",conn)
eid_pandas_counts = df["ExhibitionID"].value_counts()

## 6. Reading in SQL Results Using Chunks ##

import time

start1 = time.time()
eid_counts = pd.read_sql("SELECT exhibitionid, COUNT(*) as counts FROM exhibitions GROUP BY exhibitionid ORDER BY counts DESC;",conn)
end1 = time.time()
print(end1 - start1)

start = time.time()
q = 'select exhibitionid from exhibitions;'
chunk_iter = pd.read_sql(q, conn, chunksize=10000)

lista = []

for chunk in chunk_iter:
    calculation = chunk["ExhibitionID"].value_counts()
    lista.append(calculation)
    
full_value_counts = pd.concat(lista)
full_value_counts2 = full_value_counts.groupby(full_value_counts.index).sum()

end = time.time()

print(end-start)


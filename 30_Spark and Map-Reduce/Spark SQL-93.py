## 2. Register the DataFrame as a Table ##

from pyspark.sql import SQLContext
sqlCtx = SQLContext(sc)
df = sqlCtx.read.json("census_2010.json")

df.registerTempTable("census2010")
tables = sqlCtx.tableNames
print(tables)

## 3. Querying ##

sqlCtx.sql("SELECT age FROM census2010").show()

## 4. Filtering ##

query = 'SELECT males, females FROM census2010 WHERE (age < 15) AND (age > 5)'

sqlCtx.sql(query).show()

## 5. Mixing Functionality ##

query = "SELECT males, females FROM census2010"

df = sqlCtx.sql(query)
df.describe().show()

## 6. Multiple tables ##

from pyspark.sql import SQLContext
sqlCtx = SQLContext(sc)
df = sqlCtx.read.json("census_2010.json")
df.registerTempTable('census2010')

df2 = sqlCtx.read.json("census_1980.json")
df2.registerTempTable("census1980")

df3 = sqlCtx.read.json("census_1990.json")
df3.registerTempTable("census1990")

df4 = sqlCtx.read.json("census_2000.json")
df4.registerTempTable("census2000")

tables = sqlCtx.tableNames()
print(tables)

## 7. Joins ##

query = "SELECT c1.total, c2.total FROM census2010 c1 INNER JOIN census2000 c2 ON c1.age = c2.age"

sqlCtx.sql(query).show(20)

## 8. SQL Functions ##

query = "SELECT SUM(c1.total), SUM(c2.total), SUM(c3.total) FROM census2010 c1 INNER JOIN census2000 c2 ON c1.age = c2.age INNER JOIN census1990 c3 ON c1.age = c3.age"

sqlCtx.sql(query).show()
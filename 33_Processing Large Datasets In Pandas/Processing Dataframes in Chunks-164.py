## 2. Processing Chunks ##

import pandas as pd
import matplotlib.pyplot as plt

memory_footprints = []

chunk_iter = pd.read_csv("moma.csv", chunksize = 250)

for chunk in chunk_iter: 
    memory_footprints.append(chunk.memory_usage(deep='True').sum()/1048576)
    
plt.hist(memory_footprints)
plt.show()
print(memory_footprints)

## 3. Counting Across Chunks ##

num_rows = 0

chunk_iter = pd.read_csv('moma.csv',chunksize=250)

for chunk in chunk_iter:
    num_rows += len(chunk)
    
print(num_rows)

## 4. Batch Processing ##

lifespans = []
dtypes = {'ConstituentEndDate':'float','ConstituentBeginDate':'float'}
chunk_iter = pd.read_csv("moma.csv",chunksize = 250, dtype=dtypes)

for chunk in chunk_iter:
    serie = chunk["ConstituentEndDate"] - chunk["ConstituentBeginDate"]
    lifespans.append(serie)
    
lifespans_dist = pd.concat(lifespans)
print(lifespans_dist)

## 5. Optimizing Performance ##

import time

lifespans = []
start1 = time.time()
chunk_iter = pd.read_csv("moma.csv", chunksize=250, dtype={"ConstituentBeginDate": "float", "ConstituentEndDate": "float"})
for chunk in chunk_iter:
    lifespans.append(chunk['ConstituentEndDate'] - chunk['ConstituentBeginDate'])
lifespans_dist = pd.concat(lifespans)
end1 = time.time()

print(end1 - start1)

start2 = time.time()
# %%timeit
lifespans = []
chunk_iter = pd.read_csv("moma.csv", chunksize=250, dtype={"ConstituentBeginDate": "float", "ConstituentEndDate": "float"},  usecols=['ConstituentBeginDate', 'ConstituentEndDate'])
for chunk in chunk_iter:
    lifespans.append(chunk['ConstituentEndDate'] - chunk['ConstituentBeginDate'])
lifespans_dist = pd.concat(lifespans)
end2 = time.time()

print(end2 - start2)

## 6. Counting Unique Values ##

chunk_iter = pd.read_csv("moma.csv", chunksize=250, usecols=['Gender'])
print(chunk_iter)

overall_vc = []

for chunk in chunk_iter: 
    unique = chunk['Gender'].value_counts()
    overall_vc.append(unique)
    
combined_vc = pd.concat(overall_vc)



## 7. Combining Chunks Using GroupBy ##

chunk_iter = pd.read_csv("moma.csv", chunksize=250, usecols=['Gender'])

overall_vc = []

for chunk in chunk_iter: 
    overall_vc.append(chunk["Gender"].value_counts())
    
combined_vc = pd.concat(overall_vc)

final_vc = combined_vc.groupby(combined_vc.index).sum()

## 8. Working With Intermediate Dataframes ##

chunk_iter = pd.read_csv("moma.csv",chunksize=1000,usecols = ["ExhibitionID","Gender"])

resumen = []

for chunk in chunk_iter:
    unique = chunk["Gender"].groupby(chunk["ExhibitionID"]).value_counts()
    resumen.append(unique)

overall = pd.concat(resumen)
id_gender_counts = overall.groupby(overall.index).sum()


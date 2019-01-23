## 3. The Dataset ##

import pandas as pd

data = pd.read_csv("ecommerce5000.csv", encoding="Latin-1")
data.head()

## 5. Finding duplicate values ##

iz_operations = 0
item_operations = 0
duplicates_init = 0
duplicates_false = 0
duplicates_true = 0
if_duplicate = 0
duplicates_append = 0

duplicates_init += 1
duplicates = []

# Loop through each item in the query column.
for i, item in enumerate(query):
    duplicates_false += 1
    duplicate = False

    # Loop through each item in the query column.
    for z, item2 in enumerate(query):
        # If the outer and inner loops are on the same value, keep going.
        # Without this, we'll falsely detect rows as duplicates.
        iz_operations += 1
        if i == z:
            continue
        # Mark as duplicate if we find a match.
        item_operations += 1
        if item == item2:
            duplicates_true += 1
            duplicate = True
    # Add to the duplicates list.
    if_duplicate += 1
    if duplicate:
        duplicates_append += 1
        duplicates.append(item)

## 6. Big O notation ##

sum_increments = 0
total = 0

sum_increments = 0

for item in query: 
    sum_increments += 1
    total += len(item)
    


## 7. O(n^2) ##

counts_increments = 0
value_checks = 0
counts = {}

for item in query: 
    if item not in counts:
        counts[item] = 0
    if item in counts:
        counts_increments += 1
        counts[item] += 1
        
duplicates = []

for k,v in counts.items():
    value_checks += 1
    if v>1: duplicates.append(v)

print(counts_increments)
print(value_checks)
print(len(counts))
 

## 8. Timing code runs ##

import time

start1 = time.time()
duplicate_series = query_series.duplicated()
duplicate_values_series = query_series[duplicate_series]
end1 = time.time()

pandas_elapsed = end1 - start1
print(pandas_elapsed)
print(" ")

start2 = time.time()
counts_increments = 0
value_checks = 0
counts = {}

for item in query: 
    if item not in counts:
        counts[item] = 0
    if item in counts:
        counts_increments += 1
        counts[item] += 1
        
duplicates = []

for k,v in counts.items():
    value_checks += 1
    if v>1: duplicates.append(v)
end2 = time.time()

elapsed = end2 - start2

print(elapsed)

## 9. Stable time estimates ##

import time
import statistics
import matplotlib.pyplot as plt

def pandas_duplicates(): 
    duplicate_series = query_series.duplicated()
    duplicate_values_series = query_series[duplicate_series]


def normal_duplicates():
    counts = {}

    for item in query: 
        if item not in counts:
            counts[item] = 0
        if item in counts:
            counts[item] += 1
        
    duplicates = []

    for k,v in counts.items():
        if v>1: duplicates.append(v)
pandas_elapsed = []
for i in range(1000):
    start1 = time.time()
    pandas_duplicates()
    end1 = time.time()
    delta = end1 - start1
    pandas_elapsed.append(delta)
    
elapsed = []
for i in range(1000):
    start2 = time.time()
    normal_duplicates()
    end2 = time.time()
    delta2 = end2 - start2
    elapsed.append(delta2)

print(statistics.median(pandas_elapsed))
print(statistics.median(elapsed))

plt.hist(pandas_elapsed)
plt.show()
plt.hist(elapsed)


## 10. Refactoring ##

import time
import statistics

deltas = []
for i in range(1000):
    start = time.time()
    duplicados = []
    dic = {}
    for item in query:
        if item not in dic:
            dic[item]=0
            duplicados.append(item)
    end = time.time()
    deltas.append(end - start)
    
print(statistics.median(deltas))

plt.hist(deltas)
plt.show()


        
        

## 12. Alternate profiling strategies ##

import cProfile

def algo():
    unique = set()
    duplicates = set()
    for item in query:
        if item in unique:
            duplicates.add(item)
        else:
            unique.add(item)
            
cProfile.run('algo()')

## 13. Practicing writing efficient algorithms ##

import time 
import statistics

def pandas_algo():
    data1 = data[["relevance","product_link","query"]]
    get_max_relevance = lambda x: x.loc[x["relevance"].idxmax(), "product_link"]
    return data1.groupby("query").apply(get_max_relevance)

def algo():
    data1 = data[["relevance","product_link","query"]]
    dic = {}
    for row in data1.iterrows():
        relevance = row[1]["relevance"]
        item = row[1]["query"]
        link = row[1]["product_link"]
        if item not in dic:
            dic[item] = (relevance,link)
        if (item in dic) and (relevance > dic[item][0]):
            dic[item] = (relevance,link)
    return dic

def algo2():
    relevance = data["relevance"].tolist()
    links = data["product_link"].tolist()
    query = data["query"].tolist()
    dic = {}
    for i,item in enumerate(query):
        if item not in dic: 
            dic[item] = [0,""]
        elif (relevance[i] > dic[item][0]):
            dic[item] = [relevance[i],links[i]]
    return dic          

def run_with_timing(func):
    elapsed = []
    for i in range(10):
        start = time.time()
        func()
        elapsed.append(time.time() - start)
    return statistics.median(elapsed)

pandas_elapsed = run_with_timing(pandas_algo)
elapsed = run_with_timing(algo)
elapsed2 = run_with_timing(algo2)

print(pandas_elapsed)
print(" ")
print(elapsed)
print(" ")
print(elapsed2)


## 14. Big O Notation practice ##

import re
import statistics

algo1_time_complexity = 0
algo1_space_complexity = 0

def algo1(data):
    total = 0
    for index, row in data.iterrows():
        total += int(row["rank"])
    return total

algo2_time_complexity = 0
algo2_space_complexity = 0

def algo2(data):
    prices = []
    for index, row in data.iterrows():
        price_search = re.search('.*(\d+).*', row["product_price"], re.IGNORECASE)

        if price_search:
            price = float(price_search.group(1))
        else:
            price = None
        prices.append(price)
    price_avg = statistics.mean([p for p in prices if p is not None])
    weighted_relevance = []
    for index, row in data.iterrows():
        if prices[index] is not None:
            price = prices[index] / price_avg
        else:
            price = price_avg
        weighted_relevance.append(float(row["relevance"]) * price)
    return weighted_relevance

algo1_space_complexity = 0
algo1_time_complexity = 1

algo2_space_complexity = 1
algo2_time_complexity = 1
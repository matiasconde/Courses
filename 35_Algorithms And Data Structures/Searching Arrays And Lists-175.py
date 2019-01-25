## 2. Searching Arrays ##

import pandas as pd

data = pd.read_csv("amounts.csv")
amounts = list(data["Amount"])
times = [int(i) for i in list(data["Time"])]

first_4554 = times.index(4554)

## 3. Linear Search ##

def linear_search(array, search):
    indexes = []
    for i,v in enumerate(array):
        if v==search:
            indexes.append(i)
    return indexes

sevens = linear_search(times,7)

## 4. Searching Multiple Arrays ##

def linear_multi_search(array, search):
    indexes = []
    for i,v in enumerate(array):
        if (v[0] == search[0]) and (v[1] == search[1]):
            indexes.append(i)
    return indexes

transactions = [[times[i],amounts[i]] for i in range(len(times))]
results = linear_multi_search(transactions,[56,10.84])


## 5. Profiling Linear Search ##

import matplotlib.pyplot as plt

def linear_search(array, search):
    counter = 0
    indexes = []
    for i, item in enumerate(array):
        counter += 1
        if item == search:
            indexes.append(i)
    return counter

lengths = [10,100,1000,10000]
counters = []
for length in lengths:
    first_amounts = amounts[:length]
    counters.append(linear_search(first_amounts,7))
    
plt.plot(lengths,counters)
plt.show()

## 7. Binary Search ##

import math

def swap(array, pos1, pos2):
    store = array[pos1]
    array[pos1] = array[pos2]
    array[pos2] = store

def insertion_sort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j - 1] > array[j]:
            swap(array, j, j-1)
            j-=1

def binary_search(array, search):
    mid_point = 0
    z = len(array) - 1
    i = 0
    while i <= z: 
        mid_point = math.floor((i+z)/2)
        if search == array[mid_point]: return mid_point
        elif array[mid_point] < search:
            i = mid_point + 1
        else: 
            z = mid_point - 1

result = binary_search(times,56)

## 8. Complex Criteria With Binary Search ##

def insertion_sort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j - 1] > array[j]:
            swap(array, j, j-1)
            j-=1

def binary_search(array, search):
    array.sort()
    m = 0
    i = 0
    z = len(array) - 1
    while i<= z:
        m = math.floor(i + ((z - i) / 2))
        if array[m] == search:
            return m
        elif array[m] < search:
            i = m + 1
        elif array[m] > search:
            z = m - 1
            
transactions = ["{}_{}".format(times[i],amounts[i]) for i in range(len(amounts))]
print(transactions)
result = binary_search(transactions,"56_10.84")

## 9. Fuzzy Matches With Binary Search ##

def binary_search(array, search):
    array.sort()
    m = 0
    i = 0
    z = len(array) - 1
    while i<= z:
        m = math.floor(i + ((z - i) / 2))
        if array[m] == search:
            return m
        elif array[m] < search:
            i = m + 1
        elif array[m] > search:
            z = m - 1
    return m

def fuzzy_match(array, lower, upper, m):
    j = m 
    l = m+1
    matches = []
    
    while  (0<j) and (lower <= array[j] <= upper):
        matches.append(array[j])
        j -= 1
    while (l<len(array)) and (lower <= array[l] <= upper):
        matches.append(array[l])
        l += 1
    return matches

m = binary_search(amounts,150)
matches = fuzzy_match(amounts,100,2000,m)

print(matches)

## 10. Profiling Binary Search ##

import matplotlib.pyplot as plt

def binary_search(array, search):
    array.sort()
    m = 0
    i = 0
    z = len(array) - 1
    counter = 0
    while i<= z:
        counter += 1
        m = math.floor(i + ((z - i) / 2))
        if array[m] == search:
            return m
        elif array[m] < search:
            i = m + 1
        elif array[m] > search:
            z = m - 1
    return counter

lengths = [10,100,1000,10000]
counters = []
for length in lengths:
    first_amounts = amounts[:length]
    counters.append(binary_search(first_amounts,-1))
    
plt.plot(lengths,counters)
plt.show()

## 11. Profiling Binary Search With Sorting ##

def insertion_sort(array):
    counter = 0
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j - 1] > array[j]:
            counter += 1
            swap(array, j, j-1)
            j-=1
    return counter

def binary_search(array, search):
    counter = insertion_sort(array)
    insertion_sort(array)
    m = 0
    i = 0
    z = len(array) - 1
    while i<= z:
        counter += 1
        m = math.floor(i + ((z - i) / 2))
        if array[m] == search:
            return m
        elif array[m] < search:
            i = m + 1
        elif array[m] > search:
            z = m - 1
    return counter

lengths = [10,100,1000,10000]

counters = []
for i in lengths:
     # We sort in reverse order so we get the worst case performance of the insertion sort.
    first_amounts = sorted(amounts[:i], reverse=True)
    counter = binary_search(first_amounts, -1)
    counters.append(counter)

plt.plot(lengths, counters)
plt.show()
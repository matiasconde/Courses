## 2. Sorting Arrays ##

import pandas as pd

df = pd.read_csv("amounts.csv")

amounts = list(df["Amount"])
times = list(df["Time"])

print(sum(amounts)/len(amounts))
               

## 3. Swapping Elements ##

def swap(array, pos1, pos2):
    first_value_stored = array[pos1]
    array[pos1] = array[pos2]
    array[pos2] = first_value_stored
    return array

first_amounts = amounts[:10]
first_amounts = swap(first_amounts,1,2)

## 4. Selection Sort ##

def minimo(array):
    minimo = array[0]
    min_index = 0
    for i,v in enumerate(array):
        if v<minimo:
            minimo = v
            min_index = i
    return [minimo,min_index]

def selection_sort(array):
    
    for i in range(len(array)):
        lowest_index = i
        for j in range(i,len(array)):
            if array[j] < array[lowest_index]:
                lowest_index = j
                
        swap(array,i,lowest_index)
        
    
first_amounts = amounts[:10] 
print(selection_sort(first_amounts))

## 5. Profiling The Selection Sort ##

import matplotlib.pyplot as plt

def selection_sort(array):
    counter = 0
    for i in range(len(array)):
        lowest_index = i
        
        for z in range(i, len(array)):
            counter += 1
            if array[z] < array[lowest_index]:
                lowest_index = z
        swap(array, lowest_index, i)
    return counter

lengths = [10,100,1000,10000]
counters = []
for length in lengths:
    first_amounts = amounts[:length]
    counters.append(selection_sort(first_amounts))
    
plt.plot(lengths,counters)
plt.show()

## 6. Bubble Sort ##

def bubble_sort(array):
    swaps = 1
    while swaps > 0:
        swaps = 0
        for i in range(len(array) -1):
            if array[i]>array[i+1]:
                swap(array,i,i+1)
                swaps += 1
            else: continue
first_amounts = amounts[:10]
print(bubble_sort(first_amounts))
               

## 7. Profiling The Bubble Sort ##

import matplotlib.pyplot as plt

def bubble_sort(array):
    counter = 0
    swaps = 1
    while swaps > 0:
        swaps = 0
        for i in range(len(array) - 1):
            counter += 1
            if array[i] > array[i+1]:
                swap(array, i, i+1)
                swaps += 1
    return counter

lengths = [10,100,1000,10000]
counters = []

for length in lengths: 
    first_amounts = amounts[:length]
    counters.append(bubble_sort(first_amounts))
    
plt.plot(lengths,counters)
plt.show()


## 9. Insertion Sort ##

def insertion_sort(array):
    for i in range(1,len(array)):
        j = i
        while j>0 and (array[j-1]>array[j]):
            swap(array,j-1,j)
            j -= 1
            
first_amounts = amounts[:10]
print(insertion_sort(first_amounts))

## 10. Profiling The Insertion Sort ##

import matplotlib.pyplot as plt

def insertion_sort(array):
    counter = 0
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j - 1] > array[j]:
            counter += 1
            swap(array, j, j-1)
            j-=1
    return counter

lengths = [10,100,1000,10000]
counters = []

for length in lengths: 
    first_amounts = amounts[:length]
    counters.append(insertion_sort(first_amounts))
    
plt.plot(lengths,counters)
plt.show()

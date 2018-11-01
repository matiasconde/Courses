## 1. The Range ##

import pandas as pd
houses = pd.read_table('AmesHousing_1.txt')
def range(array):
    return array.max()-array.min()

range_by_year = {}

for year in houses["Yr Sold"]:
    range_by_year[year] = range(houses.loc[houses["Yr Sold"] == year]["SalePrice"])
    
print(range_by_year)

one = False
two = True

## 2. The Average Distance ##

C = [1,1,1,1,1,1,1,1,1,21]

def average_distance(array):
    mean = sum(array)/len(array)
    distances = []
    for value in array:
        distances.append(value-mean)
    return sum(distances)/len(distances)    
    
avg_distance = average_distance(C)

print(avg_distance)

## 3. Mean Absolute Deviation ##

C = [1,1,1,1,1,1,1,1,1,21]

def average_distance(array):
    mean = sum(array)/len(array)
    distances = []
    for value in array:
        distances.append(abs(value-mean))
    return sum(distances)/len(distances)    
    
mad = average_distance(C)

print(mad)

## 4. Variance ##

C = [1,1,1,1,1,1,1,1,1,21]

def mean_squared_distance(array):
    mean = sum(array)/len(array)
    distances = []
    for value in array:
        distances.append((value-mean)**2)
    return sum(distances)/len(distances)    
    
variance_C = mean_squared_distance(C)

print(mean_squared_distance)

## 5. Standard Deviation ##

from math import sqrt
C = [1,1,1,1,1,1,1,1,1,21]

def standard_deviation(array):
    mean = sum(array)/len(array)
    distances = []
    for value in array:
        distances.append((value-mean)**2)
    return sqrt(sum(distances)/len(distances))    
    
standard_deviation_C = standard_deviation(C)

print(mean_squared_distance)

## 6. Average Variability Around the Mean ##

def standard_deviation(array):
    reference_point = sum(array) / len(array)
    
    distances = []
    for value in array:
        squared_distance = (value - reference_point)**2
        distances.append(squared_distance)
        
    variance = sum(distances) / len(distances)
    
    return sqrt(variance)

standard_deviations = {}

for year in houses["Yr Sold"]:
    array = houses[houses["Yr Sold"]==year]["SalePrice"]
    standard_deviations[year] = standard_deviation(array)
    
def keywithmaxval(d):
     """ a) create a list of the dict's keys and values; 
         b) return the key with the max value"""  
     v=list(d.values())
     k=list(d.keys())
     return k[v.index(max(v))]

def keywithminval(d):
     """ a) create a list of the dict's keys and values; 
         b) return the key with the max value"""  
     v=list(d.values())
     k=list(d.keys())
     return k[v.index(min(v))]

        
greatest_variability = keywithmaxval(standard_deviations)
lowest_variability = keywithminval(standard_deviations)


## 7. A Measure of Spread ##

sample1 = houses['Year Built'].sample(50, random_state = 1)
sample2 = houses['Year Built'].sample(50, random_state = 2)

def standard_deviation(array):
    reference_point = sum(array) / len(array)
    
    distances = []
    for value in array:
        squared_distance = (value - reference_point)**2
        distances.append(squared_distance)
    
    variance = sum(distances) / len(distances)
    
    return sqrt(variance)

bigger_spread = "sample 2"

st_dev1 = standard_deviation(sample1)
st_dev2 = standard_deviation(sample2)

print(st_dev1,st_dev2)





## 8. The Sample Standard Deviation ##

def standard_deviation(array):
    reference_point = sum(array) / len(array)
    
    distances = []
    for value in array:
        squared_distance = (value - reference_point)**2
        distances.append(squared_distance)
    
    variance = sum(distances) / len(distances)
    
    return sqrt(variance)

import matplotlib.pyplot as plt

standard_deviations = []

for i in range(5000):
    sample = houses["SalePrice"].sample(10,random_state=i)
    standard_deviations.append(standard_deviation(sample)) 

plt.hist(standard_deviations)
plt.axvline(standard_deviation(houses["SalePrice"]))
plt.show()

print(standard_deviation(houses["SalePrice"]))

## 9. Bessel's Correction ##

from math import sqrt
import matplotlib.pyplot as plt

def standard_deviation(array):
    mean = array.mean()
    diferences = []
    
    for value in array:
        diferences.append((value-mean)**2)
    
    return sqrt(sum(diferences)/(len(diferences)-1))

standard_deviations = []
for i in range(5000):
    sample = houses["SalePrice"].sample(10,random_state=i)
    stand_dev_sample = standard_deviation(sample)
    standard_deviations.append(stand_dev_sample)
    
plt.hist(standard_deviations)
plt.axvline(standard_deviation(houses["SalePrice"]))
plt.show()

## 10. Standard Notation ##

sample = houses.sample(100, random_state = 1)
from numpy import std, var

pandas_stdev = sample["SalePrice"].std(ddof=1)
numpy_stdev = numpy.std(sample["SalePrice"], ddof=1)
equal_stdevs = pandas_stdev == numpy_stdev

pandas_var = sample["SalePrice"].var(ddof=1)
numpy_var = numpy.var(sample["SalePrice"],ddof=1)
equal_vars = pandas_var == numpy_var

## 11. Sample Variance — Unbiased Estimator ##

import numpy

population = [0, 3, 6]

samples = [[0,3], [0,6],
           [3,0], [3,6],
           [6,0], [6,3]
          ]
lista1 = []
lista2 = []

for i in range(6):
    std = numpy.std(samples[i],ddof=1)
    lista1.append(std)
    var = numpy.var(samples[i],ddof=1)
    lista2.append(var)
    
equal_stdev = numpy.std(population,ddof=0) == numpy.mean(lista1)

equal_var = numpy.var(population,ddof=0) == numpy.mean(lista2)


    
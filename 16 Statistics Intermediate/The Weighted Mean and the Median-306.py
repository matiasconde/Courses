## 1. Introduction ##

mean_new = houses_per_year["Mean Price"].mean()

mean_original = houses["SalePrice"].mean()

difference = mean_original - mean_new

## 2. Different Weights ##

mean_original = houses["SalePrice"].mean().round(2)

prices = houses_per_year["Mean Price"].tolist()
sales = houses_per_year["Houses Sold"].tolist()

total=0
total_n_houses = 0

for i in range(len(prices)):
    total += prices[i]*sales[i]
    total_n_houses += sales[i]
    
weighted_mean = round(total/total_n_houses,2)
difference = mean_original-weighted_mean

## 3. The Weighted Mean ##

import numpy as np

def weighted_mean(values,weights):
    ponderate = values*weights
    total = ponderate.sum()
    total_sold = weights.sum()
    return total/total_sold

weighted_mean_numpy = np.average(a=houses_per_year["Mean Price"],weights=houses_per_year["Houses Sold"])

weighted_mean_function = weighted_mean(houses_per_year["Mean Price"],houses_per_year["Houses Sold"])

equal = weighted_mean_function == weighted_mean_numpy
    

## 4. The Median for Open-ended Distributions ##

distribution1 = [23, 24, 22, '20 years or lower,', 23, 42, 35]
distribution2 = [55, 38, 123, 40, 71]
distribution3 = [45, 22, 7, '5 books or lower', 32, 65, '100 books or more']

median1 = 23
median2 = 55
median3 = 32

## 5. Distributions with Even Number of Values ##

serie_auxiliar = houses['TotRms AbvGrd'].replace("10 or more",10)

s1 = serie_auxiliar.astype("int64")


s1.sort_values()
print(s1.shape)
print(s1[[1463]])
median = (s1[[1463]]+s1[[1462]])/2



## 6. The Median as a Resistant Statistic ##

houses["Lot Area"].plot.box()
houses["SalePrice"].plot.box()

mean_area = houses["Lot Area"].mean()
median_area = houses["Lot Area"].median()
print(mean_area,median_area)

mean_sale = houses["SalePrice"].mean()
median_sale = houses["SalePrice"].median()
print(mean_sale,median_sale)

lotarea_difference = mean_area-median_area
saleprice_difference = mean_sale-median_sale

## 7. The Median for Ordinal Scales ##

import matplotlib.pyplot as plt
mean = houses["Overall Cond"].mean()
median = houses["Overall Cond"].median()

houses["Overall Cond"].plot.hist()
plt.axvline(mean, label="Mean",color="r")
plt.axvline(median, label="Median",color="g")

plt.show()
print(mean,median)
more_representative = "mean"
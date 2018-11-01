## 1. Individual Values ##

import pandas as pd
houses = pd.read_table('AmesHousing_1.txt')

value = houses["SalePrice"].std(ddof=0)+houses["SalePrice"].mean()
houses["SalePrice"].plot.kde(xlim=(houses["SalePrice"].min(),houses["SalePrice"].max()))
plt.axvline(houses["SalePrice"].mean(),color="black",label="Mean")
plt.axvline(value,color="r",label="Standard deviation")
plt.axvline(220000,color="orange",label="220000")
plt.legend()
plt.show()

very_expensive = False


## 2. Number of Standard Deviations ##

distance = abs(houses["SalePrice"].mean() - 220000)

st_devs_away = distance / houses["SalePrice"].std(ddof=0)




## 3. Z-scores ##

min_val = houses['SalePrice'].min()
mean_val = houses['SalePrice'].mean()
max_val = houses['SalePrice'].max()

def z_score(value,array):
    return (value - array.mean()) / numpy.std(array)

min_z = z_score(min_val,houses["SalePrice"])
mean_z = z_score(mean_val,houses["SalePrice"])
max_z = z_score(max_val,houses["SalePrice"])





## 4. Locating Values in Different Distributions ##

def z_score(value, array, bessel = 0):
    mean = sum(array) / len(array)
    
    from numpy import std
    st_dev = std(array, ddof = bessel)
    
    distance = value - mean
    z = distance / st_dev
    
    return z

neighborhood = ["NAmes","CollgCr","Edwards","Somerst","OldTown"]
z_scores = {}

for neighbor in neighborhood:
    z_scores[neighbor] = abs(z_score(200000,houses[houses["Neighborhood"]==neighbor]["SalePrice"]))
    
v = list(z_scores.values())
k = list(z_scores.keys())

print(z_scores)

best_investment1 = k[v.index(min(v))]

print(best_investment1)

best_investment = "College Creek"


## 5. Transforming Distributions ##

mean = houses['SalePrice'].mean()
st_dev = houses['SalePrice'].std(ddof = 0)
houses['z_prices'] = houses['SalePrice'].apply(
    lambda x: ((x - mean) / st_dev)
    )

z_mean_price = houses["z_prices"].mean()
z_stdev_price = houses["z_prices"].std(ddof=0)

mean_area = houses["Lot Area"].mean()
stdev_area = houses["Lot Area"].std(ddof=0)

houses["z_area"] = houses["Lot Area"].apply(lambda x: (x - mean_area)/stdev_area)

z_mean_area = houses["z_area"].mean()
z_stdev_area = houses["z_area"].std(ddof=0)

print(z_mean_area,z_mean_price)
print(z_stdev_area,z_stdev_price)

houses["z_area"].plot.kde()
plt.axvline(z_mean_area)
plt.show()
houses["z_prices"].plot.kde()
plt.axvline(z_mean_price)
plt.show()




## 6. The Standard Distribution ##

from numpy import std, mean
population = [0,8,0,8]

mean1 = mean(population)
std_dev = std(population)
z_population = []

for v in population: 
    z_population.append((v - mean1)/std_dev)
    
mean_z = mean(z_population)
stdev_z = std(z_population)

## 7. Standardizing Samples ##

from numpy import std, mean
sample = [0,8,0,8]

x_bar = mean(sample)
s = std(sample, ddof = 1)

standardized_sample = []
for value in sample:
    z = (value - x_bar) / s
    standardized_sample.append(z)
    
stdev_sample = std(standardized_sample,ddof=1)

## 8. Using Standardization for Comparisons ##

mean_index1 = houses["index_1"].mean()
stdev_index1 = houses["index_2"].mean()

mean_index2 = houses["index_1"].std()
stdev_index2 = houses["index_2"].std()

houses["z_index_1"] = houses["index_1"].apply(lambda x: (x-mean_index1)/stdev_index1)
houses["z_index_2"] = houses["index_2"].apply(lambda x: (x-mean_index1)/stdev_index1)

print(houses["z_index_1"].head(2),houses["z_index_2"].head(2))

better = "first"

## 9. Converting Back from Z-scores ##

houses["z_merged_transf"] = houses["z_merged"]*10+50

mean_transformed = houses["z_merged_transf"].mean()
print(mean_transformed)

stdev_transformed = houses["z_merged_transf"].std(ddof=0)
print(stdev_transformed)
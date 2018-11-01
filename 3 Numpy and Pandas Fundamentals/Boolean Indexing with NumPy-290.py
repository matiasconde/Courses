## 1. Reading CSV files with NumPy ##

import numpy as np

taxi = np.genfromtxt("nyc_taxis.csv",delimiter=",",skip_header=1)


## 2. Boolean Arrays ##

a = np.array([1, 2, 3, 4, 5])
b = np.array(["blue", "blue", "red", "blue"])
c = np.array([80.0, 103.4, 96.9, 200.3])

a_bool = a < 3
b_bool = b == "blue"
c_bool = c > 100

print(a_bool)
print(b_bool)

## 3. Boolean Indexing with 1D ndarrays ##

pickup_month = taxi[:,1]

january_bool = pickup_month == 1
january = pickup_month[january_bool]
january_rides = january.shape[0]

february_bool = pickup_month == 2
february = pickup_month[february_bool]
february_rides = february.shape

march_bool = pickup_month == 3
march = pickup_month[march_bool]
march_rides = march.shape

print(march)




## 4. Boolean Indexing with 2D ndarrays ##

tip_amount = taxi[:,12]
tip_bool = tip_amount > 50
top_tips = taxi[tip_bool,5:14] # tip amounts of more than 50, and the columns from indexes 5 to 13 inclusive. Assign the resulting array to top_tips.

print(top_tips)





## 5. Assigning Values in ndarrays ##

# this creates a copy of our taxi ndarray
taxi_modified = taxi.copy()

taxi_modified[28214,5] = 1
taxi_modified[:,0] = 16
taxi_modified[[1800,1801],7] = taxi_modified[:,7].mean()

## 6. Assignment Using Boolean Arrays ##

# this creates a copy of our taxi ndarray
taxi_modified = taxi.copy()

# create a new column filled with `0`.
zeros = np.zeros([taxi_modified.shape[0], 1])
taxi_modified = np.concatenate([taxi, zeros], axis=1)
print(taxi_modified)

taxi_modified[(taxi_modified[:,5]==2)|(taxi_modified[:,5]==3)|(taxi_modified[:,5]==5),15] = 1
taxi_modified[~((taxi_modified[:,5]==2)|(taxi_modified[:,5]==3)|(taxi_modified[:,5]==5)),15] = 0


## 7. Challenge: Which is the most popular airport? ##

jfk = taxi[taxi[:,6]==2]
laguardia = taxi[taxi[:,6]==3]
newark = taxi[taxi[:,6]==5]

jfk_count = taxi[taxi[:,6]==2].shape[0]
laguardia_count = taxi[taxi[:,6]==3].shape[0]
newark_count = taxi[taxi[:,6]==5].shape[0]

## 8. Challenge: Calculating Statistics for Trips on Clean Data ##

trip_mph = taxi[:,7] / (taxi[:,8] / 3600)

cleaned_taxi = taxi[trip_mph<100]

mean_distance = cleaned_taxi[:,7].mean()
mean_length = cleaned_taxi[:,8].mean()
mean_total_amount = cleaned_taxi[:,13].mean()
mean_mph = (cleaned_taxi[:,7]/(cleaned_taxi[:,8] / 3600)).mean()
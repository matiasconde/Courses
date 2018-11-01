## 1. Recap ##

import pandas as pd

train_df = pd.read_csv("dc_airbnb_train.csv")
test_df = pd.read_csv("dc_airbnb_test.csv")


## 2. Hyperparameter optimization ##

from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
import numpy as np

hyper_params = np.arange(1,6)
features = ["accommodates","bedrooms","bathrooms","number_of_reviews"]
mse_values = []
for param in hyper_params: 
    knn = KNeighborsRegressor(algorithm="brute",n_neighbors=param)
    knn.fit(train_df[features],train_df["price"])
    predictions = knn.predict(test_df[features])
    mse_values.append(mean_squared_error(test_df["price"],predictions))
                      
print(mse_values)

## 3. Expanding grid search ##

from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
import numpy as np

hyper_params = np.arange(1,21)
features = ["accommodates","bedrooms","bathrooms","number_of_reviews"]
mse_values = []
for param in hyper_params: 
    knn = KNeighborsRegressor(algorithm="brute",n_neighbors=param)
    knn.fit(train_df[features],train_df["price"])
    predictions = knn.predict(test_df[features])
    mse_values.append(mean_squared_error(test_df["price"],predictions))
                      
print(mse_values)

## 4. Visualizing hyperparameter values ##

import matplotlib.pyplot as plt
%matplotlib inline

features = ['accommodates', 'bedrooms', 'bathrooms', 'number_of_reviews']
hyper_params = [x for x in range(1, 21)]
mse_values = list()

for hp in hyper_params:
    knn = KNeighborsRegressor(n_neighbors=hp, algorithm='brute')
    knn.fit(train_df[features], train_df['price'])
    predictions = knn.predict(test_df[features])
    mse = mean_squared_error(test_df['price'], predictions)
    mse_values.append(mse)
    
plt.scatter(hyper_params,mse_values)
plt.show()

## 5. Varying features and hyperparameters ##

hyper_params = [x for x in range(1,21)]
mse_values = list()
features = ['accommodates', 'bedrooms', 'bathrooms', 'beds',
       'minimum_nights', 'maximum_nights', 'number_of_reviews']

for param in hyper_params:
    knn = KNeighborsRegressor(algorithm="brute",n_neighbors=param)
    knn.fit(train_df[features],train_df["price"])
    predictions = knn.predict(test_df[features])
    mse_values.append(mean_squared_error(test_df["price"],predictions))

plt.scatter(hyper_params,mse_values)
plt.show()
   

## 6. Practice the workflow ##

two_features = ['accommodates', 'bathrooms']
three_features = ['accommodates', 'bathrooms', 'bedrooms']
hyper_params = [x for x in range(1,21)]
# Append the first model's MSE values to this list.
two_mse_values = list()
# Append the second model's MSE values to this list.
three_mse_values = list()
two_hyp_mse = dict()
three_hyp_mse = dict()

for param in hyper_params:
    knn = KNeighborsRegressor(algorithm="brute",n_neighbors=param)
    knn.fit(train_df[two_features],train_df["price"])
    predictions = knn.predict(test_df[two_features])
    two_mse_values.append(mean_squared_error(test_df["price"],predictions))

for param in hyper_params:
    knn = KNeighborsRegressor(algorithm="brute",n_neighbors=param)
    knn.fit(train_df[three_features],train_df["price"])
    predictions = knn.predict(test_df[three_features])
    three_mse_values.append(mean_squared_error(test_df["price"],predictions))

a = min(two_mse_values)
b = [i+1 for i,v in enumerate(two_mse_values) if min(two_mse_values)==v][0]
c = min(three_mse_values)
d = [i+1 for i,v in enumerate(three_mse_values) if min(three_mse_values)==v][0]

two_hyp_mse[b]=a
three_hyp_mse[d]=c

print(min(two_mse_values),min(three_mse_values))

print([i+1 for i,v in enumerate(two_mse_values) if min(two_mse_values)==v][0])

print([i+1 for i,v in enumerate(three_mse_values) if min(three_mse_values)==v][0])
## 2. Introduction To The Data ##

import pandas as pd

data = pd.read_csv("AmesHousing.txt",delimiter="\t")
train = data[:1460]
test = data[1460:]

print(data.info())

target = "SalePrice"

print(data.shape)





## 3. Simple Linear Regression ##

import matplotlib.pyplot as plt
# For prettier plots.
import seaborn as sns

plt.scatter(data["Garage Area"],data["SalePrice"], color="black")
plt.scatter(data["Gr Liv Area"],data["SalePrice"],color="green")
plt.scatter(data["Overall Cond"],data["SalePrice"],color="orange")
plt.show()


## 5. Using Scikit-Learn To Train And Predict ##

from sklearn.linear_model import LinearRegression

lm = LinearRegression()

lm.fit(train[["Gr Liv Area"]],train["SalePrice"])
a1, a0 = lm.coef_, lm.intercept_

       

## 6. Making Predictions ##

import numpy as np
from sklearn.metrics import mean_squared_error

lr = LinearRegression()
lr.fit(train[['Gr Liv Area']], train['SalePrice'])

predictions1 = lr.predict(train[["Gr Liv Area"]]) 
predictions2 = lr.predict(test[["Gr Liv Area"]])

train_rmse = (mean_squared_error(train["SalePrice"],predictions1))**0.5

test_rmse = (mean_squared_error(test["SalePrice"],predictions2))**0.5



## 7. Multiple Linear Regression ##

cols = ['Overall Cond', 'Gr Liv Area']

lr = LinearRegression()
lr.fit(train[cols],train["SalePrice"])

predictions1 = lr.predict(train[cols])
predictions2 = lr.predict(test[cols])

train_rmse_2 = (mean_squared_error(train["SalePrice"],predictions1))**0.5
test_rmse_2 = (mean_squared_error(test["SalePrice"],predictions2))**0.5

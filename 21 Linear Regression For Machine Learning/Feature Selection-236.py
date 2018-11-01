## 1. Missing Values ##

import pandas as pd
data = pd.read_csv('AmesHousing.txt', delimiter="\t")
train = data[0:1460]
test = data[1460:]

cols_to_drop = ["PID","Year Built","Year Remod/Add","Garage Yr Blt","Mo Sold","Yr Sold"]

numerical_train = train.select_dtypes(include=["int","float"])
numerical_train = numerical_train.drop(columns=cols_to_drop)
   
null_series = numerical_train.isnull().sum()
full_cols_series = null_series.loc[null_series==0]
print(full_cols_series)

## 2. Correlating Feature Columns With Target Column ##

train_subset = train[full_cols_series.index]

correlations = train_subset.corr()

sorted_corrs = abs(correlations["SalePrice"]).sort_values()

print(sorted_corrs)

## 3. Correlation Matrix Heatmap ##

import seaborn as sns
import matplotlib.pyplot as plt

strong_corrs = sorted_corrs.loc[sorted_corrs>0.3].index
data = train_subset[strong_corrs].corr()
sns.heatmap(data)
plt.show()

## 4. Train And Test Model ##

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np

final_corr_cols = strong_corrs.drop(['Garage Cars', 'TotRms AbvGrd'])
features = final_corr_cols.drop(['SalePrice']).index
target = 'SalePrice'

clean_train = train[final_corr_cols.index]
clean_test = test[final_corr_cols.index].dropna()

lr = LinearRegression()
lr.fit(clean_train[features],clean_train["SalePrice"])

predictions1 = lr.predict(clean_train[features])
predictions2 = lr.predict(clean_test[features])

train_rmse = mean_squared_error(clean_train["SalePrice"],predictions1)**0.5
test_rmse = mean_squared_error(clean_test["SalePrice"],predictions2)**0.5

## 5. Removing Low Variance Features ##

features_data = train[features]

for column in features_data.columns:
    features_data[column] = (features_data[column] - features_data[column].min()) / (features_data[column].max()-features_data[column].min()) 
    
sorted_vars = features_data.var().sort_values()

print(sorted_vars)

## 6. Final Model ##

final_features = sorted_vars.drop("Open Porch SF").index

lr = LinearRegression()
lr.fit(clean_train[final_features],clean_train["SalePrice"])

predictions1 = lr.predict(clean_train[final_features])
predictions2 = lr.predict(clean_test[final_features])

train_rmse_2 = mean_squared_error(clean_train["SalePrice"],predictions1)**0.5

test_rmse_2 = mean_squared_error(clean_test["SalePrice"],predictions2)**0.5

print(train_rmse_2)
print(test_rmse_2)
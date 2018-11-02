## 1. Introduction ##

import numpy as np
import pandas as pd

dc_listings = pd.read_csv("dc_airbnb.csv")
stripped_commas = dc_listings['price'].str.replace(',', '')
stripped_dollars = stripped_commas.str.replace('$', '')
dc_listings['price'] = stripped_dollars.astype('float')

df = dc_listings.iloc[np.random.permutation(dc_listings.index)]

split_one = df.iloc[:1862]
split_two = df.iloc[1862:]

print(split_one.shape,split_two.shape)


## 2. Holdout Validation ##

from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error

train_one = split_one
test_one = split_two
train_two = split_two
test_two = split_one

knn = KNeighborsRegressor()

knn.fit(train_one[["accommodates"]], train_one["price"])
predictions_one = knn.predict(test_one[["accommodates"]])

iteration_one_rmse = (mean_squared_error(test_one[["price"]],predictions_one))**0.5

knn.fit(train_two[["accommodates"]],train_two["price"])

predictions_two = knn.predict(test_two[["accommodates"]])

iteration_two_rmse = (mean_squared_error(test_two["price"],predictions_two))**0.5

avg_rmse = np.mean([iteration_one_rmse,iteration_two_rmse])

## 3. K-Fold Cross Validation ##

parts = [0,745,1490,2234,2978,3723]

for i in range(1,6):
    dc_listings.loc[dc_listings.index[parts[i-1]:parts[i]],"fold"] = i
    
print(dc_listings['fold'].value_counts(dropna=False))
print("\n Num of missing values: ", dc_listings['fold'].isnull().sum())

## 4. First iteration ##

from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error

knn = KNeighborsRegressor()

train_df = dc_listings.loc[(dc_listings["fold"]==2)|(dc_listings["fold"]==3)|(dc_listings["fold"]==4)|(dc_listings["fold"]==5)]

test_df = dc_listings.loc[dc_listings["fold"]==1]

knn.fit(train_df[["accommodates"]],train_df["price"])

labels = knn.predict(test_df[["accommodates"]])

iteration_one_rmse = mean_squared_error(test_df["price"],labels)**0.5



## 5. Function for training models ##

# Use np.mean to calculate the mean.
import numpy as np
fold_ids = [1,2,3,4,5]

def train_and_validate(df,fold_ids):
    rmse_values = []
    for i in range(1,len(fold_ids)+1):
        folds_for_train = [j for j in fold_ids if i!=j]
        knn = KNeighborsRegressor()
        frames = []
        for k in folds_for_train:
            frames.append(dc_listings.loc[dc_listings["fold"]==k])
        train_df = pd.concat(frames)
        test_df = dc_listings.loc[dc_listings["fold"]==i]
        
        knn.fit(train_df[["accommodates"]],train_df["price"])
        predictions = knn.predict(test_df[["accommodates"]])
        
        rmse_values.append(mean_squared_error(test_df["price"],predictions)**0.5)
    return rmse_values

rmses = train_and_validate(dc_listings,fold_ids)
print(rmses)
avg_rmse = np.mean(rmses)
print(avg_rmse)
    

## 6. Performing K-Fold Cross Validation Using Scikit-Learn ##

from sklearn.model_selection import cross_val_score, KFold
from sklearn.metrics import mean_squared_error
from sklearn.metrics import make_scorer
from sklearn.neighbors import KNeighborsRegressor

kf = KFold(5,shuffle=True,random_state=1)
knn = KNeighborsRegressor()
mses = cross_val_score(knn,dc_listings[["accommodates"]],dc_listings["price"],scoring=make_scorer(mean_squared_error),cv=kf)

rmses = [(abs(j))**0.5 for j in mses]
avg_rmse = np.mean(rmses)

## 7. Exploring Different K Values ##

from sklearn.model_selection import cross_val_score, KFold

num_folds = [3, 5, 7, 9, 10, 11, 13, 15, 17, 19, 21, 23]

for fold in num_folds:
    kf = KFold(fold, shuffle=True, random_state=1)
    model = KNeighborsRegressor()
    mses = cross_val_score(model, dc_listings[["accommodates"]], dc_listings["price"], scoring="neg_mean_squared_error", cv=kf)
    rmses = np.sqrt(np.absolute(mses))
    avg_rmse = np.mean(rmses)
    std_rmse = np.std(rmses)
    print(str(fold), "folds: ", "avg RMSE: ", str(avg_rmse), "std RMSE: ", str(std_rmse))
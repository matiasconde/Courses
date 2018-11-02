## 1. Introduction ##

import pandas as pd
columns = ["mpg", "cylinders", "displacement", "horsepower", "weight", "acceleration", "model year", "origin", "car name"]
cars = pd.read_table("auto-mpg.data", delim_whitespace=True, names=columns)
filtered_cars = cars[cars['horsepower'] != '?'].copy()
filtered_cars['horsepower'] = filtered_cars['horsepower'].astype('float')

print(cars.head())

## 3. Bias-variance tradeoff ##

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np
import matplotlib.pyplot as plt

def train_and_test(cols):
    model = LinearRegression()
    model.fit(filtered_cars[cols],filtered_cars["mpg"])
    predictions = model.predict(filtered_cars[cols])
    variance = np.var(predictions)
    mse = mean_squared_error(predictions,filtered_cars["mpg"])
    return(mse,variance)
    
cyl_mse, cyl_var = train_and_test(["cylinders"])

weight_mse, weight_var = train_and_test(["weight"])

## 4. Multivariate models ##

# Our implementation for train_and_test, takes in a list of strings.
def train_and_test(cols):
    # Split into features & target.
    features = filtered_cars[cols]
    target = filtered_cars["mpg"]
    # Fit model.
    lr = LinearRegression()
    lr.fit(features, target)
    # Make predictions on training set.
    predictions = lr.predict(features)
    # Compute MSE and Variance.
    mse = mean_squared_error(filtered_cars["mpg"], predictions)
    variance = np.var(predictions)
    return(mse, variance)

features = ["cylinders","displacement","horsepower", "weight", "acceleration", "model year", "origin"]
lista = []
for i in range(len(features)):
    lista.append(train_and_test(features[:i+1]))

tupla = tuple(lista)
((one_mse,one_var),(two_mse,two_var),(three_mse,three_var),(four_mse,four_var),(five_mse,five_var),(six_mse,six_var),(seven_mse,seven_var)) = tupla

## 5. Cross validation ##

from sklearn.model_selection import cross_val_score, KFold
from sklearn.metrics import mean_squared_error, make_scorer
import numpy as np

def train_and_cross_val(cols):
    kf = KFold(n_splits=10, shuffle=True, random_state=3)
    lr = LinearRegression()
    features = filtered_cars[cols]
    target = filtered_cars["mpg"]
    
    mses = []
    var = []
    
    for train_interval,test_interval in kf.split(features):
        X_train, X_test = features.iloc[train_interval], features.iloc[test_interval]
        y_train, y_test = target.iloc[train_interval], target.iloc[test_interval]
        lr.fit(X_train,y_train)
        predictions = lr.predict(X_test)
    
        mses.append(mean_squared_error(y_test,predictions))
        var.append(np.var(predictions))
    
        avg_mse = np.mean(mses)
        avg_var = np.mean(var)
   
    
    return (avg_mse,avg_var)

columns = ["cylinders","displacement","horsepower", "weight", "acceleration", "model year", "origin"]

lista = []

for i in range(len(columns)-1):
    lista.append(train_and_cross_val(columns[:i+2]))

tupla = tuple(lista)

((two_mse,two_var),(three_mse,three_var),(four_mse,four_var),(five_mse,five_var),(six_mse,six_var),(seven_mse,seven_var)) = tupla


## 6. Plotting cross-validation error vs. cross-validation variance ##

from sklearn.model_selection import cross_val_score, KFold
from sklearn.metrics import mean_squared_error, make_scorer
import numpy as np
import matplotlib.pyplot as plt

def train_and_cross_val(cols):
    kf = KFold(n_splits=10, shuffle=True, random_state=3)
    lr = LinearRegression()
    features = filtered_cars[cols]
    target = filtered_cars["mpg"]
    
    mses = []
    var = []
    
    for train_interval,test_interval in kf.split(features):
        X_train, X_test = features.iloc[train_interval], features.iloc[test_interval]
        y_train, y_test = target.iloc[train_interval], target.iloc[test_interval]
        lr.fit(X_train,y_train)
        predictions = lr.predict(X_test)
    
        mses.append(mean_squared_error(y_test,predictions))
        var.append(np.var(predictions))
    
        avg_mse = np.mean(mses)
        avg_var = np.mean(var)
   
    
    return (avg_mse,avg_var)
"""
columns = ["cylinders","displacement","horsepower", "weight", "acceleration", "model year", "origin"]

lista = []

for i in range(len(columns)-1):
    lista.append(train_and_test(columns[:i+2]))

tupla = tuple(lista)

((two_mse,two_var),(three_mse,three_var),(four_mse,four_var),(five_mse,five_var),(six_mse,six_var),(seven_mse,seven_var)) = tupla

y_values1 = [two_mse,three_mse,four_mse,five_mse,six_mse,seven_mse]
y_values2 = [two_var,three_var,four_var,five_var,six_var,seven_var]
x_values1 = np.arange(2,8)

plt.scatter(x_values1,y_values1,c="red")
plt.scatter(x_values1,y_values2,c="blue")
plt.show()
"""
# We've hidden the `train_and_cross_val` function to save space but you can still call the function!
import matplotlib.pyplot as plt
        
two_mse, two_var = train_and_cross_val(["cylinders", "displacement"])
three_mse, three_var = train_and_cross_val(["cylinders", "displacement", "horsepower"])
four_mse, four_var = train_and_cross_val(["cylinders", "displacement", "horsepower", "weight"])
five_mse, five_var = train_and_cross_val(["cylinders", "displacement", "horsepower", "weight", "acceleration"])
six_mse, six_var = train_and_cross_val(["cylinders", "displacement", "horsepower", "weight", "acceleration", "model year"])
seven_mse, seven_var = train_and_cross_val(["cylinders", "displacement", "horsepower", "weight", "acceleration","model year", "origin"])
plt.scatter([2,3,4,5,6,7], [two_mse, three_mse, four_mse, five_mse, six_mse, seven_mse], c='red')
plt.scatter([2,3,4,5,6,7], [two_var, three_var, four_var, five_var, six_var, seven_var], c='blue')
plt.show()
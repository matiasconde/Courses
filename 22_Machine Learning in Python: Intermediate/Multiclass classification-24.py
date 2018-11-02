## 1. Introduction to the data ##

import pandas as pd
cars = pd.read_csv("auto.csv")

unique_regions = cars["origin"].unique()
print(unique_regions)

## 2. Dummy variables ##

dummy_cylinders = pd.get_dummies(cars["cylinders"], prefix="cyl")
cars = pd.concat([cars, dummy_cylinders], axis=1)

dummy_years = pd.get_dummies(cars["year"], prefix="year")
cars = pd.concat([cars,dummy_years], axis=1)
cars.drop(labels=["year","cylinders"],axis=1,inplace=True)
print(cars.head())

## 3. Multiclass classification ##

shuffled_rows = np.random.permutation(cars.index)
shuffled_cars = cars.iloc[shuffled_rows]


train = shuffled_cars[:int(0.7*cars.shape[0])]
test = shuffled_cars[int(0.7*cars.shape[0]):]

print(test)

## 4. Training a multiclass logistic regression model ##

from sklearn.linear_model import LogisticRegression

unique_origins = cars["origin"].unique()
unique_origins.sort()

models = {}

features = list(dummy_cylinders.columns) + list(dummy_years.columns)

for origin in unique_origins:
    X = train[features]
    Y = train["origin"]==origin
    logistic_model = LogisticRegression()
    logistic_model.fit(X,Y)
    models[origin]=logistic_model

## 5. Testing the models ##

testing_probs = pd.DataFrame(columns=unique_origins)

for origin in unique_origins:
    testing_probs[origin] = models[origin].predict_proba(test[features])[:,1]
    




## 6. Choose the origin ##

predicted_origins = testing_probs.idxmax(axis=1)
print(predicted_origins)
## 2. Introduction to the data ##

import pandas as pd

dc_listings = pd.read_csv("dc_airbnb.csv")

print(dc_listings.head(1))

## 4. Euclidean distance ##

import numpy as np

first_distance = abs(dc_listings["accommodates"][0]-3)

## 5. Calculate distance for all observations ##

def distances(value):
    return abs(value-3)

dc_listings["distance"] = dc_listings["accommodates"].apply(distances)

print(dc_listings["distance"].value_counts())

## 6. Randomizing, and sorting ##

import numpy as np
np.random.seed(1)

shuffled_index = np.random.permutation(dc_listings.index)

dc_listings = dc_listings.loc[shuffled_index,:].sort_values(by="distance")

print(dc_listings["price"].head(10))

## 7. Average price ##

stripped_commas = dc_listings["price"].str.replace(",","")
stripped_dollars = stripped_commas.str.replace("$","")
stripped_dollars = stripped_dollars.astype(float)

dc_listings["price"] = stripped_dollars

mean_price = dc_listings["price"].head(5).mean()

print(mean_price)

## 8. Function to make predictions ##

# Brought along the changes we made to the `dc_listings` Dataframe.
dc_listings = pd.read_csv('dc_airbnb.csv')
stripped_commas = dc_listings['price'].str.replace(',', '')
stripped_dollars = stripped_commas.str.replace('$', '')
dc_listings['price'] = stripped_dollars.astype('float')
dc_listings = dc_listings.loc[np.random.permutation(len(dc_listings))]

def predict_price(new_listing):
    temp_df = dc_listings.copy()
    temp_df["distance"] = abs(temp_df["accommodates"]-new_listing)
    mean = temp_df.sort_values(by="distance")["price"].head(5).mean()
    return mean

acc_one = predict_price(1)
acc_two = predict_price(2)
acc_four = predict_price(4)
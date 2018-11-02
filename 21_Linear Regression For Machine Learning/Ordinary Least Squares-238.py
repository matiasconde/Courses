## 1. Introduction ##

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('AmesHousing.txt', delimiter="\t")
train = data[0:1460]
test = data[1460:]

features = ['Wood Deck SF', 'Fireplaces', 'Full Bath', '1st Flr SF', 'Garage Area',
       'Gr Liv Area', 'Overall Qual']

X = train[features]
y = train["SalePrice"]
X_np = np.asarray(train[features])
y_np = np.asarray(train["SalePrice"])
cuenta1 = np.transpose(X_np)
cuenta2 = np.dot(cuenta1,X_np)
cuenta3 = np.linalg.inv(cuenta2)
cuenta4 = np.dot(cuenta3,cuenta1)
a = np.dot(cuenta4,y_np)

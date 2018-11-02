## 1. Introduction ##

import pandas as pd

data = pd.read_csv('AmesHousing.txt', delimiter="\t")
train = data[0:1460]
test = data[1460:]

train_null_counts = train.isnull().sum()
features_not_null = train_null_counts[train_null_counts==0].index
print(train_null_counts==0)
df_no_mv = train[features_not_null]

## 2. Categorical Features ##

text_cols = df_no_mv.select_dtypes(include=['object']).columns

for col in text_cols:
    print(col+":", len(train[col].unique()))
    
for column in text_cols:
    train[column] = train[column].astype("category")
    
print(train["Utilities"].cat.codes.value_counts())

## 3. Dummy Coding ##

dummy_cols = pd.DataFrame()

for column in text_cols:
    dummies = pd.get_dummies(train[column])
    train = pd.concat([train,dummies],axis=1)

train.drop(text_cols,inplace=True,axis=1)

## 4. Transforming Improper Numerical Features ##

train["years_until_remod"] = train["Year Remod/Add"] - train["Year Built"]


## 5. Missing Values ##

import pandas as pd

data = pd.read_csv('AmesHousing.txt', delimiter="\t")
train = data[0:1460]
test = data[1460:]

train_null_counts = train.isnull().sum()


interested_missing_values = train_null_counts[(train_null_counts>0)&(train_null_counts<584)].index

df_missing_values = train[interested_missing_values]
print(df_missing_values.isnull().sum())

print(df_missing_values.dtypes)

## 6. Imputing Missing Values ##

float_cols = df_missing_values.select_dtypes(include=['float'])

float_cols = float_cols.fillna(float_cols.mean())
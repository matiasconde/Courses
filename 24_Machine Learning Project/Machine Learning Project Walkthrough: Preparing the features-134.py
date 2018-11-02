## 1. Recap ##

import pandas as pd

loans = pd.read_csv("filtered_loans_2007.csv")
null_counts = loans.isnull().sum()

print(null_counts)

## 2. Handling missing values ##

loans.drop(labels=["pub_rec_bankruptcies"],inplace=True,axis=1)

loans.dropna(how="any",axis=0,inplace=True)

print(loans.dtypes.value_counts())



## 3. Text columns ##

object_columns_df = loans.select_dtypes(include="object")

print(object_columns_df[0:2])

## 5. First 5 categorical columns ##

cols = ['home_ownership', 'verification_status', 'emp_length', 'term', 'addr_state']
for c in cols:
    print(loans[c].value_counts())

## 6. The reason for the loan ##

print(loans["purpose"].value_counts())
print(loans["title"].value_counts())

## 7. Categorical columns ##

mapping_dict = {
    "emp_length": {
        "10+ years": 10,
        "9 years": 9,
        "8 years": 8,
        "7 years": 7,
        "6 years": 6,
        "5 years": 5,
        "4 years": 4,
        "3 years": 3,
        "2 years": 2,
        "1 year": 1,
        "< 1 year": 0,
        "n/a": 0
    }
}

loans.drop(labels=["last_credit_pull_d","addr_state","title","earliest_cr_line"],axis=1,inplace=True)

loans["int_rate"] = loans["int_rate"].str.rstrip("%").astype(float)

loans["revol_util"] = loans["revol_util"].str.rstrip("%").astype(float)

loans.replace(to_replace=mapping_dict,inplace=True)





## 8. Dummy variables ##

df_dummies = pd.get_dummies(loans[["home_ownership","verification_status","purpose","term"]])

loans.drop(labels=["home_ownership","verification_status","purpose","term"],axis=1,inplace=True)

loans = pd.concat([loans,df_dummies],axis=1)


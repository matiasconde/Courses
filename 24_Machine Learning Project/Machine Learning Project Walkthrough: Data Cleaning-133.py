## 3. Reading in to Pandas ##

import pandas as pd

loans_2007 = pd.read_csv("loans_2007.csv")

print(loans_2007.head(1))
print(loans_2007.shape)

## 5. First group of columns ##


features_to_drop = ["id","member_id","funded_amnt","funded_amnt_inv","grade","sub_grade","emp_title","issue_d"]

loans_2007.drop(labels=features_to_drop,inplace=True,axis="columns")


## 7. Second group of features ##

features_to_remove2 = ["zip_code","out_prncp","out_prncp_inv","total_pymnt","total_pymnt_inv","total_rec_prncp"]

loans_2007.drop(labels=features_to_remove2,axis="columns",inplace=True)

## 9. Third group of features ##

features_to_drop3 = ["total_rec_int","total_rec_late_fee","recoveries","collection_recovery_fee","last_pymnt_d","last_pymnt_amnt"]

loans_2007.drop(labels=features_to_drop3,axis="columns",inplace=True)

print(loans_2007.head(1))
print(loans_2007.shape[1])

## 10. Target column ##

print(loans_2007["loan_status"].value_counts())

## 12. Binary classification ##

loans_2007 = loans_2007.loc[(loans_2007["loan_status"]=="Fully Paid")|(loans_2007["loan_status"]=="Charged Off")]

mapping_dict = {"loan_status":{"Fully Paid":1,"Charged Off":0}}

loans_2007.replace(to_replace=mapping_dict,inplace=True)

## 13. Removing single value columns ##

drop_columns = []

for column in loans_2007.columns:
    serie = loans_2007[column]
    serie.dropna(inplace=True)
    uniques = serie.unique()
    if len(uniques)<=1:
        drop_columns.append(column)
        
loans_2007.drop(labels=drop_columns,axis=1,inplace=True)

print(drop_columns)

    
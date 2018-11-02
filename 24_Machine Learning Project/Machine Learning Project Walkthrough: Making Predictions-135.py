## 1. Recap ##

import pandas as pd

loans = pd.read_csv("cleaned_loans_2007.csv")

print(loans.info())

## 3. Picking an error metric ##

import pandas as pd

tn = ((predictions==0)&(loans["loan_status"]==0)).sum()

tp = ((predictions==1)&(loans["loan_status"]==1)).sum()

fp = ((predictions==1)&(loans["loan_status"]==0)).sum()

fn = ((predictions==0)&(loans["loan_status"]==1)).sum()



## 5. Class imbalance ##

import pandas as pd
import numpy

# Predict that all loans will be paid off on time.
predictions = pd.Series(numpy.ones(loans.shape[0]))

tn = ((predictions==0)&(loans["loan_status"]==0)).sum()

tp = ((predictions==1)&(loans["loan_status"]==1)).sum()

fp = ((predictions==1)&(loans["loan_status"]==0)).sum()

fn = ((predictions==0)&(loans["loan_status"]==1)).sum()

fpr = fp / (fp + tn)

tpr = tp / (tp + fn)

print(fpr,tpr)

## 6. Logistic Regression ##

from sklearn.linear_model import LogisticRegression

features = loans.drop("loan_status",axis=1)
target = loans["loan_status"]

lr = LogisticRegression()
lr.fit(features,target)
predictions = lr.predict(features)

## 7. Cross Validation ##

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_predict
lr = LogisticRegression()

predictions = cross_val_predict(lr,features,target,cv=3)

predictions = pd.Series(predictions)

tp = ((predictions==1)&(target==1)).sum()
tn = ((predictions==0)&(target==0)).sum()
fp = ((predictions==1)&(target==0)).sum()
fn = ((predictions==0)&(target==1)).sum()

tpr = tp / (tp + fn)

fpr = fp / (fp + tn)

print(fpr,tpr)

## 9. Penalizing the classifier ##

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_predict

lr = LogisticRegression(class_weight = "balanced")

predictions = cross_val_predict(lr,features,target,cv=3)

predictions = pd.Series(predictions)

tp = ((predictions==1)&(target==1)).sum()
tn = ((predictions==0)&(target==0)).sum()
fp = ((predictions==1)&(target==0)).sum()
fn = ((predictions==0)&(target==1)).sum()

tpr = tp / (tp + fn)

fpr = fp / (fp + tn)

print(fpr,tpr)

## 10. Manual penalties ##

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_predict

penalty = {0: 10,1:1}

lr = LogisticRegression(class_weight=penalty)

predictions = cross_val_predict(lr,features,target,cv=3)

predictions = pd.Series(predictions)

tp = ((predictions==1)&(target==1)).sum()
tn = ((predictions==0)&(target==0)).sum()
fp = ((predictions==1)&(target==0)).sum()
fn = ((predictions==0)&(target==1)).sum()

tpr = tp / (tp + fn)

fpr = fp / (fp + tn)

print(fpr,tpr)

## 11. Random forests ##

from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import cross_val_predict

rf = RandomForestClassifier(random_state=1,class_weight="balanced")

predictions = cross_val_predict(rf,features,target,cv=3)

predictions = pd.Series(predictions)

tp = ((predictions==1)&(target==1)).sum()
tn = ((predictions==0)&(target==0)).sum()
fp = ((predictions==1)&(target==0)).sum()
fn = ((predictions==0)&(target==1)).sum()

tpr = tp / (tp + fn)

fpr = fp / (fp + tn)

print(fpr,tpr)
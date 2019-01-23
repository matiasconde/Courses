## 2. Introduction ##

import pandas as pd

moma = pd.read_csv('moma.csv')
moma.info()

## 3. How Pandas Represents Values in a Dataframe ##

['import pandas as pd\nmoma = pd.read_csv("moma.csv")\n\nprint(moma._data)\n']

## 5. Different Types Have Different Memory Footprints ##


size = moma.size

total_bytes = size*8


total_megabytes = total_bytes/(1024*1024)

print(total_bytes, " ", total_megabytes)


## 7. Calculating the True Memory Footprint ##

obj_cols = moma.select_dtypes(include=['object'])

obj_cols_mem = obj_cols.memory_usage(deep='True')

obj_cols_sum = obj_cols_mem.sum() / (1024*1024)

print(obj_cols_sum)

## 9. Optimizing Integer Columns With Subtypes ##

import numpy as np

moma["ExhibitionSortOrder"].describe()
print(np.iinfo('int16'))

moma["ExhibitionSortOrder"] = moma["ExhibitionSortOrder"].astype('int16',inplace=True)

print(moma["ExhibitionSortOrder"].dtypes)
print(moma["ExhibitionSortOrder"].memory_usage(deep=True))

## 10. Optimizing Float Columns With Subtypes ##

moma = pd.read_csv("moma.csv")
moma['ExhibitionSortOrder'] = moma['ExhibitionSortOrder'].astype("int16")
float_cols = list(moma.select_dtypes(include=['float']).columns)

for col in float_cols:
    moma[col] = pd.to_numeric(moma[col],downcast='float')

print(moma[float_cols].dtypes)


## 12. Converting To DateTime ##

moma["ExhibitionBeginDate"] = pd.to_datetime(moma["ExhibitionBeginDate"])
moma["ExhibitionEndDate"] = pd.to_datetime(moma["ExhibitionEndDate"])

moma["ExhibitionBeginDate"].memory_usage(deep=True)
moma["ExhibitionEndDate"].memory_usage(deep=True)




## 14. Converting to Categorical to Save Memory ##

obj_cols = moma.select_dtypes(include=['object']).columns

cantFilas = moma.shape[0]

for col in obj_cols: 
    if len(moma[col].unique()) < cantFilas:
        moma[col] = moma[col].astype('category')
        
print(moma.info(memory_usage='deep'))

## 15. Selecting Types While Reading the Data In ##

keep_cols = ['ExhibitionID', 'ExhibitionNumber', 'ExhibitionBeginDate', 'ExhibitionEndDate', 'ExhibitionSortOrder', 'ExhibitionRole', 'ConstituentType', 'DisplayName', 'Institution', 'Nationality', 'Gender']
moma = pd.read_csv("moma.csv", parse_dates=["ExhibitionBeginDate", "ExhibitionEndDate"], usecols=keep_cols)
print(moma.memory_usage(deep=True).sum()/(1024*1024))

                   
                   
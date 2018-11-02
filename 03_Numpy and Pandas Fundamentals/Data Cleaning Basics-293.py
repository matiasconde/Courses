## 1. Reading CSV Files with Encodings ##

import pandas as pd

laptops = pd.read_csv("laptops.csv",encoding = "Windows_1251")

laptops.info()

## 2. Cleaning Column Names ##


def clean_label(col):
    col = col.strip()
    
    col = col.replace("Operating System","os")
    col = col.replace(" ","_")
    col = col.replace("(","")
    col = col.replace(")","")
    col = col.lower()
   
    return col

laptops.columns = [clean_label(col) for col in laptops.columns]


## 3. Converting String Columns to Numeric ##

laptops["screen_size"] = laptops["screen_size"].str.replace('"','').astype(float)
laptops.rename({"screen_size": "screen_size_inches"}, axis=1, inplace=True)

laptops["ram"] = laptops.loc[:,"ram"].str.replace("GB","").astype(int)

laptops.rename({"ram":"ram_gb"},axis=1,inplace=True)

dtypes = laptops.dtypes

## 4. Practicing Converting String Columns to Numeric ##

laptops["weight"] = laptops["weight"].str.strip()
laptops["weight"] = laptops["weight"].str.replace("s","")
laptops["weight"] = laptops["weight"].str.replace("kg","")
laptops["weight"] = laptops["weight"].astype(float)


laptops["price_euros"] = laptops["price_euros"].str.strip()
laptops["price_euros"] = laptops["price_euros"].str.replace(",",".")
laptops["price_euros"] = laptops["price_euros"].astype(float)

laptops.rename({"weight":"weight_kg"},axis=1,inplace=True)

weight_describe = laptops["weight_kg"].describe()
price_describe = laptops["price_euros"].describe()




## 5. Extracting Values from the Start of Strings ##

laptops["gpu_manufacturer"] = (laptops["gpu"]
                                    .str.split(n=1,expand=True)
                                    .iloc[:,0]
                               )

laptops["cpu_manufacturer"] = laptops.loc[:,"cpu"].str.split(" ",n=2,expand=True).iloc[:,0]



## 6. Extracting Values from the End of Strings ##

screen_res = laptops["screen"].str.rsplit(n=1, expand=True)
screen_res.columns = ["A", "B"]
screen_res.loc[screen_res["B"].isnull(), "B"] = screen_res["A"]
laptops["screen_resolution"] = (screen_res["B"]
                                    .str.split(n=1,expand=True)
                                    .iloc[:,0]
                               )

laptops["cpu_speed_ghz"] = laptops.loc[:,"cpu"].str.replace("GHz","")
laptops["cpu_speed_ghz"] = laptops["cpu_speed_ghz"].str.rsplit(" ",n=1,expand=True).iloc[:,1].astype(float)


## 7. Correcting Bad Values ##

mapping_dict = {
    'Android': 'Android',
    'Chrome OS': 'Chrome OS',
    'Linux': 'Linux',
    'Mac OS': 'macOS',
    'No OS': 'No OS',
    'Windows': 'Windows',
    'macOS': 'macOS'
}

laptops["os"] = laptops["os"].map(mapping_dict)

## 8. Dropping Missing Values ##

laptops_no_null_rows = laptops.dropna(axis=0)
laptops_no_null_cols = laptops.dropna(axis=1)

## 9. Filling Missing Values ##

value_counts_before = laptops.loc[laptops["os_version"].isnull(), "os"].value_counts()
laptops.loc[laptops["os"] == "macOS", "os_version"] = "X"

laptops.loc[laptops["os"] == "No OS","os_version"] = "Version Unknown"

value_counts_after = laptops.loc[laptops["os_version"].isnull(),"os"].value_counts()



## 10. Challenge: Extracting Storage Information ##

""""
#print(laptops["storage"].unique())

laptops["storage"] = laptops["storage"].str.replace("  ","")
laptops["storage"] = laptops["storage"].str.replace("Flash Storage","Flash_Storage")
laptops["storage"] = laptops["storage"].str.replace("+","")

df = laptops["storage"].str.split(" ",n=3,expand=True)

df.iloc[:,1] = df.iloc[:,1].str.replace("Flash_Storage","Flash Storage")

df.iloc[:,0] = df.iloc[:,0].str.replace("GB","")
df.iloc[:,0] = df.iloc[:,0].str.replace("TB","")
df.iloc[:,2] = df.iloc[:,2].str.replace("GB","")
df.iloc[:,2] = df.iloc[:,2].str.replace("TB","")

df.iloc[:,0] = df.iloc[:,0].astype(float)
df.iloc[:,2] = df.iloc[:,2].astype(float)

def tb_to_gb(value):
    if value<5:
        return value*1000
    else: return value

df.iloc[:,0] = df.iloc[:,0].apply(tb_to_gb)
df.iloc[:,2] = df.iloc[:,2].apply(tb_to_gb)

laptops[["storage_1_capacity_gb","storage_1_type","storage_2_capacity_gb","storage_2_type"]] = df

laptops.drop("storage",axis=1,inplace=True)
"""

# replace 'TB' with 000 and rm 'GB'
laptops["storage"] = laptops["storage"].str.replace('GB','').str.replace('TB','000')

# split out into two columns for storage
laptops[["storage_1", "storage_2"]] = laptops["storage"].str.split("+", expand=True)

for s in ["storage_1", "storage_2"]:
    s_capacity = s + "_capacity_gb"
    s_type = s + "_type"
    # create new cols for capacity and type
    laptops[[s_capacity, s_type]] = laptops[s].str.split(n=1,expand=True)
    # make capacity numeric (can't be int because of missing values)
    laptops[s_capacity] = laptops[s_capacity].astype(float)

# remove unneeded columns
laptops.drop(["storage", "storage_1", "storage_2"], axis=1, inplace=True)

## 11. Reordering Columns and Exporting Cleaned Data ##

laptops_dtypes = laptops.dtypes
cols = ['manufacturer', 'model_name', 'category', 'screen_size_inches',
        'screen', 'cpu', 'cpu_manufacturer',  'cpu_speed', 'ram_gb',
        'storage_1_type', 'storage_1_capacity_gb', 'storage_2_type',
        'storage_2_capacity_gb', 'gpu', 'gpu_manufacturer', 'os',
        'os_version', 'weight_kg', 'price_euros']

laptops = laptops[cols]

laptops.to_csv("laptops_cleaned.csv",index=False)

laptops_cleaned = pd.read_csv("laptops_cleaned.csv")

laptops_cleaned_dtypes = laptops_cleaned.dtypes


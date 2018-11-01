## 1. Introduction ##

houses = pd.read_table("AmesHousing_1.txt")
    
scale_land = "ordinal"

scale_roof = "nominal"

kitchen_variable = "discrete"

print(houses["Kitchen AbvGr"].tail(50))



## 2. The Mode for Ordinal Variables ##

def mode(array):
    dic = {}
    for i in array:
        if i in dic.keys():
            dic[i] += 1
        else:
            dic[i] = 1
    v=list(dic.values())
    k=list(dic.keys())
    return k[v.index(max(v))]

mode_function = mode(houses["Land Slope"])

mode_method = houses["Land Slope"].mode()

same = mode_function == mode_method

## 3. The Mode for Nominal Variables ##

# The function we wrote (you can copy-paste yours from the previous screen)
def mode(array):
    counts = {}
    
    for value in array:
        if value in counts:
            counts[value] += 1
        else:
            counts[value] = 1
    
    return (max(counts, key = counts.get),
            counts
           )

mode, value_counts = mode(houses['Roof Style'])
print(value_counts)
print(houses["Roof Style"].value_counts())


## 4. The Mode for Discrete Variables ##

#Bedroom AbvGr
print(houses["Bedroom AbvGr"].head(50))

bedroom_variable = "discrete"

bedroom_mode = houses["Bedroom AbvGr"].mode()

print(houses["SalePrice"].head(50))

price_variable = "continuous"



## 5. Special Cases ##

intervals = pd.interval_range(start = 0, end = 800000, freq = 100000)
gr_freq_table = pd.Series([0,0,0,0,0,0,0,0], index = intervals)

for value in houses['SalePrice']:
    for interval in intervals:
        if value in interval:
            gr_freq_table.loc[interval] += 1
            break

print(gr_freq_table)

# Type your answer below

mode = 150000
midpoint = 150000
mean = houses["SalePrice"].mean()
median = houses["SalePrice"].median()

print(mode,median,mean)

sentence_1 = True
sentence_2 = True

## 6. Skewed Distributions ##

distribution_1 = {'mean': 3021 , 'median': 3001, 'mode': 2947}
distribution_2 = {'median': 924 , 'mode': 832, 'mean': 962}
distribution_3 = {'mode': 202, 'mean': 143, 'median': 199}

shape_1 = "right skew"
shape_2 = "right skew"
shape_3 = "left skew"

## 7. Symmetrical Distributions ##

m = houses["Mo Sold"]
m.plot.kde(xlim = (m.min(),m.max()))

mode = m.mode()

plt.axvline(6,color="Green",label="Mode")
plt.axvline(m.median(),color="Orange",label="Median")
plt.axvline(m.mean(),color="Black",label="Mean")
plt.legend()


## 1. Simplifying Data ##

import pandas as pd
wnba = pd.read_csv("wnba.csv")

print(wnba.shape)
print(wnba)

## 2. Frequency Distribution Tables ##

wnba = pd.read_csv('wnba.csv')

freq_distro_height = wnba["Height"].value_counts()
freq_distro_pos = wnba["Pos"].value_counts()

print(freq_distro_height)
print(freq_distro_pos)

## 3. Sorting Frequency Distribution Tables ##

wnba = pd.read_csv('wnba.csv')
age_ascending = wnba["Age"].value_counts().sort_index(ascending=True)
age_descending = wnba["Age"].value_counts().sort_index(ascending=False)




## 4. Sorting Tables for Ordinal Variables ##

def make_pts_ordinal(row):
    if row['PTS'] <= 20:
        return 'very few points'
    if (20 < row['PTS'] <=  80):
        return 'few points'
    if (80 < row['PTS'] <=  150):
        return 'many, but below average'
    if (150 < row['PTS'] <= 300):
        return 'average number of points'
    if (300 < row['PTS'] <=  450):
        return 'more than average'
    else:
        return 'much more than average'
    
wnba['PTS_ordinal_scale'] = wnba.apply(make_pts_ordinal, axis = 1)

# Type your answer below

pts_ordinal_desc = wnba['PTS_ordinal_scale'].value_counts().iloc[[4,3,0,2,1,5]]

## 5. Proportions and Percentages ##

wnba = pd.read_csv('wnba.csv')

percentages = wnba["Age"].value_counts(normalize=True)*100

proportion_25 = percentages[25].round(2)
percentage_30 = percentages[30].round(2)
percentage_over_30 = percentages.sort_index().loc[30:].sum().round(3)
percentage_below_23 = percentages.sort_index().loc[:23].sum().round(3)

## 6. Percentiles and Percentile Ranks ##

from scipy.stats import percentileofscore
wnba = pd.read_csv('wnba.csv')

percentile_rank_half_less = percentileofscore(wnba["Games Played"],score=17,kind='weak')

percentage_half_more = 100 - percentile_rank_half_less

## 7. Finding Percentiles with pandas ##

from scipy.stats import percentileofscore

wnba = pd.read_csv('wnba.csv')

age_upper_quartile = wnba["Age"].describe().iloc[6]
age_middle_quartile = wnba["Age"].describe().iloc[5]
age_95th_percentile = wnba["Age"].describe(percentiles=[.95]).iloc[5]

question1 = True
question2 = False
question3 = True


## 8. Grouped Frequency Distribution Tables ##

wnba = pd.read_csv('wnba.csv')
grouped_freq_table = (wnba["PTS"].value_counts(bins=10,normalize=True)*100).sort_index(ascending=False)

## 9. Information Loss ##

import pandas as pd
wnba["MIN"].value_counts(bins=40).sort_index()

## 10. Readability for Grouped Frequency Tables ##

wnba = pd.read_csv('wnba.csv')

intervals = pd.interval_range(start=0,end=600,freq=60)

gr_freq_table_10 = pd.Series([0,0,0,0,0,0,0,0,0,0],index=intervals)

for value in wnba["PTS"]:
    for interval in intervals:
        if value in interval:
            gr_freq_table_10.loc[interval] +=1
            break
            
gr_freq_table_10.sum()



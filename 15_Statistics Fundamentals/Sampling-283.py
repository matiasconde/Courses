## 3. Populations and Samples ##

question1 = 'population'
question2 = 'population'
question3 = 'sample'
question4 = 'population'
question5 = 'sample'

## 4. Sampling Error ##

import pandas as pd
wnba = pd.read_csv('wnba.csv')

print(wnba.head())
print(wnba.tail())
print(wnba.shape)

parameter = wnba["Games Played"].max()
sample = wnba["Games Played"].sample(30,random_state=1)
statistic = sample.max()
sampling_error = parameter - statistic

print(parameter,statistic,sampling_error)



## 5. Simple Random Sampling ##

import pandas as pd
import matplotlib.pyplot as plt

wnba = pd.read_csv('wnba.csv')

samples = []

for i in range(100):
    s = wnba["PTS"].sample(10,random_state=i).mean()
    mean = s.mean()
    samples.append(mean)

true_mean = wnba["PTS"].mean()

x_values = [i for i in range(1,101)]

plt.scatter(x_values,samples)
plt.axhline(true_mean)
plt.show()

## 7. Stratified Sampling ##

wnba["pts_per_game"] = wnba["PTS"]/wnba["Games Played"]

positions = ['F', 'G/F', 'G', 'C', 'F/C']

stats = {}

for position in positions:
    stratum = wnba.loc[wnba["Pos"]==position]["pts_per_game"]
    sample = stratum.sample(10,random_state=0)
    mean = sample.mean()
    stats[position] = mean
    
def keymaxalue(dic):
    v = list(dic.values())
    k = list(dic.keys())
    return k[v.index(max(v))]

position_most_points = keymaxalue(stats)
print(position_most_points)

## 8. Proportional Stratified Sampling ##

a = wnba['Games Played'].value_counts(bins = 3, normalize = True) * 100

strat1 = wnba.loc[wnba["Games Played"]<=12]["PTS"]
strat2 = wnba.loc[(wnba["Games Played"]>12) & (wnba["Games Played"]<= 22)]["PTS"]
strat3 = wnba.loc[ wnba["Games Played"] > 22]["PTS"]

print(strat1.mean(),strat2.mean(),strat3.mean())

means = []

for i in range(100):
    
    sample1 = strat1.sample(1,random_state=i)
    sample2 = strat2.sample(2,random_state=i)
    sample3 = strat3.sample(7,random_state=i)
    sample = pd.concat([sample1,sample2,sample3])
    means.append(sample.mean())

x_values = range(1,101)
plt.scatter(x_values,means)
plt.axhline(wnba["PTS"].mean())
plt.show()

## 9. Choosing the Right Strata ##

a = wnba['MIN'].value_counts(bins = 3, normalize = True)
print(a)

strat1 = wnba.loc[wnba["MIN"]<=347.333]["PTS"]
strat2 = wnba.loc[(wnba["MIN"]>347.333) & (wnba["MIN"]<= 682.667)]["PTS"]
strat3 = wnba.loc[ wnba["MIN"] > 682.667]["PTS"]

print(strat1.mean(),strat2.mean(),strat3.mean())

means = []

for i in range(100):
    
    sample1 = strat1.sample(5,random_state=i)
    sample2 = strat2.sample(4,random_state=i)
    sample3 = strat3.sample(4,random_state=i)
    sample = pd.concat([sample1,sample2,sample3])
    means.append(sample.mean())

x_values = range(1,101)
plt.scatter(x_values,means)
plt.axhline(wnba["PTS"].mean())
plt.show()


## 10. Cluster Sampling ##

random_teams = list(pd.Series(wnba["Team"].unique()).sample(4,random_state=0))


df = pd.DataFrame()

for i in random_teams:
    
    df = df.append(wnba.loc[wnba["Team"]==i])
        
print(df.columns)

sampling_error_height = wnba["Height"].mean()-df["Height"].mean()

sampling_error_age = wnba["Age"].mean()-df["Age"].mean()

sampling_error_BMI = wnba["BMI"].mean()-df["BMI"].mean()

sampling_error_points = wnba["PTS"].mean()-df["PTS"].mean()
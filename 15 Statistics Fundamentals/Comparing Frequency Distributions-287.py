## 1. Comparing Frequency Distributions ##

# The WNBA dataset is already stored in the wnba variable
rookies = wnba[wnba['Exp_ordinal'] == 'Rookie']
little_xp = wnba[wnba['Exp_ordinal'] == 'Little experience']
experienced = wnba[wnba['Exp_ordinal'] == 'Experienced']
very_xp = wnba[wnba['Exp_ordinal'] == 'Very experienced']
veterans =  wnba[wnba['Exp_ordinal'] == 'Veteran']
rookie_distro = rookies['Pos'].value_counts()
little_xp_distro = little_xp['Pos'].value_counts()
experienced_distro = experienced['Pos'].value_counts()
very_xp_distro = very_xp['Pos'].value_counts()
veteran_distro = veterans['Pos'].value_counts()

print(rookie_distro, '\n\n', little_xp_distro, '\n\n', experienced_distro, '\n\n',
      very_xp_distro, '\n\n', veteran_distro)

## 2. Grouped Bar Plots ##

import seaborn as sns
sns.countplot(data=wnba, x="Exp_ordinal",hue="Pos",order=["Rookie","Little experience","Experienced","Very experienced","Veteran"],hue_order=["C","F","F/C","G","G/F"])

## 3. Challenge: Do Older Players Play Less? ##

import seaborn as sns
wnba["age_mean_relative"] = wnba["Age"].apply(lambda x: "old" if x>=27 else "young")
wnba["min_mean_relative"] = wnba["MIN"].apply(lambda x: "average or above" if x>=497 else "below average")

sns.countplot(data=wnba,x="age_mean_relative",hue="min_mean_relative")

result = "rejection"


## 4. Comparing Histograms ##

import matplotlib.pyplot as plt

wnba[wnba.Age >= 27]["MIN"].plot.hist(label="Old",histtype="step",legend=True)
wnba[wnba.Age < 27]["MIN"].plot.hist(label="Young",histtype="step",legend=True)
plt.axvline(wnba["MIN"].mean().round(0),label="Average")
plt.legend()
                                    

## 5. Kernel Density Estimate Plots ##

import seaborn as sns
wnba[wnba["Age"]>=27]["MIN"].plot.kde(label="Old",legend=True)
wnba[wnba["Age"]<27]["MIN"].plot.kde(label="Young",legend=True)
plt.axvline(wnba["MIN"].mean().round(0),label="Average")
plt.legend()


## 7. Strip Plots ##

import seaborn as sns

sns.stripplot(data=wnba,x="Pos",y="Weight",jitter=True)


## 8. Box plots ##

import seaborn as sns

sns.boxplot(data=wnba,x="Pos",y="Weight")

## 9. Outliers ##

descriptive_stats = wnba["Games Played"].describe()
iqr = descriptive_stats[6]-descriptive_stats[4]

lower_bound = descriptive_stats[4]-1.5*iqr
upper_bound = descriptive_stats[6]+1.5*iqr

cont1=0
cont2=0

for value in wnba["Games Played"]:
    if value > upper_bound:
        cont2 +=1
    elif value < lower_bound:
        cont1 +=1
        
outliers_high = cont2
outliers_low = cont1

sns.boxplot(wnba["Games Played"],whis=1.5,orient = "vertical",width=.15)


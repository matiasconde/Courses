## 2. Calculating expected values ##

males_over50k = .669*.241*32561
males_under50k = .669*.759*32561

females_over50k = .241*.331*32561
females_under50k = .759*.331*32561


## 3. Calculating chi-squared ##

males_over50k = round(.669*.241*32561,1)
males_under50k = round(.669*.759*32561,1)

females_over50k = round(.241*.331*32561,1)
females_under50k = round(.759*.331*32561,1)

obs_males_over50k = 6662
obs_males_under50k = 15128

obs_females_over50k = 1179
obs_females_under50k = 9592

expected = [males_over50k,females_over50k,males_under50k,females_under50k]
observed = [obs_males_over50k,obs_females_over50k,obs_males_under50k,obs_females_under50k]
chisq_gender_income = 0

for i in range(4):
    chisq_gender_income += (observed[i]-expected[i])**2 / expected[i] 

## 4. Finding statistical significance ##

import scipy
from scipy.stats import chisquare

males_over50k = round(.669*.241*32561,1)
males_under50k = round(.669*.759*32561,1)

females_over50k = round(.241*.331*32561,1)
females_under50k = round(.759*.331*32561,1)

obs_males_over50k = 6662
obs_males_under50k = 15128

obs_females_over50k = 1179
obs_females_under50k = 9592

expected = [males_over50k,females_over50k,males_under50k,females_under50k]
observed = [obs_males_over50k,obs_females_over50k,obs_males_under50k,obs_females_under50k]

chisq_value, pvalue_gender_income = chisquare(observed,expected)

## 5. Cross tables ##

import pandas as pd

table = pd.crosstab(income["sex"],[income["race"]])
print(table)

## 6. Finding expected values ##

import numpy as np
from scipy.stats import chi2_contingency
import pandas as pd

table = pd.crosstab(income["sex"],[income["race"]])
chisq_value, pvalue_gender_race, dof, expected = chi2_contingency(table)

## 2. Calculating differences ##

female_diff=(10771-16280.5)/16280.5
male_diff=(21790-16280.5)/16280.5

## 3. Updating the formula ##

female_diff=(10771-16280.5)**2/16280.5
male_diff=(21790-16280.5)**2/16280.5

gender_chisq = male_diff + female_diff

## 4. Generating a distribution ##

chi_squared_values = []
expected_value = 16280.5
for i in range(1000):
    randoms = numpy.random.random(32561)
    for i,value in enumerate(randoms):
        if value<0.5:
            randoms[i]=0
        else: randoms[i]=1
    male_count = (randoms==0).sum()
    female_count = (randoms==1).sum()
    male_diff = (male_count - expected_value)**2 / expected_value
    female_diff = (female_count - expected_value)**2 / expected_value
    chi_squared_values.append(male_diff + female_diff)

plt.hist(chi_squared_values)

## 6. Smaller samples ##

exp_value = 162.805
N = exp_value

female_diff = (exp_value - 107.71)**2 / N
male_diff = (exp_value - 217.9)**2 / N

gender_chisq = male_diff + female_diff

## 7. Sampling distribution equality ##

chi_squared_values = []

for i in range(1000):
    uniform_randoms = numpy.random.random(300)
    for i,v in enumerate(uniform_randoms):
        if v<0.5: uniform_randoms[i]=0
        else: uniform_randoms[i]=1
    male_count = (uniform_randoms==0).sum()
    female_count = (uniform_randoms==1).sum()
    male_diff = (male_count - 150)**2 / 150
    female_diff = (female_count - 150)**2 / 150
    chi_squared_values.append(male_diff + female_diff)

plt.hist(chi_squared_values)
plt.show()

## 9. Increasing degrees of freedom ##

lista = []
lista.append((27816-26146.5)**2 / 26146.5)
lista.append((3124-3939.9)**2 / 3939.9)
lista.append((1039-944.3)**2 / 944.3)
lista.append((311-260.5)**2 / 260.5)
lista.append((271-1269.8)**2 / 1269.8)


race_chisq = sum(lista)

## 10. Using SciPy ##

from scipy.stats import chisquare
import numpy as np

Observed = [27816,3124,1039,311,271]
Expected = [26146.5,3939.9,944.3,260.5,1269.8]

chisquare_value, race_pvalue = chisquare(observed,expected)


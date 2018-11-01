## 3. Bikesharing distribution ##

import pandas
bikes = pandas.read_csv("bike_rental_day.csv")

prob_over_5000 = (bikes[bikes["cnt"]>5000].shape[0])/(bikes["cnt"].shape[0])

## 4. Computing the distribution ##

import math

# Each item in this list represents one k, starting from 0 and going up to and including 30.
outcome_counts = list(range(31))

def combinatorial(N,k):
    return (math.factorial(N)) / ((math.factorial(k))*(math.factorial(N-k)))

def binomial_density(p,i,N):
    return math.pow(p,i)*math.pow(1-p,N-i)*combinatorial(N,i)

p = .39
N = 30
outcome_probs = []

for i in outcome_counts:
    outcome_probs.append(binomial_density(p,i,N))
    

## 5. Plotting the distribution ##

import matplotlib.pyplot as plt

# The most likely number of days is between 10 and 15.
plt.bar(outcome_counts, outcome_probs)
plt.show()

## 6. Simplifying the computation ##

import scipy
from scipy import linspace
from scipy.stats import binom
import matplotlib.pyplot as plt
# Create a range of numbers from 0 to 30, with 31 elements (each number has one entry).
outcome_counts = linspace(0,30,31)

dist = binom.pmf(outcome_counts,30,.39)

plt.bar(outcome_counts,dist)
plt.show()

## 8. Computing the mean of a probability distribution ##

dist_mean = None

N=30
p=.39

dist_mean = N*p

## 9. Computing the standard deviation ##

dist_stdev = None

N=30
p=.39
q=1-p

dist_stdev = (N*p*q)**0.5

## 10. A different plot ##

# Enter your answer here.
import scipy
from scipy import linspace
from scipy.stats import binom
import matplotlib.pyplot as plt

outcome_counts = linspace(0,10,11)
dist1 = binom.pmf(outcome_counts,10,.39)
plt.bar(outcome_counts,dist1)
plt.show()

outcome_counts2 = linspace(0,100,101)
dist2 = binom.pmf(outcome_counts2,100,.39)
plt.bar(outcome_counts2,dist2)
plt.show()


## 11. The normal distribution ##

# Create a range of numbers from 0 to 100, with 101 elements (each number has one entry).
outcome_counts = scipy.linspace(0,100,101)

# Create a probability mass function along the outcome_counts.
outcome_probs = binom.pmf(outcome_counts,100,0.39)

# Plot a line, not a bar chart.
plt.plot(outcome_counts, outcome_probs)
plt.show()

## 12. Cumulative density function ##

outcome_counts = linspace(0,30,31)

N= 30
p = .39

dist = binom.cdf(outcome_counts,N,p)
plt.plot(outcome_counts,dist)
plt.show()

## 14. Faster way to calculate likelihood ##

left_16 = None
right_16 = None

left_16 = binom.cdf(16,30,.39)
right_16 = 1 - left_16
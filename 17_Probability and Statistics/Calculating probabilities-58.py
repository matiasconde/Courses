## 2. Probability of renting bikes ##

import pandas as pd
bikes = pd.read_csv("bike_rental_day.csv")

probability_over_4000 = bikes[bikes["cnt"]>4000].shape[0]/(bikes["cnt"].shape[0])

## 4. Calculating probabilities ##

# Enter your code here.
coin_1_prob = (.5**3)*3

## 6. Calculating the number of combinations ##

sunny_1_combinations = None

sunny_1_combinations = 5

## 8. Finding the number of combinations ##

import math
def combinatorial(N, k):
    # Calculate the numerator of our formula.
    numerator = math.factorial(N)
    # Calculate the denominator.
    denominator = math.factorial(k) * math.factorial(N - k)
    # Divide them to get the final value.
    return numerator / denominator

combinations_7 = combinatorial(10, 7)

#prob = bikes[bikes["cnt"]>4000].shape[0]/(bikes["cnt"].shape[0])

combinations_8 = combinatorial(10,8)

combinations_9 = combinatorial(10,9)

## 10. Calculating the probability of one combination ##

prob_combination_3 = None

prob_combination_3 = (.7**3)*(.3**2)

## 12. Function to calculate the probability of a single combination ##

p = .6
q = .4

import math
def combinatorial(N, k):
    # Calculate the numerator of our formula.
    numerator = math.factorial(N)
    # Calculate the denominator.
    denominator = math.factorial(k) * math.factorial(N - k)
    # Divide them to get the final value.
    return numerator / denominator

def binomial_density(p,q,N,k):
    prob = (p**k)*(q**(N-k))
    return prob*combinatorial(N,k)

prob_8 = binomial_density(p,q,10,8)
prob_9 = binomial_density(p,q,10,9)
prob_10 = binomial_density(p,q,10,10)

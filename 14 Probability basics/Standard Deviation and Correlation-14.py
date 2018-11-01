## 2. The Mean as the Center ##

# Make a list of values
values = [2, 4, 5, -1, 0, 10, 8, 9]
# Compute the mean of the values
values_mean = sum(values) / len(values)
# Find the difference between each of the values and the mean by subtracting the mean from each value.
differences = [i - values_mean for i in values]
# This equals 0.  If you'd like, try changing the values around to verify that it still equals 0.
print(sum(differences))

# We can use the median function from numpy to find the median.
# The median is the "middle" value in a set of values. If we sort the values in order, it's the one in the center (or the average of the two in the center if there are an even number of items in the set).
# You'll see that the differences from the median don't always add up to 0.  You might want to play around with this and think about why that is.
from numpy import median

values_median = numpy.median(values)

median_difference_sum = [i-values_median for i in values]

print(median_difference_sum)

print(values_mean)
print(values_median)
print(sorted(values))

## 3. Finding Variance ##

import matplotlib.pyplot as plt
import pandas as pd
# We've already loaded the NBA data into the nba_stats variable.
# Find the mean value of the column.
pf_mean = nba_stats["pf"].mean()
# Initialize variance at zero.
variance = 0
# Loop through each item in the "pf" column.
for p in nba_stats["pf"]:
    # Calculate the difference between the mean and the value.
    difference = p - pf_mean
    # Square the difference. This ensures that the result isn't negative.
    # If we didn't square the difference, the total variance would be zero.
    # ** in python means "raise whatever comes before this to the power of whatever number is after this."
    square_difference = difference ** 2
    # Add the difference to the total.
    variance += square_difference
# Average the total to find the final variance.
variance = variance / len(nba_stats["pf"])

pts_mean = nba_stats["pts"].mean()

point_variance = sum([(i-pts_mean)**2 for i in nba_stats["pts"]])/len(nba_stats["pts"])

## 4. Understanding the Order of Operations ##

# You may be wondering why multiplication and division are on the same level.
# It doesn't matter whether we do the multiplication or division first; the answer here will always be the same.
# In this case, we need to think of division as multiplication by a fraction. Otherwise, we'll be dividing more than we want to.
# Create a formula
a = 5 * 5 / 2
# Multiply by 1/2 instead of dividing by 2. The result is the same (2/2 == 2 * 1/2).
a_subbed = 5 * 5 * 1/2
a_mul_first = 25 * 1/2
a_div_first = 5 * 2.5
print(a_mul_first == a_div_first)

# The same is true for subtraction and addition.
# In this case, we need to convert subtraction into adding a negative number. If we don't we'll end up subtracting more than we expect.
b = 10 - 8 + 5
# Add -8 instead of subtracting 8.
b_subbed = 10 + -8 + 5
b_sub_first = 2 + 5
b_add_first = 10 + -3
print(b_sub_first == b_add_first)

c = float(10 * 2 + 5)
d = (3 - 1) /( 2 * 2)

## 5. Using Parentheses to Change the Order of Operations ##

a = 50 * 50 - 10 / 5
a_paren = 50 * (50 - 10) / 5
# If we put multiple operations inside parentheses, the interpreter will use the order of operations to determine the sequence in which it should execute them.
a_paren = 50 * (50 - 10 / 5)

b = 10 * (10 + 100)
c = (8 - 6) * 100

## 6. Fractional Powers ##

a = 5 ** 2
# Raise to the fourth power
b = 10 ** 4

# Take the square root ( 3 * 3 == 9, so the answer is 3)
c = 9 ** (1/2)

# Take the cube root (4 * 4 * 4 == 64, so 4 is the cube root)
d = 64 ** (1/3)

e = 11**5

f = 10000**(1/4)

## 7. Calculating Standard Deviation ##

# We've already loaded the NBA stats into the nba_stats variable.

def std_deviation(column_stats):
    column_mean = nba_stats[column_stats].mean()
    v = sum([(i-column_mean)**2 for i in nba_stats[column_stats]])/len(nba_stats[column_stats])
    return v**(1/2)

mp_dev = std_deviation("mp")

print(mp_dev)

ast_dev = std_deviation("ast")

print(ast_dev)



## 8. Finding Standard Deviation Distance ##

import matplotlib.pyplot as plt

plt.hist(nba_stats["pf"])
mean = nba_stats["pf"].mean()
plt.axvline(mean, color="r")
# We can calculate standard deviation by using the std() method on a pandas series.
std_dev = nba_stats["pf"].std()
# Plot a line one standard deviation below the mean.
plt.axvline(mean - std_dev, color="g")
# Plot a line one standard deviation above the mean.
plt.axvline(mean + std_dev, color="g")

# We can see how many of the data points fall within one standard deviation of the mean.
# The more that fall into this range, the more dense the data is.
plt.show()

# We can calculate how many standard deviations a data point is from the mean by doing some subtraction and division.
# First, we find the total distance by subtracting the mean.
total_distance = nba_stats["pf"][0] - mean
# Then we divide by standard deviation to find how many standard deviations away the point is.
standard_deviation_distance = total_distance / std_dev

point_10 = nba_stats["pf"][9]
point_100 = nba_stats["pf"][99]

point_10_std = (point_10 - mean) / std_dev
point_100_std = (point_100 - mean) / std_dev

## 9. Working with the Normal Distribution ##

import numpy as np
import matplotlib.pyplot as plt
# The norm module has a pdf function (pdf stands for probability density function)
from scipy.stats import norm

# The arange function generates a numpy vector
# The vector below will start at -1, and go up to, but not including 1
# It will proceed in "steps" of .01.  So the first element will be -1, the second -.99, the third -.98, all the way up to .99.
points = np.arange(-1, 1, 0.01)

# The norm.pdf function will take the points vector and convert it into a probability vector
# Each element in the vector will correspond to the normal distribution (earlier elements and later element smaller, peak in the center)
# The distribution will be centered on 0, and will have a standard devation of .3
probabilities = norm.pdf(points, 0, .3)

# Plot the points values on the x-axis and the corresponding probabilities on the y-axis
# See the bell curve?
plt.plot(points, probabilities)
plt.show()

points2 = np.arange(-10,10,0.1)
probabilities2 = norm.pdf(points2,0,2)

plt.plot(points2,probabilities2)
plt.show()

## 10. Normal Distribution Deviation ##

# Housefly wing lengths in millimeters
wing_lengths = [36, 37, 38, 38, 39, 39, 40, 40, 40, 40, 41, 41, 41, 41, 41, 41, 42, 42, 42, 42, 42, 42, 42, 43, 43, 43, 43, 43, 43, 43, 43, 44, 44, 44, 44, 44, 44, 44, 44, 44, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 47, 47, 47, 47, 47, 47, 47, 47, 47, 48, 48, 48, 48, 48, 48, 48, 48, 49, 49, 49, 49, 49, 49, 49, 50, 50, 50, 50, 50, 50, 51, 51, 51, 51, 52, 52, 53, 53, 54, 55]

n = len(wing_lengths)

mean = sum(wing_lengths)/n
variance = sum([(i - mean)**2 for i in wing_lengths]) / n

std_dev = variance**(1/2)

std_dev_distances = [(i-mean)/std_dev for i in wing_lengths]

def module(x):
    if x<0:
        return (-1)*x
    else: return x
    
cont1 = 0 

for i in std_dev_distances:
    if module(i)<=1:
        cont1 += 1
print(cont1/n)

within_one_percentage = cont1 / n
print(within_one_percentage)
cont2 = 0 


for i in std_dev_distances:
    if module(i)<=2:
        cont2 += 1
        
within_two_percentage = cont2 / n

cont3 = 0 

for i in std_dev_distances:
    if module(i)<=3:
        cont3 += 1
        
within_three_percentage = cont3 / n

print(within_one_percentage,within_two_percentage,within_three_percentage)
        
    
    

## 11. Using Scatterplots to Plot Correlations ##

import matplotlib.pyplot as plt

# Plot field goals attempted (number of shots someone takes in a season) vs. point scored in a season.
# Field goals attempted is on the x-axis, and points is on the y-axis.
# As you can tell, they are very strongly correlated. The plot is close to a straight line.
# The plot also slopes upward, which means that as field goal attempts go up, so do points.
# That means that the plot is positively correlated.
plt.scatter(nba_stats["fga"], nba_stats["pts"])
plt.show()

# If we make points negative (so the people who scored the most points now score the least, because 3000 becomes -3000), we can change the direction of the correlation.
# Field goals are negatively correlated with our new "negative" points column -- the more free throws you attempt, the less negative points you score.
# We can see this because the correlation line slopes downward.
plt.scatter(nba_stats["fga"], -nba_stats["pts"])
plt.show()

# Now, we can plot total rebounds (number of times someone got the ball back for their team after someone shot) vs total assists (number of times someone helped another person score).
# These are uncorrelated, so you don't see the same nice line as you see with the plot above.
plt.scatter(nba_stats["trb"], nba_stats["ast"])
plt.show()

plt.scatter(nba_stats["fta"],nba_stats["pts"])
plt.show()

plt.scatter(nba_stats["stl"],nba_stats["pf"])
plt.show()


## 12. Measuring Correlation with Pearson's r ##

from scipy.stats.stats import pearsonr

# The pearsonr function will find the correlation between two columns of data.
# It returns the r value and the p value.  We'll learn more about p values later on.
r, p_value = pearsonr(nba_stats["fga"], nba_stats["pts"])
# As we can see, this is a very high positive r value - it's close to 1.
print(r)

# These two columns are much less correlated.
r, p_value = pearsonr(nba_stats["trb"], nba_stats["ast"])
# We get a much lower, but still positive, r value.
print(r)

r_fta_pts, p_value = pearsonr(nba_stats["fta"], nba_stats["pts"])
r_stl_pf, p_value = pearsonr(nba_stats["stl"], nba_stats["pf"])

print(r_fta_pts,p_value)
print(r_stl_pf,p_value)

## 13. Calculate Covariance ##

# We've already loaded the nba_stats variable.}

def covariance(x,y):
    n = x.shape[0]
    mean_x = x.mean()
    mean_y = y.mean()
    dev_x = x-mean_x
    dev_y = y-mean_y
    cv = (dev_x*dev_y).sum()
    return float(cv / n)

cov_stl_pf = covariance(nba_stats["stl"],nba_stats["pf"])
print(cov_stl_pf)

cov_fta_pts = covariance(nba_stats["fta"],nba_stats["pts"])
print(cov_fta_pts)



## 14. Calculate Correlation With the std() Method ##

from numpy import cov
# We've already loaded the nba_stats variable for you.

r_fta_blk = cov(nba_stats["fta"],nba_stats["blk"])[0,1] / (nba_stats["fta"].std()*nba_stats["blk"].std())
print(r_fta_blk)

r_ast_stl = cov(nba_stats["ast"],nba_stats["stl"])[0,1] / (nba_stats["ast"].std()*nba_stats["stl"].std())
print(r_ast_stl)

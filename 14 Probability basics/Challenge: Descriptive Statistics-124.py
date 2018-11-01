## 1. Introduction ##

import matplotlib.pyplot as plt
import pandas as pd
movie_reviews = pd.read_csv("fandango_score_comparison.csv")

fig = plt.figure(figsize=(5,12))
columns = ["RT_user_norm","Metacritic_user_nom","Fandango_Ratingvalue","IMDB_norm"]

for i in range(1,5):
    ax = fig.add_subplot(4,1,i)
    ax.set_xlim(0.0,5.0)
    movie_reviews[columns[i-1]].hist(ax=ax)

plt.show()

## 2. Mean ##

def calc_mean(series):
    return series.mean()

user_reviews = movie_reviews[ ["RT_user_norm","Metacritic_user_nom","Fandango_Ratingvalue","IMDB_norm"]]

means = user_reviews.apply(calc_mean)

rt_mean = means["RT_user_norm"]
mc_mean = means["Metacritic_user_nom"]
fg_mean = means["Fandango_Ratingvalue"]
id_mean = means["IMDB_norm"]

print(means)

## 3. Variance and standard deviation ##

def calc_mean(series):
    vals = series.values
    mean = sum(vals) / len(vals)
    return mean

def calc_variance(series):
    vals = series.values
    mean = calc_mean(series)
    return sum([(i-mean)**2 for i in vals]) / len(vals)

rt_var = user_reviews.apply(calc_variance)["RT_user_norm"]
rt_stdev = rt_var**(0.5)

print(rt_var,rt_stdev)

mc_var = user_reviews.apply(calc_variance)["Metacritic_user_nom"]
mc_stdev = mc_var**(0.5)

print(mc_var,mc_stdev)

fg_var = user_reviews.apply(calc_variance)["Fandango_Ratingvalue"]
fg_stdev = fg_var**(0.5)

print(fg_var,fg_stdev)

id_var = user_reviews.apply(calc_variance)["IMDB_norm"]
id_stdev = id_var**(0.5)

print(id_var,id_stdev)

## 4. Scatter plots ##

import matplotlib.pyplot as plt
import pandas as pd
user_reviews = movie_reviews[ ["RT_user_norm","Metacritic_user_nom","Fandango_Ratingvalue","IMDB_norm"]]
fig = plt.figure(figsize=(4,8))

ax1 = fig.add_subplot(3,1,1)
ax2 = fig.add_subplot(3,1,2)
ax3 = fig.add_subplot(3,1,3)
ax1.set_xlim(0.0,5.0)
ax2.set_xlim(0.0,5.0)
ax3.set_xlim(0.0,5.0)
    
ax1.scatter(user_reviews["RT_user_norm"],user_reviews["Fandango_Ratingvalue"])
ax2.scatter(user_reviews["Metacritic_user_nom"],user_reviews["Fandango_Ratingvalue"])
ax3.scatter(user_reviews["IMDB_norm"],user_reviews["Fandango_Ratingvalue"])

plt.show()



## 5. Covariance ##

user_reviews = movie_reviews[ ["RT_user_norm","Metacritic_user_nom","Fandango_Ratingvalue","IMDB_norm"]]

def calc_mean(series):
    vals = series.values
    mean = sum(vals) / len(vals)
    return mean

def covariance(serie1,serie2):
    vals1 = serie1.values
    vals2 = serie2.values
    mean1 = calc_mean(serie1)
    mean2 = calc_mean(serie2)
    n = len(vals1)
    
    return sum([(vals1[i]-mean1)*(vals2[i]-mean2) for i in range(n)]) / n
                
rt_fg_covar = covariance(user_reviews["RT_user_norm"],user_reviews["Fandango_Ratingvalue"])

mc_fg_covar = covariance(user_reviews["Metacritic_user_nom"],user_reviews["Fandango_Ratingvalue"])

id_fg_covar = covariance(user_reviews["IMDB_norm"],user_reviews["Fandango_Ratingvalue"])

print(rt_fg_covar, mc_fg_covar, id_fg_covar)

## 6. Correlation ##

def calc_mean(series):
    vals = series.values
    mean = sum(vals) / len(vals)
    return mean

def calc_variance(series):
    mean = calc_mean(series)
    squared_deviations = (series - mean)**2
    mean_squared_deviations = calc_mean(squared_deviations)
    return mean_squared_deviations

def calc_covariance(series_one, series_two):
    x = series_one.values
    y = series_two.values
    x_mean = calc_mean(series_one)
    y_mean = calc_mean(series_two)
    x_diffs = [i - x_mean for i in x]
    y_diffs = [i - y_mean for i in y]
    codeviates = [x_diffs[i] * y_diffs[i] for i in range(len(x))]
    return sum(codeviates) / len(codeviates)

def calc_std_deviation(series):
    return calc_variance(series)**0.5

rt_fg_covar = calc_covariance(movie_reviews["RT_user_norm"], movie_reviews["Fandango_Ratingvalue"])
mc_fg_covar = calc_covariance(movie_reviews["Metacritic_user_nom"], movie_reviews["Fandango_Ratingvalue"])
id_fg_covar = calc_covariance(movie_reviews["IMDB_norm"], movie_reviews["Fandango_Ratingvalue"])

def calc_correlation(series_one,series_two):
    return calc_covariance(series_one,series_two)/(calc_std_deviation(series_one)*calc_std_deviation(series_two))

rt_fg_corr = calc_correlation(movie_reviews["RT_user_norm"], movie_reviews["Fandango_Ratingvalue"])
mc_fg_corr = calc_correlation(movie_reviews["Metacritic_user_nom"], movie_reviews["Fandango_Ratingvalue"])
id_fg_corr = calc_correlation(movie_reviews["IMDB_norm"], movie_reviews["Fandango_Ratingvalue"])

print(rt_fg_corr,mc_fg_corr,id_fg_corr)
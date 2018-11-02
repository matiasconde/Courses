## 2. The Mean ##

distribution = [0,2,3,3,3,4,13]

mean = sum(distribution)/len(distribution)

center = False

distances = [abs(i-mean) for i in distribution]

below = sum(distances[:5])
above = sum(distances[5:])

print(below-above)

equal_distances = True

## 3. The Mean as a Balance Point ##

from numpy.random import randint, seed
equal_distances = 0

for j in range(5000):
    seed(j)
    dist = randint(low=0,high=1000,size=10)
    mean = sum(dist)/len(dist)
    low_distances = [abs(i-mean).round(1) for i in dist if i<=mean]
    high_distances = [abs(i-mean).round(1) for i in dist if i> mean]
    suma1 = sum(low_distances)
    suma2 = sum(high_distances)
    if (suma1.round(1)-suma2.round(1)) == 0.0:
        equal_distances += 1

print(equal_distances)


## 4. Defining the Mean Algebraically ##

one=False
two=False
three=False

## 5. An Alternative Definition ##

distribution_1 = [42, 24, 32, 11]
distribution_2 = [102, 32, 74, 15, 38, 45, 22]
distribution_3 = [3, 12, 7, 2, 15, 1, 21]
def mean(x):
    suma=0
    n = len(x)
    for i in range(n):
        suma += x[i-1]
    return suma/n        
        
mean_1 = mean(distribution_1)
mean_2 = mean(distribution_2)
mean_3 = mean(distribution_3)



## 6. Introducing the Data ##

houses = pd.read_table("AmesHousing_1.txt")
print(houses.head())
one = True
two = False

houses.shape
three = True




## 7. Mean House Prices ##

def mean(distribution):
    sum_distribution = 0
    for value in distribution:
        sum_distribution += value
        
    return sum_distribution / len(distribution)

function_mean = mean(houses["SalePrice"])

pandas_mean = houses["SalePrice"].mean()

means_are_equal = function_mean == pandas_mean



## 8. Estimating the Population Mean ##

mean = houses["SalePrice"].mean()
k = 5
x_values = []
y_values = []

for i in range(100):
    
    sample = houses["SalePrice"].sample(k,random_state=i)
    sample_size = k
    k += 29
    Sample_mean = sample.mean()
    sample_error = mean-Sample_mean
    x_values.append(sample_size)
    y_values.append(sample_error)

plt.scatter(x_values,y_values)
plt.axhline(0)
plt.axvline(2930)
plt.xlabel("Sample size")
plt.ylabel("Sampling error")
plt.show()

## 9. Estimates from Low-Sized Samples ##

means = []

for i in range(10000):
    sample = houses["SalePrice"].sample(100,random_state=i)
    sample_mean = sample.mean()
    means.append(sample_mean)
    
mean = sum(means)/len(means)
mean_true = houses["SalePrice"].mean()
plt.hist(means)
plt.axvline(mean_true)
plt.xlim(0,500000)
plt.xlabel("Sample mean")
plt.ylabel("Frequency")
plt.show()

print(mean, mean_true)

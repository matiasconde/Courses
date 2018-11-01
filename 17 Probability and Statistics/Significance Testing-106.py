## 3. Statistical significance ##

import numpy as np
import matplotlib.pyplot as plt

mean_group_a = np.mean(weight_lost_a)
mean_group_b = np.mean(weight_lost_b)

plt.hist(weight_lost_a,color="y",label="placebo")
plt.hist(weight_lost_b, label="pill")
plt.legend()
plt.show()

## 4. Test statistic ##

mean_difference = mean_group_b - mean_group_a

print(mean_difference)

## 5. Permutation test ##

mean_difference = 2.52
print(all_values)

mean_differences = []

for i in range(1000):
    group_a = []
    group_b = []
    for value in all_values:
        random_value = numpy.random.rand()
        if random_value>=0.5:
            group_a.append(value)
        else: group_b.append(value)
    iteration_mean_difference = numpy.mean(group_b) - numpy.mean(group_a)
    mean_differences.append(iteration_mean_difference)

plt.hist(mean_differences)
plt.show()

## 7. Dictionary representation of a distribution ##

sampling_distribution = {}

for value in mean_differences:
    if sampling_distribution.get(value,False):
        val = sampling_distribution.get(value)
        inc = val+1
        sampling_distribution[value] = inc
    else: sampling_distribution[value]=1
        
        

## 8. P value ##

frequencies = []
original_mean_difference = 2.52
N_permutations = 1000
for value in sampling_distribution.keys():
    if value>=original_mean_difference:
        frequencies.append(value)
p_value = numpy.sum(frequencies) / N_permutations

print(p_value)
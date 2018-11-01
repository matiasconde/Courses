## 1. Probability basics ##

# Print the first two rows of the data.
# print(flags[:2])

most_bars_country = flags[flags["bars"]==flags["bars"].max()]["name"]

highest_population_country = flags[flags["population"]==flags["population"].max()]["name"]

## 2. Calculating probability ##

total_countries = flags.shape[0]

orange_probability = flags["orange"].sum() / total_countries

stripe_probability = flags[flags["stripes"]>1].shape[0] / total_countries

print(flags[flags["stripes"]>1]["stripes"].shape[0])

## 3. Conjunctive probabilities ##

five_heads = .5 ** 5

ten_heads = 0.5**10

hundred_heads = 0.5**100

## 4. Dependent probabilities ##

# Remember that whether a flag has red in it or not is in the `red` column.

total_countries_with_red = flags[flags["red"]==1].shape[0]

total_countries = flags.shape[0]

three_red=1

for i in range(3):
    three_red *= (total_countries_with_red-i)/(total_countries-i)
    
    

## 5. Disjunctive probability ##

start = 1
end = 18000

hundred_prob = (18000//100)/18000

seventy_prob = (18000//70)/18000





## 6. Disjunctive dependent probabilities ##

stripes_or_bars = None
red_or_orange = None

red_and_orange = flags[(flags["red"]==1)&(flags["orange"]==1)].shape[0]

red_or_orange = (flags[flags["red"]==1].shape[0]+flags[flags["orange"]==1].shape[0]-red_and_orange)/flags.shape[0]

stripes_and_bars = flags[(flags["stripes"]>=1)&(flags["bars"]>=1)].shape[0]

stripes_or_bars = (flags[flags["stripes"]>=1].shape[0]+flags[flags["bars"]>=1].shape[0]-stripes_and_bars)/flags.shape[0]


## 7. Disjunctive probabilities with multiple conditions ##

heads_or = None

heads_or = 1-0.5**3
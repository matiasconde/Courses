## 2. Comparing Object-Oriented to Functional ##

## Display
def read(filename):
    f = open(filename,"r")
    return [line for line in f]

def count(lista):
    return len(lista)

example_lines = read("example_log.txt")

lines_count = count(example_lines)

## 4. The Lambda Expression ##

def read(filename):
    with open(filename, 'r') as f:
        return [line for line in f]
    
lines = read('example_log.txt')

sorted_lines = sorted(lines, key=lambda x: x.split(" ")[5])
print(sorted_lines)

## 5. The Map Function ##

lines = read('example_log.txt')

ip_addresses = list(map(lambda x: x.split(" ")[0], lines))

print(ip_addresses)

## 6. The Filter Function ##

lines = read('example_log.txt')
ip_addresses = list(map(lambda x: x.split()[0], lines))

filtered_ips = list(filter(lambda x: int(x.split(".")[0]) <= 20, ip_addresses))
print(filtered_ips)

## 7. The Reduce Function ##

from functools import reduce

lines = read('example_log.txt')
ip_addresses = list(map(lambda x: x.split()[0], lines))
filtered_ips = list(filter(lambda x: int(x.split('.')[0]) <= 20, ip_addresses))

total_lines = reduce(lambda a,_: 2 if isinstance(a,str) else a+1, lines)
total_filtered_ips = reduce(lambda a,_:  2 if isinstance(a,str) else a+1, filtered_ips)

ratio = total_filtered_ips / total_lines
print(ratio)

## 8. Rewriting with List Comprehension ##

lines = read('example_log.txt')
# Rewrite ip_addresses, and filtered_ips.
# list(map(lambda x: x.split()[0], lines))
# list(filter(lambda x: int(x.split('.')[0]) <= 20, ip_addresses))
count_all = reduce(lambda x, _: 2 if isinstance(x, str) else x + 1, lines)
count_filtered = reduce(lambda x, _: 2 if isinstance(x, str) else x + 1, filtered_ips)
ratio = count_filtered / count_all
print(ratio)

ip_addresses = [x.split()[0] for x in lines]
filtered_ips = [x for x in ip_addresses if int(x.split(".")[0])<=20]


## 9. Writing Function Partials ##

from functools import partial

lines = read('example_log.txt')
ip_addresses = list(map(lambda x: x.split()[0], lines))
filtered_ips = list(filter(lambda x: int(x.split('.')[0]) <= 20, ip_addresses))

# reduce(lambda x, _: 2 if isinstance(x, str) else x + 1, lines)
# reduce(lambda x, _: 2 if isinstance(x, str) else x + 1, filtered_ips)
ratio = count_filtered / count_all

contar = partial(reduce,lambda x, _: 2 if isinstance(x,str) else x+1)

count_all = contar(lines)
count_filtered = contar(ip_addresses)



## 10. Using Functional Composition ##

lines = read('example_log.txt')
ip_addresses = list(map(lambda x: x.split()[0], lines))
filtered_ips = list(filter(lambda x: int(x.split('.')[0]) <= 20, ip_addresses))

ratio = count_filtered / count_all

get_ips = partial(map, lambda x: x.split()[0])
filter_ips = partial(filter,lambda x: int(x.split(".")[0]) <= 20)
count = partial(reduce, lambda x,_: 2 if isinstance(x,str) else x+1)

composed = compose(get_ips, filter_ips, count)
counted = composed(lines)
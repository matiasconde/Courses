## 2. Recursion is thinking in Recursion ##

search_list = ['apple', 'orange', 'pear', 'fig', 'passionfruit']

def search(strings, term, index=0):
    if strings[0] == term:
        return index
    if (len(strings)<=1):
        return -1
    new_strings = strings[1:]
    index += 1
    return search(new_strings,term,index = index)
    
apple_index = search(search_list,"apple")
pear_index = search(search_list,"pear")
foo_index = search(search_list,"foo")


## 3. Stack Overflow ##

def traverse_list(values):
    return traverse_list(values)
    

traverse_list([])

## 4. Divide and Conquer ##

import math

def summation(values):
    middle = math.floor(len(values)/2)
    if middle == 0: 
        return values
    part1 = values[:middle]
    part2 = values[middle:]
    
    return summation(part1) + summation(part2)
  
f = open("random_integers.txt","r") 
random_integers = [int(line) for line in f.readlines()]

divide_and_conquer_sum = summation(random_integers)

## 6. Merge Sort (Part 2) ##

import math 

f = open('random_integers.txt', 'r')
random_integers = [int(line) for line in f.readlines()]

def merge(left_list, right_list):
    sorted = []
    while left_list and right_list:
        if left_list[0] < right_list[0]:
            sorted.append(left_list.pop(0))
        else:
            sorted.append(right_list.pop(0))
    sorted += left_list
    sorted += right_list
    return sorted

def merge_sort(unsorted):
    if len(unsorted)<=1:
        return unsorted
    middle = math.floor(len(unsorted)/2) 
    part1 = unsorted[middle:]
    part2 = unsorted[:middle]
    sorted1 = merge_sort(part1)
    sorted2 = merge_sort(part2)
    sorted = merge(sorted1,sorted2)
    return sorted

random_sorted = merge_sort(random_integers)
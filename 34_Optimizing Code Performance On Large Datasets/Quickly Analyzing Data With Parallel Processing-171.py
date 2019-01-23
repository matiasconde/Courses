## 1. Movie Quotes Data ##

with open("lines/theprincessbride.txt","r") as f: print(f.read())
with open("lines/theroadwarrior.txt","r") as w: print(w.read())
with open("lines/shallowgrave.txt","r") as q: print(q.read())

## 2. The Concurrent Futures Package ##

import math
import concurrent.futures
numbers = [1,10,20,50]

def sqrt(number):
    return math.sqrt(number)

pool = concurrent.futures.ProcessPoolExecutor(max_workers=5)
roots = list(pool.map(sqrt,numbers))

print(roots)

## 3. Reading In Files ##

import concurrent.futures
import os

files = os.listdir("lines")

def counter_func(path):
    with open("lines/"+path,"r") as f: 
        counter = 0
        for line in f: 
            counter += 1
        return counter
  
pool = concurrent.futures.ThreadPoolExecutor(max_workers=5)
lenghts = list(pool.map(counter_func,files))

movie_lengths = {}

for i,file in enumerate(files):
    movie_lengths[file] = lenghts[i]
max_lines = max(lenghts)

for k,v in movie_lengths.items():
    if v == max_lines: 
        most_lines = k
        m = v
        
        
print(most_lines,m)
    




## 4. Finding The Longest Lines ##

import concurrent.futures

files = os.listdir("lines")

def longest_line(path): 
    with open("lines/"+path,"r") as f: 
        length_line = 0
        for line in f: 
            if len(line)>length_line:
                long_line = line
                length_line = len(line)
        return (length_line,long_line,path)
    
pool = concurrent.futures.ThreadPoolExecutor(max_workers=5)
results = list(pool.map(longest_line,files))

maximo = 0
for result in results: 
    if result[0] > maximo:
        maximo = result[0]
        max_movie = result[2]
        max_line = result[1]
        
longest_line_movie = max_movie
longest_line = max_line
        
        
            

## 5. Finding The Most Commonly Used Word ##

import concurrent.futures
import time

def function(filename): 
    with open(filename,"r") as f:
        words = f.read().split(" ")
    from collections import Counter
    return Counter(words).most_common()[0][0]
    
start = time.time()
pool = concurrent.futures.ProcessPoolExecutor(max_workers=5)

filenames = ["lines/{}".format(path) for path in os.listdir("lines")]

results = list(pool.map(function,filenames))

common_words = {}

for i in range(len(filenames)):
    common_words[filenames[i].replace("lines/","")] = results[i]
    
end = time.time()
print(end - start)

## 7. Debugging Errors ##

import concurrent.futures
from collections import Counter

def most_common_word(filename):
    with open(filename) as f:
        words = f.read().split(" ")
    count = Counter(words)

    return count.most_common()[0][0]

results = []
pool = concurrent.futures.ProcessPoolExecutor(max_workers=2)
filenames = ["lines/{}".format(f) for f in os.listdir("lines")]
words = pool.map(most_common_word, filenames)
words = list(words)

common_words = {}
for i in range(len(lengths)):
    common_words[filenames[i].replace("lines/", "")] = words[i]

## 8. Removing Punctuation ##

import concurrent.futures

import os

def most_common_word(filename):
    with open(filename) as f:
        data = f.read().lower()
    import re
    data = re.sub("\W+", " ", data)
    words = data.split(" ")
    words = [w for w in words if len(w) >= 5]
    from collections import Counter
    count = Counter(words)
    return count.most_common()[0][0]


results = []
start = time.time()
pool = concurrent.futures.ProcessPoolExecutor(max_workers=2)
filenames = ["lines/{}".format(f) for f in os.listdir("lines")]
words = pool.map(most_common_word, filenames)
words = list(words)

common_words = {}
for i in range(len(words)):
    common_words[filenames[i].replace("lines/", "")] = words[i]
end = time.time()

print(end - start)


## 9. Finding Word Frequencies ##

def word_frequencies(filename):
    with open(filename) as f:
        data = f.read().lower()
    import re
    data = re.sub("\W+", " ", data)
    words = data.split(" ")
    words = [w for w in words if len(w) >= 5]
    from collections import Counter
    count = Counter(words)
    return dict(count)

start = time.time()
results = []
#pool = concurrent.futures.ProcessPoolExecutor(max_workers=2)
filenames = ["lines/{}".format(f) for f in os.listdir("lines")]
word_counts = list(pool.map(word_frequencies, filenames))

total_word_counts = {}
for element in word_counts:
    for k,v in element.items():
        if k not in total_word_counts:
            total_word_counts[k] = 0
        total_word_counts[k] += v
            
top_200 = Counter(total_word_counts).most_common(200)
end = time.time()

print(end-start)
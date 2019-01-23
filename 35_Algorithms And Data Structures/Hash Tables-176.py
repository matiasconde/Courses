## 2. Hash Tables ##

import os
quotes = {}

list_of_files = os.listdir("lines")

for file in list_of_files: 
    with open("lines/"+file,"r") as f:
        quotes[file.replace(".txt","")] = f.read()
        

## 3. Hash Functions ##

def simple_hash(key):
    string = str(key)
    string = string[0]
    return ord(string)

xmen_hash = simple_hash("xmen")
things_hash = simple_hash("10thingsihateaboutyou")

## 4. Fitting Values Into An Array ##

def simple_hash(key):
    key = str(key)
    return ord(key[0])%20

xmen_hash = simple_hash("xmen")
things_hash = simple_hash("10thingsihateaboutyou")





## 5. Creating A Hash Table ##

import numpy as np

def simple_hash(key):
    key = str(key)
    code = ord(key[0])
    return code % 20

class HashTable():
    
    def __init__(self, size):
        self.array = np.empty(size,dtype=np.object)
        
    
    def __getitem__(self, key):
        position = simple_hash(key)
        return self.array[position]
    
    def __setitem__(self, key, value):
        position = simple_hash(key)
        self.array[position] = value
        
f = open("lines/xmen.txt","r")         
hash_table = HashTable(20)
hash_table["xmen"] = f.read()
        

## 6. Hash Collisions ##

class HashTable():
    
    def __init__(self, size):
        self.array = np.zeros(size, dtype=np.object)
        self.size = size
    
    def __getitem__(self, key):
        ind = simple_hash(key)
        return self.array[ind]
    
    def __setitem__(self, key, value):
        ind = simple_hash(key)
        if type(self.array[ind]) != list:
            self.array[ind] = []
        self.array[ind].append(value)
            
hash_table = HashTable(20)
hash_table["xmen"] = open("lines/xmen.txt","r").read()
hash_table["xmenoriginswolverine"] = open("lines/xmenoriginswolverine.txt","r").read()

            

## 7. Retrieving Values From Hash Tables ##

class HashTable():
    
    def __init__(self, size):
        self.array = np.zeros(size, dtype=np.object)
        self.size = size
    
    def __getitem__(self, key):
        ind = simple_hash(key)
        tuples = self.array[ind]
        for tupla in tuples: 
            if key == tupla[0]: 
                return tupla[1]
            
    def __setitem__(self, key, value):
        ind = simple_hash(key)
        if not isinstance(self.array[ind], list):
            self.array[ind] = []
        self.array[ind].append((key,value))

hash_table = HashTable(20)
hash_table["xmen"] = open("lines/xmen.txt","r").read()
hash_table["xmenoriginswolverine"] = open("lines/xmenoriginswolverine.txt","r").read()


## 8. Overwriting Values ##

class HashTable():
    
    def __init__(self, size):
        self.array = np.zeros(size, dtype=np.object)
        self.size = size
    
    def __getitem__(self, key):
        ind = simple_hash(key)
        for k,v in self.array[ind]:
            if key == k:
                return v
    
    def __setitem__(self, key, value):
        ind = simple_hash(key)
        if not isinstance(self.array[ind], list):
            self.array[ind] = []
        replace = None
        for i,tupla in enumerate(self.array[ind]):
            if tupla[0] == key:
                replace = i
        if replace is None: 
            self.array[ind].append((key,value))
        else:
            self.array[ind][replace] = (key,value)
            
hash_table = HashTable(20)
hash_table["xmen"] = open("lines/xmen.txt","r").read()
hash_table["xmen"] = open("lines/xmenoriginswolverine.txt","r").read()
            

## 9. Profiling Hash Tables ##

def simple_hash(key):
    key = str(key)
    code = ord(key[0])
    return code % 1

class HashTable():
    
    def __init__(self, size):
        self.array = np.zeros(size, dtype=np.object)
        self.size = size
    
    def __getitem__(self, key):
        counter = 0
        ind = simple_hash(key)
        for k,v in self.array[ind]:
            counter += 1
            if key == k:
                return counter
    
    def __setitem__(self, key, value):
        ind = simple_hash(key)
        if not isinstance(self.array[ind], list):
            self.array[ind] = []
        replace = None
        for i,data in enumerate(self.array[ind]):
            if data[0] == key:
                replace = i
        if replace is None:
            self.array[ind].append((key,value))
        else:
            self.array[ind][replace] = (key, value)

data = [
    ("xmen", "Wolverine"), 
    ("xmenoriginswolverine", "Superman"), 
    ("vanillasky", "Thor"), 
    ("tremors", "Aquaman"),
]

hash_table = HashTable(1)
for tupla in data: 
    hash_table[tupla[0]] = tupla[1]
    
counter = hash_table["tremors"]


## 10. Profiling Array Length ##

import time
import os
import matplotlib.pyplot as plt

class HashTable():
    
    def __init__(self, size):
        self.array = np.zeros(size, dtype=np.object)
        self.size = size
    
    def __getitem__(self, key):
        ind = hash(key)%self.size
        for k,v in self.array[ind]:
            if key == k:
                return v
    
    def __setitem__(self, key, value):
        ind = hash(key)%self.size
        if not isinstance(self.array[ind], list):
            self.array[ind] = []
        replace = None
        for i,data in enumerate(self.array[ind]):
            if data[0] == key:
                replace = i
        if replace is None:
            self.array[ind].append((key,value))
        else:
            self.array[ind][replace] = (key, value)

def profile_table(size):
    start = time.time()
    hash_table = HashTable(size)
    directory = "lines"
    
    for filename in os.listdir(directory):
        name = filename.replace(".txt", "")
        hash_table[name] = quotes[name]
    duration = time.time() - start
    return duration
    
lengths = [1,10,20,30,40,50]
times = []
for length in lengths: 
    times.append(profile_table(length))
plt.plot(lengths,times)
plt.show()
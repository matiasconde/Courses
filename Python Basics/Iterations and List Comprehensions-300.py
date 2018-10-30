## 1. Introduction ##

import csv

music = list(csv.reader(open("top100.csv")))

print(music[:5])

artists = []

for song in music[1:]:
    artists.append(song[1])

## 2. Extract the Artists using a List Comprehension ##

artists = []
for row in music[1:]:
    artists.append(row[1])
    
artists_lc = [song[1] for song in music[1:]]

## 3. Getting the Artist Count using a function ##

def counter(lista):
    dic = {}
    for item in lista:
        if item in dic:
            dic[item] += 1
        else: dic[item] = 1
    return dic

counts = counter(artists)

## 4. Getting the artist count using Counter() ##

from collections import Counter
artist_counts = Counter(artists)

## 5. Looping through our counts using the items() method ##

artist_counts = []
for key, value in counts.items():
    artist_counts.append([key,value])

## 6. Using a List Comprehension ##

artist_counts = []
for key, value in counts.items():
    artist_counts.append([key,value])
artist_counts_two = [[key,value] for key,value in counts.items()]

## 7. Sorting our list of lists to extract the top value ##

artist_counts.sort()
top_artist = artist_counts[0]

## 8. Specifying a key when sorting our list ##

def by_count(lista):
    return lista[1]
    
artist_counts.sort(key=by_count,reverse=True)


## 9. Creating a function using lambda ##

f = open("top100.csv","r")
music = list(csv.reader(f))
artists = []
for row in music[1:]:
    artists.append(row[1])
from collections import Counter
artist_dict = Counter(artists)
artist_counts = [[key,value] for key,value in artist_dict.items()]
artist_counts.sort(key=lambda x: x[1], reverse=True)

## 10. Creating a Pipeline using Modularization ##

from collections import Counter 

f = open("top100.csv","r")
music = list(csv.reader(f))
artists = [row[1] for row in music[1:]]
artist_dict = Counter(artists)
artist_counts = [[key,value] for key,value in artist_dict.items()]
artist_counts.sort(key=lambda x: x[1], reverse=True)

# Uncomment when ready!
# artists = extract_artist(music)
# artist_counts = get_count(artists)
# top = sort_by_streams(artist_counts)
def extract_artist(filename):
    return [row[1] for row in music[1:]]

def get_count(artists):
    artist_dict = Counter(artists)
    return [[key,value] for key,value in artist_dict.items()]

def sort_by_streams(artist_counts):
    artist_counts.sort(key=lambda x: x[1], reverse=True)
    return artist_counts
    
artists = extract_artist(music)
artist_counts = get_count(artists)
top = sort_by_streams(artist_counts)

## 11. How to deal with errors ##

cleaned_list = []
for item in music_sample[1:]:
    try:
        cleaned_list.append([item[0],item[1],float(item[3])])
    except:
        "Pass"

## 12. Passing new data into our pipeline ##

f = open("top100.csv","r")
music_all = list(csv.reader(f))

from collections import Counter

def extract_artist(music):
    return [row[1] for row in music[1:]]

def get_count(artists):
    artist_dict = Counter(artists)
    return [[key,value] for key,value in artist_dict.items()]

def sort_by_streams(artist_counts):
    artist_counts.sort(key=lambda x: x[1], reverse=True)
    return artist_counts

# Add your code here
artists = extract_artist(music_all)
artist_counts = get_count(artists)
top = sort_by_streams(artist_counts)
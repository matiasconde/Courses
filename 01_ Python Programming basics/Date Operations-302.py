## 1. Introduction ##

import csv

f = open("global_rankings.csv","r")
music = list(csv.reader(f))
print(music)

## 2. Using the datetime module ##

from datetime import datetime
jan_27_1965 = datetime(1965,1,27,12,43)
aug_3_1972 = datetime(1972,8,3,1,43)
oct_31_2000 = datetime(2000,10,31,15,12)
mar_2_2017 = datetime(2017,3,2,7,30)

## 3. Creating a datetime object using a string ##

from datetime import datetime

date1 = "6-02-2008"
jun_2_08 = datetime.strptime(date1,"%m-%d-%Y")

date2 = "7?15?2001"
jul_15_01 = datetime.strptime(date2,"%m?%d?%Y")

date3 = "12--30--2010"
dec_20_08 = datetime.strptime(date3,"%m--%d--%Y")

## 4. Converting the string column into a datetime column ##

from datetime import datetime

def string_to_date(dataset):
    new_list = []
    for i,item in enumerate(music):
        if i>=1:
            new_date = datetime.strptime(item[-2],"%Y-%m-%d")
            new_list.append(new_date)
            item[-2] = new_date
    return dataset[1:]

cleaned_music = string_to_date(music)


## 5. Extracting the month from the date object ##

def get_month(dataset):
    new_list = []
    for i,item in enumerate(dataset):
        item.append(item[-2].month)
        new_list.append(item)
    return new_list

add_month = get_month(cleaned_music)
     

## 6. Extracting the day from the date object ##

def get_day(dataset):
    new_list = []
    for item in dataset:
        item.append(item[-3].day)
        new_list.append(item)
    return new_list

add_day = get_day(add_month)
            

## 7. Grouping and aggregating our data ##

def organize_by_month(cleaned_music):
    months = [1,2,3,4,5,6,7,8,9,10,11,12]
    
    organized = dict()
    for month in months:
        tracks_in_month = []
        for track in cleaned_music:
            if track[-2] == month:
                tracks_in_month.append(track)
        organized[month] = tracks_in_month
    return organized

def aggregate(organized):
    months = [1,2,3,4,5,6,7,8,9,10,11,12]
    monthly_sum = dict()

    for month in months:
        tracks = organized[month]
        # Need the track name, artist and number of streams
        groups = dict()
        for t in tracks:
            track_name = t[2]
            if track_name not in groups.keys():
                groups[track_name] = int(t[3])
            else:
                groups[track_name] += int(t[3])
        monthly_sum[month] = groups
    return monthly_sum

organized = organize_by_month(add_day)
aggregated = aggregate(organized)

#print(organized)
print(aggregated)

## 8. Finding the top artist for each group ##

months = [1,2,3,4,5,6,7,8,9,10,11,12]

top_songs_by_month = []          
for month in months:
    sorted_dict = sorted(aggregated[month].items(),key = lambda x: x[1], reverse=True)
    top_songs_by_month.append(sorted_dict[0])
    
    
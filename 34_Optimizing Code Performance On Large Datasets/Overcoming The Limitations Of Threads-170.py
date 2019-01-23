## 1. The GIL ##

import threading
import time
import statistics

def open_file(path):
    file = open(path,"r")
    #reader = csv.reader(file)
    
times = []
for i in range(100):
    s1 = time.time()
    open_file("Emails.csv")
    s2 = time.time()
    times.append(s2-s1)

threaded_times = []


for i in range(100):
    s1 = time.time()
    t1 = threading.Thread(target=open_file,args=("Emails.csv",))
    t2 = threading.Thread(target=open_file,args=("Emails.csv",))
    t1.start()
    t2.start()
    s2 = time.time()
    threaded_times.append(s1 - s1)
    
print(sum(times)/len(times), "simple timing")
      
print(sum(threaded_times)/len(threaded_times), "threaded timing")
      
# Hola, te interesaría ir a tomar algo? o no tengo ninguna chance?



## 4. Clinton Emails ##

import pandas
import time

emails = pandas.read_csv("Emails.csv")
capital_letters = []

start = time.time()
for email in emails["RawText"]:
    total_capital = sum([letter.isupper() for letter in email])
    capital_letters.append(total_capital)
end = time.time()
total = end - start

print(total)
    

## 6. How The GIL Works ##

import threading

capital_letters1 = []
capital_letters2 = []

def counts_capital(start,finish,capital_letters):
    for element in emails["RawText"][start:finish]:
        count = sum([letter.isupper() for letter in element])
        capital_letters.append(count)

time1 = time.time()
t1 = threading.Thread(target = counts_capital, args = (0,3972,capital_letters1,))
t2 = threading.Thread(target = counts_capital, args = (3972,7946,capital_letters2,))

t1.start()
t2.start()

t1.join()
t2.join()

time2 = time.time()

total = time2 - time1
print(total)        

## 9. Multiprocessing ##

import threading
import multiprocessing

capital_letters1 = []
capital_letters2 = []

def counts_capital(start,finish,capital_letters):
    for element in emails["RawText"][start:finish]:
        count = sum([letter.isupper() for letter in element])
        capital_letters.append(count)

time1 = time.time()
m1 = multiprocessing.Process(target = counts_capital, args = (0,3972,capital_letters1,))
m2 = multiprocessing.Process(target = counts_capital, args = (3972,7946,capital_letters2,))

m1.start()
m2.start()

m1.join()
m2.join()

time2 = time.time()

total = time2 - time1
print(total)       
print(capital_letters)

## 11. Multiple Cores ##

import threading
import multiprocessing

def counts_capital(start,finish):
    for element in emails["RawText"][start:finish]:
        count = sum([letter.isupper() for letter in element])

time1 = time.time()

m1 = multiprocessing.Process(target = counts_capital, args = (0,1986,))
m2 = multiprocessing.Process(target = counts_capital, args = (1986,3972,))
m3 = multiprocessing.Process(target = counts_capital, args = (3972,5958,))
m4 = multiprocessing.Process(target = counts_capital, args = (5958,7946,))

m1.start()
m2.start()
m3.start()
m4.start()

m1.join()
m2.join()
m3.join()
m4.join()

time2 = time.time()

total = time2 - time1
print(total)       

## 13. Inter-Process Communication ##

import multiprocessing

def count_capital_letters(email):
    return len([letter for letter in email if letter.isupper()])

def count_capitals_in_emails(start, finish, capital_letters,conn):
    for email in emails["RawText"][start:finish]:
        capital_letters.append(count_capital_letters(email))
    conn.send(capital_letters)
    conn.close()
    
capital_letters1 = []
capital_letters2 = []

start = time.time()
parent_conn1, child_conn1 = multiprocessing.Pipe()
parent_conn2, child_conn2 = multiprocessing.Pipe()

p1 = multiprocessing.Process(target=count_capitals_in_emails, args=(0, 3972,capital_letters1,child_conn1))
p2 = multiprocessing.Process(target=count_capitals_in_emails, args=(3972, 7946,capital_letters2,child_conn2))
p1.start()
p2.start()

for process in [p1, p2]:
    process.join()

capital_letters1 = parent_conn1.recv()
capital_letters2 = parent_conn2.recv()

total = time.time() - start

print(total)
print(capital_letters1)

## 15. Worker Pools ##

from multiprocessing import Pool
import time

def counts_capital(email):
    return sum([letter.isupper() for letter in email])
        
time1 = time.time()
p = Pool(2)

capital_letters = p.map(counts_capital,emails["RawText"])


time2 = time.time()

total = time2 - time1
print(total) 
import string
"""
#exaple of tuples

import math

def multivariable(a,b):
    dist1 = math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)
    dist2 = a+b
    return dist1,dist2

a = (1,2)
b = (2,4)

print(multivariable(a,b))
"""
""" #listas anidadas
students = [
("John", ["CompSci", "Physics"]),
("Vusi", ["Maths", "CompSci", "Stats"]),
("Jess", ["CompSci", "Accounting", "Economics",
"Management"]),
("Sarah", ["InfSys", "Accounting", "Economics", "CommLaw"]),
("Zuki", ["Sociology", "Economics", "Law", "Stats","Music"])]

cont = 0

for name,subject in students:
    if "CompSci" in subject:
        cont +=1
print(cont)
"""
#1
"""
>>> list(range(10,0,-2))
[10, 8, 6, 4, 2]
>>> list(range(0,10,-2))
[]
>>> list(range(0,10,2))
[0, 2, 4, 6, 8]
>>> range(start,stop,step) si start<stop para que no sea vacia debe ser step>0
si stop<start  para que no sea vacia debe ser step<0
"""

#2 Creo que al hacer una asignación a alex desde tess, ambos son
# la misma tortuga, es decir, apuntan al mismo objeto, luego si cambio
# el color de alex, tess va a tener el mismo color
# esto que acabo de escribir está probado

#3
"""
>>> a = [1,2,3]
>>> b = a[:]
>>> b[0]=5
>>> a
[1, 2, 3]
>>> b
[5, 2, 3]
>>>
"""
"""
#4
this = ["I", "am", "not", "a", "crook"]
that = ["I", "am", "not", "a", "crook"]
print("Test 1: {0}".format(this is that))
that = this
print("Test 2: {0}".format(this is that))

#en el Test 1 tengo dos objetos distintos
# en el Test 2 le asigne a un value el objeto del otro, con lo cual apuntan al mismo



#5
# se creó el archivo "vectors.py"

#ejercicios 6 a 8 están en el archivo "vectors.py" ya que forman parte de algo que se v a usar después


#9
song = "The rain in Spain..."
song2 = " ".join(song.split())

song3 = "The       raininSpain..." #en este caso son diferentes
song4 = " ".join(song3.split())    #porque split ignora cualquier cantidad de espacios
# pero join esta seteado para juntarlos con un solo espacio.

print(song)
print(song2)

print(song3)
print(song4)

#10
def replace(s,old,new):
    a = s.split(old)
    return new.join(a)

print(replace("Mississippi", "i", "I"))

song5 = "I love spom! Spom is my favorite food. Spom, spom, yum!"
print(replace(song5, "om", "am"))

print(replace(song5, "o", "a"))

#1
import string

a = str(input("ingrese palabra o texto: ",))

a_lower = a.lower()
b = list(a_lower)
b.sort()
inventory_of_letters = {}

for letter in b:
    inventory_of_letters[letter] = inventory_of_letters.get(letter,0)+1

for key in inventory_of_letters:
    print("{0:>5} {1:>5}".format(key,inventory_of_letters[key]))

"""
"""
#1
import string

a = str(input("ingrese palabra o texto: ",))

a_lower = a.lower()
b = list(a_lower)
b.sort()
inventory_of_letters = {}

for letter in b:
    inventory_of_letters[letter] = inventory_of_letters.get(letter,0)+1

for key in inventory_of_letters:
    print("{0:>5} {1:>5}".format(key,inventory_of_letters[key]))



#2

def add_fruit(new_inventory,fruit,q = 0):
    new_inventory[fruit] = q
    return new_inventory

new_inventory = {}
add_fruit(new_inventory, "strawberries", 10)
print(new_inventory)
print(("strawberries" in new_inventory))
print(new_inventory["strawberries"] == 10)
add_fruit(new_inventory, "strawberries", 25)
print(new_inventory["strawberries"] == 35)

"""

#3
import time
import string

t0 = time.clock()

with open("Alice_wonder_lands.txt") as libro:

    contenido = libro.read()


contenido1 = contenido.lower()
contenido2 = ""
for letter in contenido1:
    if letter not in string.punctuation:
        contenido2 += letter

words = contenido2.split()
inventory_words = {}
words.sort()
print(words)

for word in words:
    inventory_words[word] = inventory_words.get(word,0)+1



print("{0:<20}{1:<20}".format("Word","Count"))
print("=========================")
for key in inventory_words.keys():
    print("{0:<20}{1:<20}".format(key,inventory_words[key]))

t1 = time.clock()

print(t0,t1,t1-t0)
print(inventory_words)

print("the word alice occurs ",inventory_words["alice"]," in the book")

max = "a"

for key in inventory_words.keys():
    if len(key)>len(max):
        max = key
print("la palabra mas larga es: ",max,"cuya longitud es: ",len(max))






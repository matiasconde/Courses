"""
#probando cap
import random as rng
import time
import vectors as v
from math import pi,e
print(v.scalar_mult(3,[pi,1]))
print(v.dot_product(v.cross_product([3,2,e],[e,e,pi]),[3,2,e]))

trow_dice = rng.randrange(1,7)
random_even = rng.randrange(0,100,2)

drng = rng.Random(30)
a = drng.randrange(10)
b = drng.randrange(10)
c = rng.randrange(10)
d = rng.randrange(10)

print("lista de randoms",a,b,c,d)

t0 = time.clock()

def make_a_random_list(num,lower,upper): #OJO QUE ACÁ SE PERMITEN REPETIDOS, OSEA ES CON REPOSICIÓN

    random_list = []
    for x in range(num):
        random_list.append(rng.randrange(lower,upper))
    return random_list

print(make_a_random_list(10,1,100))

t1 = time.clock()

randomlist_precaria = list(range(1,100))
rng.shuffle(randomlist_precaria)
print(randomlist_precaria[20:30])

t2 = time.clock()

candidato = "PIJA"

def make_a_random_list_norep(num,lower,upper):
    global candidato
    random_listnorep = []
    for x in range(num):
        while True:
            candidato = rng.randrange(lower,upper)
            if candidato not in random_listnorep:
                break
        random_listnorep.append(candidato)
    return random_listnorep

print(candidato)
print(make_a_random_list_norep(10,1,100))

t3 = time.clock()

print(t1-t0,t2-t1,t3-t2)

cards = list(range(52))
rng.shuffle(cards)
print(cards)

t4 = time.clock()
a = list(range(101))
print(sum(a))
t5 = time.clock()

b = 0
for x in range(101):
    b += x

print(b)
t6 = time.clock()

print(100*101/2)

t7 = time.clock()

print(t5-t4,t6-t5,t7-t6)

print(v.seq_tool(["asas","22",3,4,4,5,5],4))

from math import *

print(cos(pi))

# PARA OBTENER LA AYUDA COLOCAR: help() enter, nombre del modulo, enter. o simplemente probar
# dentro de help(calendar.TextCalendar()) por ejemplo

1#
#a
import calendar
#a
cal = calendar.TextCalendar()
#cal.pryear(2012)

#b
cal = calendar.TextCalendar(3)
#cal.pryear(2012,w=0,l=0,c=6,m=3)

#c
cal.prmonth(2017,5)
#d
d = calendar.LocaleTextCalendar(6,"chinese") #si se coloca un idioma no soportado, sala el error en el módulo de la libreria de python 3.6
d.pryear(2012)

import calendar
print(calendar.isleap(2013)) #no es bisiesto
print(calendar.isleap(2012)) #es bissesto

# retorna un valor boobleano, es una función de estado

#2
#a
import math

with open("funciones de math en python 36.txt","r") as file:
    all_lines = file.readlines()
    cont = 0
    for line in all_lines:
        if line[0:4]=="    ":
            if line[0:5] != "     ":
                cont += 1
                print(line[0:10])
print("there are, ", cont," functions in math module")

#b
a = float(input("ingrese número real: ",))
print(math.ceil(a)) #devuelve el menor entero mayor o igual que a (el techo)
print(math.floor(a)) #devuelve el mayor entero menor o igual que a (el piso)

#c
# se calculó con el método de newton.
import math
import time

a = float(input("ingrese número real: ",))

def raíz_cuadrada_casera(num):
    result = num
    for _ in range(13):
        result = result - (result**2-num)/(2*result)
    return result
t0 = time.clock()
print(raíz_cuadrada_casera(a))
t1 = time.clock()

t2 = time.clock()
print(math.sqrt(a))
t3 = time.clock()

tiempo_casero = t1-t0
tiempo_builtin = t3-t2

print("{0:.10f}   {1:.10f}".format(tiempo_casero,tiempo_builtin))
print("si la diferencia de tiempos es positiva, quiere decir que tarda más el método casero: ",tiempo_casero-tiempo_builtin)

#the two data constant in math module are e and pi
print(math.e,math.pi)

#3
import copy
x = [1,2,3]
y = copy.copy(x)
"""
"""

The difference between shallow and deep copying is only relevant for
    compound objects (objects that contain other objects, like lists or
    class instances).

    - A shallow copy constructs a new compound object and then (to the
      extent possible) inserts *the same objects* into it that the
      original contains.

    - A deep copy constructs a new compound object and then, recursively,
      inserts *copies* into it of the objects found in the original.
"""
#pudo haber sido útil en el ejercicio 3 del capítulo 7 sobre "files"

#4
# Realizado con los módulos :  mymodule1.py mymodule2.py y namespace_test.py

#5  el comando este imprime "main" como nombre por defecto del módulo
# o archivo en curso, pero al importar otros módulos que tambíen imprimen
# su __name__ en el módulo imprimirá "main" pero en el importando (al que le estamos importando módulos)
# va a imprimir el nombre del módulo importado

# NOMBRE __name__ por default a un módulo es "__main__"

#6
import this
"""
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""

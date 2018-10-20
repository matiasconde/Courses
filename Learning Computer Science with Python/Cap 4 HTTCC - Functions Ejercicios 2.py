
"""
#1
def turn_clockwise(C):
    a = ["N", "E", "S", "W", "N"]
    for index,value in enumerate(a):
        if C == a[index]:
            return a[index+1]

Q=str(input("ingrese punto cardinal: ",))
print(turn_clockwise(Q))


#2
def day_name(q):
    a=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    return a[int(q)]

q=int(input("ingrese día en numeros del 0 al 6: ",))
print(day_name(q))



#3
def day_num(q):
    a = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    for i,v in enumerate(a):
        if q == a[i]:
            return i
Q=str(input("ingrese día de la semana: ",))
print(day_num(Q))



#4
def day_num(q):
    a = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    for i,v in enumerate(a):
        if q == a[i]:
            return i

def deltaday(day,delta):
    resday = day + delta%7
    return resday

def day_name(q):
    a=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    return a[int(q)]

a = str(input("ingrese día: "),)
b = int(input("ingrese delta: "),)

print("usted retornará el: ",day_name(deltaday(day_num(a),b)))



#5

def day_num(q):
    a = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    for i,v in enumerate(a):
        if q == a[i]:
            return i

def deltaday(day,delta):
    if delta<0:
        delta1=(-delta)%7
        resday = day - delta1
    else:
        resday = day + delta
    return resday

def day_name(q):
    a=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    return a[int(q)]

a = str(input("ingrese día: "),)
b = int(input("ingrese delta: "),)

print("usted retornará el: ",day_name(deltaday(day_num(a),b)))



#6
A=[("January",31),("February",28),("March",31),("April",30),("May",31),("June",31),("July",30),("August",31),("September",30),("October",31),("November",30),("December",31)]

def day_in_month(namemonth):
    for value in A:
        if namemonth == value[0]:
            return value[1]

b=str(input("ingrese por teclado mes: "),)
print("su mes ingresado tiene: ",day_in_month(b),"días")



#7
def to_secs(hours,minutes,seconds):
    return hours*3600+minutes*60+seconds

a=int(input("ingrese total de horas: "))
b=int(input("ingrese total de minutos: "))
c=int(input("ingrese total de segundos: "))

print(to_secs(a,b,c))



#8
def to_secs2(hours,minutes,seconds):
    return hours*3600+minutes*60+seconds

a=float(input("ingrese total de horas: "))
b=float(input("ingrese total de minutos: "))
c=float(input("ingrese total de segundos: "))

print(int(to_secs2(a,b,c)))



#9
def hours_in(secs):
    tot = secs/3600
    return int(tot)

def minutes_in(secs):
    tot = (secs%3600)/60
    return int(tot)

def seconds_in(secs):
    tot = (secs%3600)%60
    return tot

c=float(input("ingrese total de segundos: ",))
print(hours_in(c))

d=float(input("ingrese total de segundos: ",))
print(int(minutes_in(d)))

w=float(input("ingrese total de segundos: ",))
print(seconds_in(w))



#10
#trivial

#11
def compare(a,b):
    if a<b:
        return -1
    elif a>b:
        return 1
    else:
        return 0
a = int(input("ingrese números: "))
b = int(input("ingrese números: "))
print(compare(a,b))

#12
import math

def hypotenuse(a,b):
    return math.sqrt(a*a+b*b)

a = float(input("ingrese números: "))
b = float(input("ingrese números: "))
print(hypotenuse(a,b))



#13

def slope(x1,y1,x2,y2):
    return (y2-y1)/(x2-x1)

x1 = float(input("ingrese número x1: "))
y1 = float(input("ingrese número y1: "))
x2 = float(input("ingrese número x2: "))
y2 = float(input("ingrese número y2: "))

print(slope(x1,y1,x2,y2))



#14
def is_even(n):
    return n%2==0

x1 = float(input("ingrese número x1: "))
print(is_even(x1))

#15
def is_odd(n):
    return not is_even(n)

x1 = float(input("ingrese número x1: "))
print(is_odd(x1))



#16
def is_factor(f,n):
    if f<n:
        return n%f==0
    else:
        return f%n==0

print(is_factor(3, 12))
print(not is_factor(5, 12))
print(is_factor(7, 14))
print(not is_factor(7, 15))
print(is_factor(1, 15))
print(is_factor(15, 15))
print(not is_factor(25, 15))



#17
def is_factor(f,n):
    if f<n:
        return n%f==0
    else:
        return f%n==0

def is_multiple(a,b):
    return is_factor(b,a)

print(is_multiple(12, 3))
print(is_multiple(12, 4))
print(not is_multiple(12, 5))
print(is_multiple(12, 6))
print(not is_multiple(12, 7))



#18

def f_to_c(TF):
    return ((TF - 32 )/1.8)

x = float(input("ingrese número x: "),)
print(x)

print(int(f_to_c(212)),"\n",
int(f_to_c(32)),"\n",
int(f_to_c(-40)),"\n",
int(f_to_c(36)),"\n",
int(f_to_c(37)),"\n",
int(f_to_c(38)),"\n",
int(f_to_c(39)))

def c_to_f(TC):
    return (TC*1.8+32)

x = float(input("ingrese número x: "),)
print(x)

print(int(f_to_c(212)),
int(f_to_c(32)),"\n",
int(f_to_c(-40)),"\n",
int(f_to_c(36)),"\n",
int(f_to_c(37)),"\n",
int(f_to_c(38)),"\n",
int(f_to_c(39))),"\n",
print ((c_to_f(0)),"\n"
,int(c_to_f(100)),"\n"
,int(c_to_f(-40)),"\n"
,int(c_to_f(12)),"\n"
,int(c_to_f(18)),"\n"
,int(c_to_f(-48)))


import string

#function find

a = str(input("ingrese texto donde está la URL: ",))

def extract_URL(text):
    i = text.find("https://")
    url = ""
    for index,value in enumerate(text):
        if i<=index:
            if index != "":
                url +=text[index]
    return url

print(extract_URL(a))

# probar con sadsadddddddsd sdadasdasd a dasdasd https://www.google.com.ar/search?q=sueldo+decano+utn&oq=sueldo+decano+utn&aqs=chrome..69i57.2191j0j7&sourceid=chrome&ie=UTF-8 .

b = str(input("ingrese texto con <...>: ",))

def extract_(text):
    i = text.find("<")
    j = text.find(">")
    extraction = ""
    for index, value in enumerate(text):
        if i < index < j:
            extraction += text[index]
    return extraction

print(extract_(b))

#probar con dasdasdsjonjsdoncpjm<wally>asdopfmpcdskmcsdñcmsdñlcsdasdcssdcsd


import string

a="jklmnopq"
suffix = "ack"

for index,p in enumerate(a):
    a=a.upper()
    if p != "q":
        print(a[index]+suffix)
    else:
        print(a[index]+"u"+suffix)

"""

import string

letter = "sadsssadsd {0} asdsadasdasds, adasds{1}"

print(letter.format("AAA","BBB"))

PI = "Pi hasta 3 decimales es {0:.20f}"  #MIRÁ ESTO MATY, .3f es .3float

import math

print(PI.format(math.pi+0.2222222222222222222222222222222222222222222222222222222222222222))

print(math.pi)

print("|||| {0:>20} |||{1:^7} || {2:<30} ".format("AAA","BBB","CCC"))

#{0:^20} GENERA UN RANGO DE 20 ESPACIOS Y COLOCA EL TEXTO EN EL MEDIO.


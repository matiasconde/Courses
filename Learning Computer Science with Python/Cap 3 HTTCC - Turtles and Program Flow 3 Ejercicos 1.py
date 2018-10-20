"""print(1e-8)
numbers=[83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50,49.9, 45, 44.9, 40, 39.9, 2, 0]
for x in numbers:
    if x>=75:
        print("First")
    elif 70<=x<75:
        print("Upper Second")
    elif 60<=x<70:
        print("Second")
    elif 50<=x<60:
        print("Third")
    elif 45<=x<50:
        print("F1 Supp")
    elif 40<=x<45:
        print("F2")
    elif x<40:
        print("F3")

a=float(input("ingrese primer lado recto: ",))
b=float(input("ingrese segundo lado recto: ",))
print("la hipotenusa es igual a: ", (a**2+b**2)**0.5)

a=float(input("ingrese primer lado: ",))
b=float(input("ingrese segundo lado: ",))
c=float(input("ingrese tercer lado: ",))
q=[(a**2+b**2)**0.5,(b**2+c**2)**0.5,(c**2+a**2)**0.5]
lím=1e-7
for _ in q:
    if abs(_-a)<lím or abs(_-b)<lím or abs(_-c)<lím:
        print("el triángulo es rectángulo")
else:
    print("el triángulo no es rectángulo")

print(1e-8)

import math
a=math.sqrt(2)
print(a,a*a)
print(a*a==2.0)

for _ in range(10):
    print("We like Python´s Turtles!!")

for a in ["January","February","March","April","May","June","July","August","September","October","November","December"]:
    print("One of the months of the year is ",a)

r=float(input("ingrese número de grados: ",))
contador=0
while (r)>360:
    r=r%360
    contador+=1
    print("el número de vueltas es: ",contador)

input("escriba un número para terminar")

numbers = [12, 10, 32, 3, 66, 17,42, 99, 20]

for _ in numbers:
    print(_, end="\n")

for _ in numbers:
    print(_,_*_, end="\n")


numbers = [12, 10, 32, 3, 66, 17,42, 99, 20]


total=0
for _ in numbers:
    total+=_
print(total)

total=1
for _ in numbers:
    total*=_
print(total)

"""

import turtle
"""
Joe=turtle.Turtle()

window=turtle.Screen()
window.bgcolor("white")
Joe.color("green")
Joe.shape("turtle")
Joe.pendown()
for _ in range(3):
    Joe.forward(50)
    Joe.left(120)
Joe.color("red")
for _ in range(4):
    Joe.forward(50)
    Joe.left(90)
Joe.color("blue")
for _ in range(6):
    Joe.forward(50)
    Joe.left(60)
Joe.color("lightblue")
for _ in range(8):
    Joe.forward(50)
    Joe.left(45)

input("ingrese cualquier cosa")
"""
"""
data=[160, -43, 270, -97, -43, 200, -940, 17, -86,222,123,221,321]
drunkp = turtle.Turtle()
window=turtle.Screen()
window.bgcolor("white")
for _ in data:
    drunkp.left(_)
    drunkp.forward(100)
r=sum(data)
while abs(r)>360:
    r=r%360
    print("el pirata borracho quedó apuntando con su cabeza a ",r,"grados")
else:
    print("el pirata borracho quedó apuntando con su cabeza a ",r,"grados")

q=0
numlados=int(input("¿cuantos lados tiene su polígono regular?: ",))
q=((numlados-2)*180)/numlados
print(q)
input("sias")

poligon = turtle.Turtle()
window=turtle.Screen()
window.bgcolor("white")
poligon.pendown()
poligon.color("blue")
for _ in range(numlados):
    poligon.left(180-q)
    poligon.forward(50)

star=turtle.Turtle()
star.speed(5)
star.hideturtle()
star.left(108)
for _ in range(5):
    star.left(144)
    star.forward(100)

star.showturtle()
star.color("red")
star.forward(35)
input("Sss")
"""
clock=turtle.Turtle()
clock.color("blue")
clock.shape("turtle")
clock.stamp()
clock.penup()
for _ in range(12):
    clock.forward(100)
    clock.stamp()
    clock.backward(100)
    clock.left(30)
input("SSS")

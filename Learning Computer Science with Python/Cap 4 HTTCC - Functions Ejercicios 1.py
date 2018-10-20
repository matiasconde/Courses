import turtle


def make_a_turtle(color,size,form):
    puntero=turtle.Turtle()
    puntero.pensize(size)
    puntero.shape(form)
    return puntero

def make_a_window(color,title):
    window=turtle.Screen()
    window.bgcolor(color)
    window.title(title)
    return window

def make_a_square(size):
    for _ in range(4):
        a.forward(size)
        a.left(90)

wd = make_a_window("white","workspace1")
a = make_a_turtle("blue",1,"classic")
"""
#1
for _ in range(5):
    make_a_square(50)
    a.penup()
    a.forward(100)
    a.pendown()

wd.mainloop()

#2
a.speed(50)
for _ in range(1,6):
    z = make_a_square(20+20*_)
    a.penup()
    a.right(90+45)
    a.forward((10 ** 2 + 10 ** 2) ** 0.5)
    a.left(90 + 45)
    a.pendown()

wd.mainloop()

#3
def draw_poly(n,sz):
    poligon = a
    q = ((n - 2) * 180)/n
    for _ in range(n):
        poligon.left(180 - q)
        poligon.forward(sz)

draw_poly(125,50)

#4
q=360/20
p = float(input("ingrese tamaño de forma: ",))
a.speed(10)
for _ in range(20):
    make_a_square(p)
    a.left(45)
   # a.penup()
    a.forward(((p/2)**2+(p/2)**2)**0.5)
    a.left(q)
    a.forward(-((p/2)**2+(p/2)**2)**0.5)
    a.right(45)
   # a.pendown()
    
wd.mainloop()

#5
a.right(90)
a.speed(7)
def spiral_square(size):
    n=2
    a.left(180)
    for _ in range(20):
        n+=10
        a.forward(n)
        a.right(90)

def crazy_spiral_square(size):
    n=2
    a.left(0)
    a.color("green")
    for _ in range(120):
        n+=2
        a.backward(n)
        a.right(89)


spiral_square(1)
crazy_spiral_square(0.1)
wd.mainloop()


#6
def draw_poly(n,sz):
    poligon = a
    q = ((n - 2) * 180)/n
    for _ in range(n):
        poligon.left(180 - q)
        poligon.forward(sz)

def draw_equitriangle(sz):
    draw_poly(3,sz)

draw_equitriangle(50)
wd.mainloop()

#7
def sum_to(n):
    tot=0
    for _ in range(n+1):
        tot+=_
    return(tot)

print(sum_to(10))

#8
import math

def area(r):
    return(math.pi*r*r)

print(area(5))


#9
def star(side):
    star=a
    star.left(108)
    for _ in range(5):
        star.left(144)
        star.forward(side)
    star.right(18)

star(100)
wd.mainloop()

"""
#10
def star(side):
    star=a
    star.left(108)
    for _ in range(5):
        star.left(144)
        star.forward(side)
    star.right(18+90)

def draw_poly(n,sz):
    poligon = a
    q = ((n - 2) * 180)/n
    for _ in range(n):
        star(100)
        poligon.left(180 - q)
      #  poligon.penup()
        poligon.forward(sz)
     #   poligon.pendown()
       # poligon.right(180-q)

def draw_starpoly(lados,sizep,sizestar):
    star(sizestar)
    draw_poly(lados,sizep)

draw_starpoly(10,200,100)

wd.mainloop()



#draw my first fractal

"""
import turtle
fract = turtle.Turtle()
window = turtle.Screen()
fract.speed(200)
fract2 = turtle.Turtle()
fract2.color("green")
fract2.shape("arrow")

def draw_fractal2(turt,size,order):

    if order == 0:
        turt.forward(size)
    else:
        draw_fractal2(turt,size/3,order-1)
        turt.left(60)
        draw_fractal2(turt, size / 3, order - 1)
        turt.left(-120)
        draw_fractal2(turt, size / 3, order - 1)
        turt.left(60)
        draw_fractal2(turt, size / 3, order - 1)



def draw_fractal(turt,size,order): # diulo el fractal colocando la forma en el else, todos los pasos dentro de un ciclo for

    if order == 0:
        turt.forward(size)
    else:
        for _ in [60,-120,60,0]:
            draw_fractal(turt,size/3,order-1)
            turt.left(_)

draw_fractal(fract,100,2)

draw_fractal(fract2,100,2)


fract2.circle(10)

def draw_fractal_0(turt,size):
    turt.forward(size)

def draw_fractal_1(turt,size):
    for angle in [60,-120,60,0]:
        draw_fractal_0(turt,size/3)
        turt.left(angle)

def draw_fractal_2(turt, size):
    for angle in [60, -120, 60, 0]:
        draw_fractal_1(turt, size/3)
        turt.left(angle)

draw_fractal_0(fract2,100)  #dibulo el fractal en pasos de recursion

draw_fractal_1(fract2,100)

draw_fractal_2(fract2,100)

window.mainloop()

a = [1,2,3,[1,[1,2,[1,2,[1,[1,[1,2,3,[1,[1,2,[1,2,[1,2,3,[1,[1,2,[1,2,[1,[1,2]]],54,[1,2,3,[1,[1,2,[1,1221,2,[1,[1,2]]],3],2,3,[1,2]]]],2,3,[1,2]]],[1,[1,2]]],3],2,3,[1,2]]],2]]],3],2,3,[1,2]]]

def sum_nested_list(lista):
    if len(lista) == 0:
        return 0
    head, *tail = lista
    if isinstance(head, list):
        return sum_nested_list(head)+sum_nested_list(tail)
    else:
        return head + sum_nested_list(tail)

print(sum_nested_list(a))

def sum_nested_list_2(lista):
    sum = 0
    for element in lista:
        if type(element) is list:
            sum += sum_nested_list_2(element)
        else:
            sum += element
    return sum

print(sum_nested_list_2(a))

def recursive_sum(nested_number_list):
    total = 0
    for element in nested_number_list:
        if type(element) is list:
            total += recursive_sum(element)
        else:
            total += element
    return total

print(recursive_sum(a))

def red(nido):
    if len(nido) == 0:
        return 0
    c,*t = nido
    if isinstance(c,list):
        return red(c)+red(t)
    else:
        return c+red(t)

print(red(a))

def red2(nido):
    sum = 0
    for _ in nido:
        if type(_) is list:
            sum += red2(_)
        else:
            sum += _
    return sum

print(red2(a))

def hayar_máximo_anidado(nido):

    max = None
    primeravez = True
    for x in nido:
        if type(x) == list:
            valor = hayar_máximo_anidado(x)
        else:
            valor = x

        if primeravez or valor > max:
            max = valor
            primeravez = False


    return max

print(hayar_máximo_anidado(a))

#fibonacci recursiva

import time
t0 = time.clock()
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1)+fib(n-2)

print(fib(2))
t1 = time.clock()
print ("tarda {0:.4f} segundos".format(t1-t0))

t2 = time.clock()
def fibo(n):
    result = []
    a, b = 0, 1
    for i in range(n+1):
        result.append(a)
        a, b = b, a + b
    return result[n]
print(fibo(12))
t3 = time.clock()

print ("tarda {0:.15f} segundos".format(t3-t2))

a = [1,1,2,3,[1,[1,2,[1,2,[1,[1,[1,2,3,[1,[1,2,[1,2,[1,2,3,[1,[1,2,[1,2,[1,[1,1,2]]],54,[1,2,3,[1,[1,2,[1,1221,2,[1,[1,2]]],3],2,3,[1,2]]]],2,3,[1,2]]],[1,[1,2]]],3],2,3,[1,2]]],2]]],3],2,3,[1,2]]]
cant = 0
def cant_veces(lista,n):
    global cant

    for x in lista:
        if type(x) == list:
            step = cant_veces(x,n)
        else:
            step = x

        if step == n:
            cant += 1


    return cant

print(cant_veces(a,1))

import os

def get_listdir(path):
    dir_list = os.listdir(path)
    dir_list.sort()
    return dir_list

def lista_direct_y_files(path,prefix=""):
    if prefix == "":
        print("lista de archivos desde: ",path)
        prefix = "|"
    dirlist = get_listdir(path)
    for file in dirlist:
        print(prefix+file)
        fullname = os.path.join(path,file)
        if os.path.isdir(fullname):
            lista_direct_y_files(fullname,prefix+"|")


lista_direct_y_files("C:\\Users\\Uso familiar\\Documents\\Matias")

#RECURSIÓN MUTUA

def a(n):
    if n == 0:
        return 1
    print("saltar a la función b en el step ",n-1)
    b(n-1)

def b(n):
    if n == 0:
        return 1
    print("saltar a la función a en el step ",n-1)
    a(n-1)

a(20)



def get_dirlist(path):


    dirlist = os.listdir(path)
    dirlist.sort()
    return dirlist

def print_files(path, prefix = ""):
    # Print recursive listing of contents of path 
    if prefix == "": # Detect outermost call, print a heading
        print("Folder listing for", path)
        prefix = "| "
    dirlist = get_dirlist(path)
    for file in dirlist:
        print(prefix+file) # Print the line
        fullname = os.path.join(path, file) # Turn name into full˓→pathname
        if os.path.isdir(fullname): # If a directory,→recurse.
            print_files(fullname, prefix + "| ")


#nuevamente, práctica de dirlist
import os

def get_filedir(path):
    all_files = os.listdir(path)
    all_files.sort()
    return all_files

def print_files2(path,prefix = ""):
    todos = get_filedir(path)
    if prefix == "":
        print("se obtienen los directorios desde: ",path)
        prefix = ">"

    for file in todos:
        print(prefix + file)
        fullname = os.path.join(path,file)
        if os.path.isdir(fullname):
            print_files2(fullname,prefix+">")



print_files("C:\\Users\\Uso familiar\\Documents\\Matias\\Estudios Maty\\Matemática y Física Moderna\\fisica moderna")


import pygame,math

pygame.init()

surface_size = 1024
main_surface = pygame.display.set_mode((surface_size,surface_size))
my_clock = pygame.time.Clock()

def draw_tree(order, theta, size, position, heading, color=(0,0,0),depth=0):

    trunk_ratio = 0.29 # How big is the trunk relative to whole tree?
    trunk = size * trunk_ratio # length of trunk
    delta_x = trunk * math.cos(heading)
    delta_y = trunk * math.sin(heading)
    (u, v) = position
    newposition = (u + delta_x, v + delta_y)
    pygame.draw.line(main_surface, color, position, newposition)
    pygame.draw.circle(main_surface, color, (int(position[0]),int(position[1])), 3)
    if order > 0: # Draw another layer of subtrees

        # These next six lines are a simple hack to make the tw→major halves
        # of the recursion different colors. Fiddle here to change˓→colors
        # at other depths, or when depth is even, or odd, etc.
        if depth == 0:
            color1 = (255, 0, 0)
            color2 = (0, 0, 255)
        else:
            color1 = color
            color2 = color

# make the recursive calls to draw the two subtrees
        newsize = size*(1 - trunk_ratio)
        draw_tree(order-1, theta, newsize, newposition, heading-theta, color1, depth+1)
        draw_tree(order-1, theta, newsize, newposition, heading+theta,color2, depth+1)

def gameloop():
    theta = 0
    while True:
        # Handle evente from keyboard, mouse, etc.
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            break
        theta += 0.01

        # Draw everything
        main_surface.fill((255, 255, 0))
        draw_tree(9, theta, surface_size*0.9, (surface_size//2,surface_size-50), -math.pi/2)

        pygame.display.flip()
        my_clock.tick(120)


gameloop()
pygame.quit()



#1
import turtle
turt = turtle.Turtle()
window = turtle.Screen()
window.bgcolor("lightblue")
turt.speed(100)


def koch_snowflake(tortuga,size,order):
    if order == 0:
        tortuga.forward(size)
    else:
        for angle in [-60,120,-60,0]:
            koch_snowflake(tortuga,size/3,order-1)
            tortuga.left(angle)

def draw_poly(n,sz,tortuga,size,order):
    polygon = tortuga
    q = ((n - 2) * 180)/n
    for _ in range(n):
        polygon.left(180 - q)
        koch_snowflake(turt, size, order)

draw_poly(3,50,turt,200,4)

window.mainloop()

#2
#a
from math import sin, pi

import turtle
turt = turtle.Turtle()
window = turtle.Screen()
window.bgcolor("lightblue")
turt.speed(50)

def cesaro_torn(tortuga,size,order):
    if order == 0:
        tortuga.forward(size)
    else:
        for angle in [-80,160,-80,0]:
            cesaro_torn(tortuga,size/(2+2*sin(pi/18)),order-1)  #ver que acá al aplicar sin, igualo los tamaños sea cual fuera el orden pasado a la función
            tortuga.right(angle)




#b

def draw_poly(n,sz,tortuga,size,order):
    polygon = tortuga
    q = ((n - 2) * 180)/n
    for _ in range(n):
        polygon.left(180 - q)
        cesaro_torn(turt, size, order)

draw_poly(4,50,turt,200,4)

window.mainloop()
"""

#3

import turtle
turt = turtle.Turtle()
window = turtle.Screen()
window.bgcolor("lightblue")
turt.speed(4)

def sierpinski(tortuga,size,order):
    if order == 0:
        tortuga.forward(size)
        tortuga.left(120)
        tortuga.forward(size)
        tortuga.left(120)
        tortuga.forward(size)
        tortuga.left(120)
        tortuga.forward(size)

    else:
        for angle in [120,120,120]:
            sierpinski(tortuga,size/2,order-1)
            tortuga.forward(size/2)
            tortuga.left(angle)


sierpinski(turt,300,0)
window.mainloop()

"""
#5

a = [1,2,3,[3,4,5],3,2,[1,[-55555551,2,[1,2,3,[3,4,5],3,2,[1,3,3,[-4999999999999999999],2]],3,[3,4,5],3,2,[1,3,3,[4],2]],3,3,[4],2]]

def recursive_min(nested_list):
    min = None
    first_time = True
    for _ in nested_list:
        if type(_) == list:
            valor  = recursive_min(_)
        else:
            valor = _
        if first_time:
            min = valor
            first_time = False

        if valor < min or first_time:
            min = valor


    return min

print(recursive_min(a))

#6


import time

t0 =
cont = 0
def count_target(nested_list,target):
    global cont
    #isnt_there = True
    for _ in nested_list:
        if type(_) == list:
            valor = count_target(_,target)
        else:
            valor = _

        if valor == target:
            cont += 1
            isnt_there = False

    return cont

a = [1,2,3,[3,4,5],3,2,[1,[-55555551,2,[1,2,3,[3,4,5],3,2,[1,3,3,[-4999999999999999999],2]],3,[3,4,5],3,2,[1,3,3,[4],2]],3,3,[4],2]]

print(count_target(a,c))


#7
flat = []
def flatten(nested_list):
    global flat

    for _ in nested_list:
        if type(_) == list:
            valor = flatten(_)
        else:
            valor = _
        flat.append(valor)
    return flat

print(flatten(a))


#8
def fib(n):
    fib_list = []
    for _ in range(n+1):
        a=1
        if _<=1:
            fib_list.append(_)
        else:
            fib_list.append(fib_list[_-1]+fib_list[_-2])
    return fib_list

print(fib(40))

a = fib(230)
print(a[200])


#9
import sys

print(sys.getrecursionlimit())

sys.setrecursionlimit(2000)

def recursion_depth(number):
    print("{0}, ".format(number),end="")
    recursion_depth(number+1)

recursion_depth(0)

sys.setrecursionlimit(1000)



import os

def get_files(path):
# esta función me almacena los elementos sean carpetas o archivos, de un directorio path, en una lista

    all_files = os.listdir(path)
    all_files.sort()
    return all_files

list_files = []

def list_fulldir(path):
#esta función me busca todos los archivos dentro de un directorio path , los archivos pueden estar dentro de subcarmetas y subcarmetas hasta dar con el último eslabón.

    files = get_files(path)
    global list_files
    for file in files:
        fullname = os.path.join(path,file)
        if os.path.isdir(fullname):
            list_fulldir(fullname)
        else:
            list_files.append(fullname)

    return list_files

print(get_files("C:\\Users\\Uso familiar\\Documents\\Matias\\Estudios Maty\\Matemática y Física Moderna"))
print(len(get_files("C:\\Users\\Uso familiar\\Documents\\Matias\\Estudios Maty\\Matemática y Física Moderna")))

a = list_fulldir("C:\\Users\\Uso familiar\\Documents\\Matias\\Estudios Maty\\Matemática y Física Moderna")
# Se almacena list_fulldir en una variable ya que si se ejecuta en print, y luego se ejecuta en print(len()) se ejecuta vos veces y se duplica la lista, el procedimiento dentro de
#list_fulldir es con append, es decir, va agregando cada vez que pasamos por ahí.
print(a)
print(len(a))


#10
   

import os

def get_files(path):
    all_files = os.listdir(path)
    all_files.sort()
    return all_files

def litter(path):
    alojar_trash = get_files(path)
    for file in alojar_trash:
        fullname = os.path.join(path,file)
        if os.path.isdir(fullname):
            open(os.path.join(fullname,"trash.txt"),"w")
            litter(fullname)
        else:
            continue

litter("C:\\Users\\Uso familiar\\Documents\\Matias\\videos\\FUTBOL")


import os

def get_files(path):
    all_files = os.listdir(path)
    all_files.sort()
    return all_files


def test_cleanup(path):

    #V1 de delete files, estaba bien solo que nunca llamé a la función

    alojamientos_trash = get_files(path)
    for file in alojamientos_trash:
        fullname = os.path.join(path, file)
        if os.path.isdir(fullname):
            test_cleanup(fullname)
        elif file == "trash.txt":
            with open(os.path.join(path, file), "w") as trash:
                trash.write("hi")


test_cleanup("C:\\Users\\Uso familiar\\Documents\\Matias\\videos\\FUTBOL")

print(get_files("C:\\Users\\Uso familiar\\Documents\\Matias\\videos\\FUTBOL\\cracks"))

def test_cleanup2(path):
#V2 de delete files

    alojamientos_trash = get_files(path)
    for file in alojamientos_trash:
        if file == "trash.txt":
            with open(os.path.join(path, file),"w") as trash:
                trash.write("hola")

        fullname = os.path.join(path,file)
        if os.path.isdir(fullname):
            test_cleanup2(fullname)

test_cleanup2("C:\\Users\\Uso familiar\\Documents\\Matias\\videos\\FUTBOL")

def cleanup(path):
#V2 de delete files

    alojamientos_trash = get_files(path)
    for file in alojamientos_trash:
        if file == "trash.txt":
            full_name_to_remove = os.path.join(path, file)
            os.remove(full_name_to_remove)

        fullname = os.path.join(path,file)
        if os.path.isdir(fullname):
            cleanup(fullname)

cleanup("C:\\Users\\Uso familiar\\Documents\\Matias\\videos\\FUTBOL")

"""
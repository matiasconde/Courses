import math
def areatriangulo(b,h):
    a=(b*h)/2
    return a
def areaesfera(r):
    a=4*(math.pi)*(r*r)
    return a

def areacuadrado(l):
    a=l*l
    return a

f= int(input("ingrese figura geométrica (1=triángulo, 2=esfera, 3=cuadrado): "))

if f == 1:
        b= float (input("ingrese base del triángulo: "))
        h= float (input("ingrese altura del triángulo: "))
        c=areatriangulo(b,h)
        print("el área del triángulo es: ", c)
if f == 2:
        r = float(input("ingrese radio de la esfera: "))
        c = areaesfera(r)
        print("el área de la esferaes: ", c)
if f == 3:
        l = float(input("ingrese lado del cuadrado: "))
        c= areacuadrado(l)
        print("el area del cuadrado es: ",c)

input("INGRESE cualquier cosa PARA TERMINAR")


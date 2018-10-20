import math

def ordennum(x,y):
    if x > y:
        print("x es mayor que y")
        return(x)
    else:
        if x == y:
            print("x es igual a y")
            return(y)
        else:
            print("x es menor que y")
            return(y)
def paridad(x):
    if x%2 == x/2:
        print("el número es par")
        return(x)
    else:
         print("el número es impar")

a = int(input("ingrese primer número (x) a comparar: "))
b = int(input("ingrese segundo número (y) a comparar: "))
c = int(input("ingrese número a verificar paridad: "))

ordennum(a,b)
paridad(c)

q=input("ingrese cualquier cosa para terminar")
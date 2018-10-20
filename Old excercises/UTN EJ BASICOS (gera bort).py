import math

Q=1

def resolventecuadratica1(a,b,c):
    d = (b**2 - 4*a*c)
    if d<0:
        Q=-1
        disccomp = math.sqrt(-d)
        w = (-b) / (2 * a)
        print("las raíces son complejas")
        return(w,disccomp/(2*a))
    else:
        Q=1
        discreal = math.sqrt(d)
    w = (-b+discreal)/(2*a)
    print("las raices son reales")
    return (w)

def resolventecuadratica2(a,b,c):
    d = (b**2 - 4*a*c)
    if d<0:
        Q=-1
        disccomp = math.sqrt(-d)
        x1 = (-b) / (2 * a)
        return(x1,disccomp/(2*a))
    else:
        Q=1
        discreal = math.sqrt(d)
    x2 = (-b-discreal)/(2*a)
    return (x2)

x=int (input("ingrese a: "))
y=int (input("ingrese b: "))
z=int (input("ingrese c: "))

print("la primer raiz es: ",resolventecuadratica1(x,y,z))
print("la segunda raiz es: ",resolventecuadratica2(x,y,z))

input("oh si!")


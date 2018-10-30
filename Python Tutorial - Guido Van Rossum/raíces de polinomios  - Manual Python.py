import math
"""
Q=1

def polynomialroots(n):



x = int(input("ingrese grando del polinomio: "))
"""



def resolventecuadratica1(a,b,c):
    d = (b**2 - 4*a*c)
    if d<0:
        Q=-1
        disccomp = math.sqrt(-d)
        w = (-b) / (2 * a)
        print("las raíces son complejas")
        c=(disccomp/(2*a))
        return 'la primera raiz es: {0:.2f}'.format(w+c*1j)
    else:
        Q=1
        discreal = math.sqrt(d)
    w = (-b+discreal)/(2*a)
    print("las raices son reales")
    return 'la primer raiz es: {0:.2f}'.format(w)

def resolventecuadratica2(a,b,c):
    d = (b**2 - 4*a*c)
    if d<0:
        Q=-1
        disccomp = math.sqrt(-d)
        x1 = (-b) / (2 * a)
        c=(disccomp/(2*a))
        return 'la segunda raiz es: {0:.2f}'.format((x1 + c * 1j))
    else:
        Q=1
        discreal = math.sqrt(d)
    x2 = (-b-discreal)/(2*a)
    return 'la segunda raiz es: {0:.2f}'.format(x2)

x=int (input("ingrese a: "))
y=int (input("ingrese b: "))
z=int (input("ingrese c: "))

print(resolventecuadratica1(x,y,z))
print(resolventecuadratica2(x,y,z))

input("oh si!")


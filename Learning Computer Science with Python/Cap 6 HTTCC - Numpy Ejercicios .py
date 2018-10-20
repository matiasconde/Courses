#ejercicio en página 164
# porqué a = np.array([200],dtype=uint8)
# a+a = np.array([144],dtype=8)
#200+200 = 400 pero al pasarse de 256 valores, vuelve a empezar
#la cadena binaria hasta 144 (144+256 = 400)
#
#1
"""
import numpy as np
a = np.array([2,3,4,4], dtype = "uint8")
k = 100

print(a+253)

# lo que sucede es que cada valor puede llegar al máximo de 255 y vuelve a
# empezar, con lo cual, el primero llega a 2+253 = 255, el segundo +3+253 = 256 , se pasa uno, entonces 256-255 = 1
#y el valor 1 es el 0 (porque arranca de 0) y así sucesivamente.

#2
import numpy as np

def cosa_loca(list):
    cont = 0
    value = True
    a = np.array(list)
    while value:
        a[a<100]=a[a<100]*2
        for i in range(len(a)):
            if a[i] > 100:
                cont += 1
        if cont == 5:
            value = False
        else:
            cont = 0
    a[a>200] = 0
    a[150>a] = 0
    return a

print(cosa_loca([230, 10, 284, 39, 76]))

"""

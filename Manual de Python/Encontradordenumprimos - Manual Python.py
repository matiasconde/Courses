a=int(input("ingrese hasta que número natural, sin incluir, desea buscar números primos: "))
cont=0
for n in range(2,a):
    for x in range(2,n):
        if n%x == 0:
            break  #acá sale de la sentencia if, el break para salir de una sentencia, se escribe dentro de la misma
    else:
        print(n, "es un número primo")
        cont+=1

print(cont, "números primos en total")
input("cualq")



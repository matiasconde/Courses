palabra = ["a","b","c","canino"]

for p in palabra:
    print(p,len(p))

palabra.insert(0,"z")

print(palabra)

c = ""
print(c)

for p in range(len(palabra)):
    c=c+palabra[p]


print(c)

for i in range(len(palabra)):
    print(i, c[i])


for num in range(2,10):
    if num%2==0:
        print("encontré un número par", num)
        continue
    print("encontré un número impar", num)


while True:
    pass #espera ocupada hasta una interrupción de teclado Ctrl C

a=int(input("ingrese hasta que número natural, sin incluir, desea buscar números primos: "))


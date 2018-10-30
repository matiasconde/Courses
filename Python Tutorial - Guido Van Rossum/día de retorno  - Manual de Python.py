a=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]

b=int(input("ingrese un número de día (del 0 al 6): ",))

print(a[b])

startday = int(input("ingrese día en que partíó: ",))

qsleeps = int(input("¿Luego de cuantas noches ha retornado usted? ",))


z = qsleeps%7
w=z+startday
while (w)>6:
    w=w%7
    print(w)

print("usted a regresado el día: ",a[w])


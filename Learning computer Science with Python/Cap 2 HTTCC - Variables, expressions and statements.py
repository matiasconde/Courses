a="All "
b="work "
c="and "
d="no "
e="play "

#programa para concatenar

f="makes "
g="Jack "
h="a "
i="dull "
j="boy "

print(a+b+c+d+e+f+g+h+i+j)
ValorPresente=float(input("ingrese valor a depositar o a invertir: ", ))
interest=float(input("ingrese tasa de interés compesto anual: ", ))
numcap=int(input("ingrese número de capitalizaciones a realizar en un año: ", ))
qaños=int(input("ingrese cantidad de años a permanecer en la operación: ", ))

print("Sus inversiones habrán crecido hasta: ",ValorPresente*(1+interest/(numcap*100))**(qaños*numcap))

w=int(input("ingrese la hora que es actualmente: ",))
z=int(input("ingrese la cantidad de horas en que desea que suene su alarma: ",))

x = z%24
u=x+w
while (u)>24:
    u=u%7
    print(u)

print("cuando suene la alarma en su reloj figurará la hora: ",u)

q=int(input("ingrese número: ", ))
cont=0
while q!=0:
    cont+=1
    q=q//10
print("su número tiene: ",cont," dígitos")

for x in range(99999):
    print(x,"\t", x**2)

"""
#1
a=[1,-2,3,-4,4,3,-3,-4,5,-5,34,-3,3,-23,4,54,5,4,33,4,4,4,4,5]

cont=0
for _ in a:
    if _%2==1:
        cont+=1
print(cont)

#2
sum=0
for _ in a:
    if _ % 2 == 0:
        sum += _
print(sum)

#3
sum2=0
for _ in a:
    if _<0:
        sum2 += _
print(sum2)

#4
count=0
b=["dasdasdasd","sadsadsa","s","asda","lalalong"]
for _ in b:
    if len(_)==5:
        count+=1
print(count)

#5
sum3=0
z=0
for i in range(0,len(a)):
    if a[i]%2 == 0:
        print(i,a[i])
        z=i
        break
    else:
        z=i+1
for i in range(0,z):
    sum3+=a[i]

print(sum(a))
print(sum3)

#6
b=["sasasa","lala","sadasdddddd","","sasa3df2"]
cont=0
for _ in b:
    if _=="sam":
        break
    else:
        cont+=1
print(cont)

#7
num=float(input("ingrese número a calcular su raíz cuadrada: ",)) #calculando raices cuadradas por el método de Newton
approximation=1
for _ in range(5):
    approximation = approximation - (approximation**2-num)/(2*approximation)
    print(approximation)

#8
num=int(input("ingrese la cantidad de números triángulares a imprimir: ",))
sum=0
for _ in range(1,num+1):
    sum+=_
    print(_, sum)

#9
num=int(input("ingrese número a verificar si es primo o no: ",))
for _ in range(2,num):
    if num%_ == 0:
        print(num, " no es primo")
        break
else:
    print(num, " es primo")

#10
a=[(160, 20), (-43, 10), (270, 8), (-43, 112)]
import turtle
drunk2=turtle.Turtle()
drunk2.color("red")
window=turtle.Screen()
window.bgcolor("lightblue")
t=0
f=0
for _ in a:
    drunk2.left(_[0])
    drunk2.forward(_[1])
input("sasa")


#11
import math
z=math.sqrt(50**2+50**2)
a=[(90, 50), (90,50), (-120,50), (-120,50),(-75,z),(-135,50),(-135,z),(-135,50)]
import turtle
casita=turtle.Turtle()
casita.color("red")
window=turtle.Screen()
window.bgcolor("lightblue")
t=0
f=0
for _ in a:
    casita.left(_[0])
    casita.forward(_[1])
input("sasa")


#12
num=int(input("ingrese número entero para contarle sus dígitos: ",))
cont=0
if num==0:
    print("tiene 1 dígito")
elif num<0:
    num=num*(-1)
    while num>0:
        num=num//10
        cont+=1
    print("tiene, ",cont," dígitos")
else:
    while num > 0:
        num = num // 10
        cont += 1
    print("tiene ", cont, " dígitos")

#13
num=int(input("ingrese número entero para contarle sus dígitos pares: ",))
cont=0
z=0
if num==0:
    print("tiene 1 dígito par")
elif num<0:
    num=num*(-1)
    while num>0:
        z=num%10
        num=num//10
        if z%2==0:
            cont+=1
    print("tiene, ",cont," dígitos pares")
else:
    while num > 0:
        z = num % 10
        num = num // 10
        if z % 2 == 0:
            cont += 1
    print("tiene ", cont, " dígitos pares")



#14

sum=0
numbers=list(input("ingrese lista de números: ",))
sqnumbers=[]
print(numbers)
for i in range(len(numbers)):
    sum+=int(numbers[i])**2
    sqnumbers.append(int(numbers[i])**2)
print(sqnumbers)
print("la suma de los cuadrados de la lista ingresada es: ",sum)

"""
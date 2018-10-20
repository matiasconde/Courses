import random

z=random.Random()
number=z.randrange(1,20000)
intentos=0
mensaje:""
while True:
    intento = int(input("adivina mi número entre 1 y 20000: ", ))
    intentos+=1
    if intento>number:
        print(str(intento)+"es muy alto.\n")
    elif intento<number:
        print(str(intento)+"es muy bajo.\n")
    else:
        print("\n\nGreat, you got it in " + str(intentos) + " intentos!\n\n")
        break
    if intentos>4:
        print("\n\nI'm sorry, you not gone got it")
        break



lista=[("Juan",["contaduría","futbol"]),("Matias",["ingeniería","futbol"])]
cont=0
for nombre,ocupación in lista:
    for o in ocupación:
        if o == "futbol":
            cont+=1
print("la cantidad de personas que se ocupan al fútbol son: ",cont)

k=[1,4,6,7,8,9,10]
for number in k:
    if number%2==1:
        print(True)
        break
else:
    print(False)
cont=0
k=[1,3,5,7,8]
for number in k:
    if number%2==1:
        cont+=1
print(cont==len(k))

cont=0
k=[2,4,6,8,10,11,12,14,16,17,22,24,26,28,29,30,33,32,34,36]
for number in k:
    if number%2==1:
        cont+=1
        if cont==3:
            print("ahhhh listo hay al menos 3 impares, ",True)
            break
        else:
            print("no llega a haber 3 impares, hay: ",cont, " impares", "por lo tanto es: ",False)

Joe=random.Random()

lista=[]
tot=0
for _ in range (10000000000):
    tot+=Joe.randrange(1000)
print(tot)







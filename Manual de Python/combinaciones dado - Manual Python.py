import math


def sumadosdados(x):
    return (x - 1)

a = int(input("ingrese suma deseada al tirar los dos dados: "))
print("número de combinaciones posibles para esa suma: ",sumadosdados(a))

def sumadosdados2(y):
    if y>12:
        print("la combinación es imposible")
    else:
        c=0
        for i in range(1,7):
            for j in range(1,7):
                if (i+j)==y:
                    c=c+1
                    print(i,j)
    return(c)

b = int(input("ingrese suma deseada al tirar los dos dados: "))

print("la probabilidad de obtener la combinación pedida es de: %",((sumadosdados2(b)/36)*100))

print("número de combinaciones posibles para esa suma: ", sumadosdados2(b))

input("ingrese cualquier cosa para terminar")

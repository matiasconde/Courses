import math
from matplotlib import pyplot as pl

def factorial(n):
    b = n
    f = n
    if n<0:
        raise ValueError("Error de valor, debe ser un entero positivo")
    if n==0:
        return 1
    else:
        while b>1:
            f *= (b-1)
            b -= 1
    return f

def combinatorio(n,m):
    return int((factorial(n))/(factorial(m)*factorial(n-m)))

def potencia(a,b):
    #a a la b
    return math.pow(a,b)

def Poisson(x,λ,t):
    return (potencia((λ*t),x)/factorial(x))*math.exp(-λ*t)

def Binomial(x,n,θ):
    return combinatorio(n,x)*pow(θ,x)*pow(1-θ,n-x)

def Hipergeométrica(x,N,D,n):
    return (combinatorio(D,x)*combinatorio(N-D,n-x))/combinatorio(N,n)


#ahora voy a resolver el ejercicio 10 parte a, de la práctica 3 del 2016 de la material \
# probabilidad de uba exactas matemáticas

"""
sum = 0
for i in range(9):
    sum += (combinatorio(20,8-i)*combinatorio(25,i))/(combinatorio(50,8))

print(sum)



Alternativa
def c(n,m):
    return int((factorial(n))/(factorial(m)*factorial(n-m)))

a = c(20,8)*c(25,0)+c(20,7)*c(25,1)+c(20,6)*c(25,2)+c(20,5)*c(25,3)+c(20,4)*c(25,4)+c(20,3)*c(25,5)\
    +c(20,2)*c(25,6)+c(20,1)*c(25,7)+c(20,0)*c(25,8)

print(a)
b = c(50,8)
print(b)

print(a/b)


#ahora voy a resolver el ejercicio 10 parte b, de la práctica 3 del 2016 de la material \
#probabilidad de uba exactas matemáticas

sum2 = 0
for i in range(4):
    sum2 += (combinatorio(20,8-i)*combinatorio(25,i))/combinatorio(50,8)

print(sum2)


print(potencia(2,4))

print(Poisson(4,2,1))

sum3=0
for i in [8,12,16]:
    sum3 += Poisson(i,2,4)
print(sum3)


sum4=0
y2=[]
for i in range(5):
    sum4 += Poisson(i,2,1)
    y2.append(sum4)
    if sum4>=0.99:
        print(i)
        print(y2)
        break
print("la probabilidad de cumplimiento en cada semana es de: ",sum4)
print("la probabilidad de incumplimiento en cada semana es de: ",1-sum4)

x=list(range(5))
x2=list(range(5))
y=[]
for i in range(5):
    y.append(Poisson(i,2,1))

pl.plot(x,y,"r-.",label="X~Poisson(2,1) density")
pl.plot(x2,y2,"y.",label="X~Poisson(2,1) distribution")
pl.legend()
pl.xlabel("dominio")
pl.ylabel("imagen")
pl.bar(x,y,width=0.1)
pl.show()


# Se puede apreciar numéricamente que la hipergeométrica tiende a la binomial
print(Binomial(5,10,0.6))
print(Hipergeométrica(5,1000,600,10))

"""

#features
#https://www.amazon.com/dp/B077TCYHZP/ref=psdc_13896597011_t2_B078945RGW
NVIDIA GeForce Titan Xp 2x GPU DEVBOX is top of the line fully-loaded GPU solution
for deep learning/machine learning applications. Features: - (1) NVIDIA GeForce Titan Xp -
(1) Core i7-6850K 6-Core 3.6GHz Processor - (2) 16GB DDR4 memory - (1) 256GB SSD for OS/Deep
    Learning Software Stacks - (1) 4TB HDD for data - Latest version of NVIDIA Digits, Caffe,
    Torch, Theano, BIDMach, CuDNNv2, OpenCV v.3.0, and NVIDIA® CUDA


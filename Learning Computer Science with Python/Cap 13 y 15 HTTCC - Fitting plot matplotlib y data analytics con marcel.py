from matplotlib import pyplot as plt
import numpy as np
import symfit.api
import math

#Plotting:

from math import exp


def fib(n):
    fib_list = []
    for _ in range(n+1):
        a=1
        if _<=1:
            fib_list.append(_)
        else:
            fib_list.append(fib_list[_-1]+fib_list[_-2])
    return fib_list
a = 5
y = fib(a)
x = []
for i in range(a+1):
    x.append(i)

def test_function(a):
    p = []
    q = []
    for _ in range(a):
        p.append(_)
        q.append(exp(_))
    return (p,q)
print(y)
print(x)
print(test_function(a)[0])
print(test_function(a)[1])

plt.plot(x,y,'y.',label="fibonacci")
plt.plot(test_function(a)[0],test_function(a)[1],"bx",label="exponencial",)
plt.legend()
plt.xlabel("dominio")
plt.ylabel("imagen")
plt.xlim(0,20)
plt.ylim(0,100)
plt.bar(x,y)
plt.bar(test_function(a)[0],test_function(a)[1],width = 0.1)
plt.show()

plt.bar(np.arange(1,2.9,0.17),[1,2,3,4,5,6,7,8,9,10,11,12],width = 0.1)
plt.xlim(0,3.5)
plt.ylim(0,15)
#np.arange(1,2.9,0.17))
plt.show()


def fit_function(x):
    return 0.5*x**2

x_data = [list(range(1,11))]
y_data = [2,3,5,7,11,13,17,19,23,29]

x_funct = np.linspace(1,15,50)
y_funct = fit_function(x_funct)
plt.plot(x_funct,y_funct,"y-.",label='$f(x) = 0.388 x^2$')
plt.scatter(x_data,y_data,c="r",label = "n° primos")
plt.title("Ajuste: Cuadrática vs. N° Primos")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.legend()
plt.savefig('Figure_1_.pdf')
plt.show()



x_data1 = [1,2,3,4,5,6,7,8,9,10]
y_data1 = [2,4,6,8,10,12,14,16,18,20]

x_data2 = [2,3,5,7,11,13,17,19,23,29]
y_data2 = [3,5,8,4,5,6,7,8,14,20]

fig = plt.figure()
graph1 = fig.add_subplot(2,2,1)
graph2 = fig.add_subplot(3,2,2)
graph1.plot(x_data1,y_data1,label="Datos 1")
graph2.plot(x_data2,y_data2,label="Datos 2")
graph1.legend()
graph2.legend()
graph1.set_xlabel("Eje X-1")
graph1.set_ylabel("Eje Y-1")
graph2.set_xlabel("Eje X-2")
graph2.set_ylabel("Eje Y-2")
graph1.set_title("Gráfico de Datos 1")
graph2.set_title("Gráfico de Datos 2")

plt.show()





path = "radiobases_4g.csv"


class Celdas:
    def __init__(self, país):
        self.pais = país

    def celdas_x_provincia(self, prov):
        #toma una provincia y visualiza las celdas instaladas en esas provincias
        

        with open(path, "r") as archivo:
            list_util_final = []
            leer = archivo.read()
            leer_split = leer.split('\n')
            # print(leer_split)

            for line in leer_split:
                list_util = []
                splt = line.split(',')
                for element in splt:
                    palabra_limpia = ''
                    for word in element:
                        if word not in '".':
                            palabra_limpia += word
                    list_util.append(palabra_limpia)

                if prov in list_util:
                    list_util_final.append(list_util[3])
                    list_util_final.append(list_util[4])

        lts_float = [float(list_util_final[0]), float(list_util_final[1])]
        plt.bar(np.arange(0., 1.0, .5), lts_float, width=0.25, label=prov)
        plt.legend()
        plt.show()
        return list_util_final


cell = Celdas('Argentina')
cell.celdas_x_provincia('Buenos Aires')
# print(cell.celdas_x_provincia('Buenos Aires'))


#FITTING 1

t_data = np.array([1.4,2.1,2.6,3.0,3.3])
h_data = np.array([10,20,30,40,50])

h = symfit.api.Variable()
g = symfit.api.Parameter()
t_model = symfit.api.sqrt(2*h/g)

fit = symfit.api.Fit(t_model,h_data,t_data)
fit_result = fit.execute()
print(fit_result)

h_range = np.linspace(0,50,1000)
datos_encajados = t_model(h=h_range,g=fit_result.params.g)
plt.plot(h_range,datos_encajados,"b",label="Modelo para obtener g")
plt.scatter([10,20,30,40,50],[1.4,2.1,2.6,3.0,3.3],c="g",label = "Datos")
plt.xlabel("Altura (m)")
plt.ylabel("Tiempo (s)")

plt.show()

#FITTING 2

t_data = np.array([1.4,2.1,2.6,3.0,3.3])
h_data = np.array([10,20,30,40,50])
n_data = np.array([5,3,8,15,30])

sigma = 0.2
sigma_t = sigma / np.sqrt(n_data)

h = symfit.api.Variable()
t = symfit.api.Variable()
g = symfit.api.Parameter()

t_model = {t: symfit.api.sqrt(2*h/g)}

fit = symfit.api.Fit(t_model,h = h_data,t = t_data,sigma_t = sigma_t)
datos_encajados_2 = fit.execute()
print(datos_encajados_2)

h_range = np.linspace(0,50,1000)
t_range = t_model[t](h = h_range,g = datos_encajados_2.params.g)
plt.plot(h_range,t_range,"r-.",label = "Fitting with uncertainty")
plt.legend()
plt.xlabel("Altura (m)")
plt.ylabel("Tiempo (s)")
plt.scatter([10,20,30,40,50],[1.4,2.1,2.6,3.0,3.3],c="g",label = "Datos")
plt.show()


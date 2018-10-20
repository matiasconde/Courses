#exceptions

#Observar que "atrapando excepciones" lo que hace es leer linea por linea y cuando aparece el error, saltar directamente a las excepciones, cuando encuentra el tipo de error que coincide con el error
#ocurrido, ejecuta el bloque debajo de dicha excepción declarada, sino está, busca una excepción "genérica", es decir, sin declaración, y ejecuta el bloque debajo de ésta última, sino, el programa termina en
#error y se corta. En caso de si haber encontrado alguna excepción, ya sea del tipo indicado, como una "genérica", luego de ejecutar el bloque correspondiente, ejecuta siempre el bloque debajo de "finally".
"""
try:
    file = open("ZZZfileversion2.txt", "r")
    b = float(1)
    a = (1, 2)
    #a[0] = 2
    #a[3]
except TypeError:
    print("las tuplas son inmutables")
except ValueError:
    print("no se ingresó un número para convertir en float")
except FileNotFoundError:
    print("no se encuentra el archivo en el directorio que usa python 3.6")
except:
    print("el error encontrado no es ni 'FileNotFoundError', ni 'ValueError', ni 'TypeError' ")
else:
    print("no hubo errores")
finally:
    print("gracias vuelva pronto")


def prueba_de_errores(lala):
    #levantando errores, dentro del "raise" tiene que haber un tipo de error, si la función es ejecutada, el error sale quebrando la ejecución,
    #si el llamado a la función está dentro de un entorno de prueba que pueda menejar el tipo de error levantado, no pasa nada.
    raise NotImplementedError("la concha de la lora me pica el culo")
    raise ValueError("ajajajaj batman")

try:
    prueba_de_errores(2)
except ValueError:
    print(0)
except NotImplementedError:
    print(1)

#ejercicio uno


import time
from MyTime import My_time

t0 = time.clock()
def recursion_depth(number):
    #analiza si puede ir más a fondo recursivamente
    try:
        recursion_depth(number+1)
        number += 1
    except RecursionError:
        print("I can´t go any deeper", number)

recursion_depth(0)
t1 = time.clock()

print("time transcurred: ", My_time(0,0,t1-t0))
print(t1-t0)
"""

def readposint():
    #ESTA función maneja sus propios errores y le avisa al usuario en que se equivocó
    a = input("ingrese un número entero positivo: ")
    try:
        float(a)
    except:
        if a=="":
            print("no se ingresó nada")
        elif type(a) == str:
            print("ingresaste letras, no números")
    else:
        if float(a)<=0:
            print("se ingresó número negativo o nulo")
        elif float(a)>float(a)//1:
            print("ingresó un número con decimales")
        else:
            print("se ingresó un número correcto",int(float(a)))
    finally:
        print("Adios vuelva, pronto")

def readposint_v2():
    # esta función eleva sus errores para que las capte algún try
    a = input("ingrese un número entero positivo: ")
    try:
        float(a)
    except ValueError:
        if a == "":
            error0 =  ValueError("no se ingresó nada")
            raise error0
        elif type(a) == str:
            error1 = TypeError("ingresaste letras, no números")
            raise error1
    else:
        if float(a) <= 0:
            error2 = RuntimeError("se ingresó número negativo o nulo")
            raise error2
        elif float(a) > float(a) // 1:
            error3 = AttributeError("ingresó un número con decimales")
            raise error3
        else:
            print("se ingresó un número correcto", int(float(a)))

try:
    #como dentro de cada excepción se llama a la función pero sin "try" si hay un error, el programa va a tener un error, y va a salir el error levantado.
    readposint_v2()
except ValueError:
    print("no se ingresó nada, vuelva a intentar, mientras más parctiques más suerte vas a tener")
    readposint_v2()
except TypeError:
    print("ingresaste letras, no números, vuelva a intentar, mientras más parctiques más suerte vas a tener")
    readposint_v2()
except RuntimeError:
    print("se ingresó número negativo o nulo, vuelva a intentar, mientras más parctiques más suerte vas a tener")
    readposint_v2()
except AttributeError:
    print("ingresó un número con decimales, vuelva a intentar, mientras más parctiques más suerte vas a tener")
    readposint_v2()
else:
    print("ingresaste un número correcto")
finally:
    print("Adios, y disfrute la vida")


import math

s = int(input("ingrese segundos ", ))

h = s//3600

remainsecs = s%3600

m = remainsecs//60

remainsecs2=remainsecs%60

longsegundero = float(input("ingrese la longitud de la aguja del segundero en metros: ", ))
longhorero = float(input("ingrese la longitud de la aguja que marca la hora en metros:", ))
z=0
if h<24:
    d=0
    h=h-24

    print("equivale a ",d, " días", h," horas", m," minutos y", remainsecs2," segundos")
    z1 = 2 * math.pi * longsegundero * s / 60
    print("la punta del segundero recorrió ", z1, " metros")
    z = 2 * math.pi * longhorero * s / 3600
    print("la punta de la aguja que marca la hora recorrió ", z, " metros")
elif 24<h<8766:
    d=h//24
    h=h-d*24

    print("equivale a ", d, " días", h, " horas", m, " minutos y", remainsecs2, " segundos")
    z1=2 * math.pi * longsegundero * s / 60
    print("la punta del segundero recorrió ", z1, " metros")
    z=2 * math.pi * longhorero * s / 3600
    print("la punta de la aguja que marca la hora recorrió ", z, " metros")
elif 8766<h:
    d=h//24
    a=d//365
    h = h - 24 * d
    d=d-365*a

    print("equivale a ", a," años", d, " días", h, " horas", m, " minutos y", remainsecs2, " segundos")
    z1 = 2 * math.pi * longsegundero * s / 60
    print("la punta del segundero recorrió ", z1, " metros")
    z = 2 * math.pi * longhorero * s / 3600
    print("la punta de la aguja que marca la hora recorrió ", z, " metros")
else:
    print("ey caiste fuera de la edad del universo")

print("pensar que el segundero recorrió una distancia equivalente al ",z1/(384400*1000)*100, " % de la distancia entre la Tierra y la Luna")
print("y pensar que la aguja que marca la hora recorrió una distancia equivalente al ",100*z/(384400*1000), " % de la distancia entre la Tierra y la Luna")


input("")
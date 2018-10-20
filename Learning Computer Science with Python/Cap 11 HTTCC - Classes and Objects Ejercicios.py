"""


def double(a):
    print(a * 2)
    return a*2


class mate:
    #te da información

    def __init__(self,mate,yerba,temperatura):
        self.mate = ""
        self.yerba = ""
        self.temperatura = 0

    def cantidad_cebadas(self,litros,tamaño_mate_cm3):
        return litros/(0.001*tamaño_mate_cm3)

    def temperatura_correcta(temperatura):
        if 70<temperatura<81:
            print("la temperatura es correcta")
        elif temperatura>=81:
            print("la temperatura es alta")
        else:
            print("la temperatura es baja")



import Point
#from Point import mate,point,double
#from Point import *

a = Point.point(5,9)
b = Point.point(3,2)

Point.point.show(a)

Point.point.show(b)

Point.double(500000)

mat = Point.mate("madera","sin palo",80)

print("{0:.2f}".format(mat.cantidad_cebadas(1,9)))

Point.mate.temperatura_correcta(75)



from Point import point

a = point()

a.x = 3
a.y = 99

point.show(a)
print(point.show(a))



#1
import Point

a = Point.point(1,1)
b = Point.point(0,0)

print(Point.point.distance_pq(a,b))

#2
import Point
a = Point.point(3,5)
q = Point.point.reflect_x(a)

q.show()

#3

from Point import point
a = point(3,5)
print(a.slope_from_origin())


#4
import Point
a = Point.point(5,5)

print(a.get_line_to(Point.point(3,2)))
if a.get_line_to(Point.point(3,2))[1]<0:
    print("y={0}x-{1}".format(a.get_line_to(Point.point(3, 2))[0], (-1)*a.get_line_to(Point.point(3, 2))[1]))
else:
    print("y={0}x+{1}".format(a.get_line_to(Point.point(3,2))[0],a.get_line_to(Point.point(3,2))[1]))


#5

#tremendo ejercicio donse se usó algebra lineal para obtener la ecuación de cualquier circunferencia general
#claramente basta con dar 3 puntos sobre una circunferencia  y el sistema tendrá solución compatible determinada
# dar cuatro puntos es superfluo, luego, con 4 pu

import Point

#a = Point.point3(1,2,1)
#b = Point.point3(3,2,1)
#c = Point.point3(3,0,1)

a = Point.point3(1,0,1)
b = Point.point3(0,1,1)
c = Point.point3(-1,0,1)


def matrix(a,b,c):
    #HAGO LA MATRIZ DE COEFICIENTES CON LOS 3 PUNTOS
    #devuelve el determinante de una matriz de 3x3 compuesta por 3 puntos en R3

    return [[a.x,a.y,a.z],[b.x,b.y,a.z],[c.x,c.y,a.z]]

def result(a,b,c):
    return [-(a.x)**2-(a.y)**2,-(b.x)**2-(b.y)**2,-(c.x)**2-(c.y)**2]

def det(a,b,c):
    return ((a.x)*((b.y)*(c.z)-(c.y)*(b.z))-(a.y)*((b.x)*(c.z)-(b.z)*(c.x))+(a.z)*((b.x)*(c.y)-(b.y)*(c.x)))

def trasp(a,b,c):
  return [[a.x,b.x,c.x],[a.y,b.y,c.y],[a.z,b.z,c.z]]

def det(a,b,c):
    return ((a.x)*((b.y)*(c.z)-(c.y)*(b.z))-(a.y)*((b.x)*(c.z)-(b.z)*(c.x))+(a.z)*((b.x)*(c.y)-(b.y)*(c.x)))

def inverse_matrix(a,b,c):
    k = det(a,b,c)
    if k!=0:
        p = [((b.y)*(c.z)-(b.z)*(c.y))/k,-((a.y)*(c.z)-(a.z)*(c.y))/k,((a.y)*(b.z)-(a.z)*(b.y))/k]
        q = [-((b.x)*(c.z)-(b.z)*(c.x)),((a.x)*(c.z)-(a.z)*(c.x))/k,-((a.x)*(b.z)-(a.z)*(b.x))/k]
        r = [((b.x)*(c.y)-(b.y)*(c.x))/k,-((a.x)*(c.y)-(a.y)*(c.x))/k,((a.x)*(b.y)-(a.y)*(b.x))/k]
    else:
        return None
    return [p,q,r]

def matriz_x_vector(a,b,c):
    p,q,r = 0,0,0
    for i in range(3):
        p += inverse_matrix(a,b,c)[0][i]*result(a,b,c)[i]
        q += inverse_matrix(a,b,c)[1][i]*result(a,b,c)[i]
        r += inverse_matrix(a,b,c)[2][i]*result(a,b,c)[i]
    return [p,q,r]


matrix(a,b,c)

print(matriz_x_vector(a,b,c))

print(det(a,b,c))

print(inverse_matrix(a,b,c))

h = -matriz_x_vector(a,b,c)[0]/2
k = -matriz_x_vector(a,b,c)[1]/2
r = (h**2+k**2-matriz_x_vector(a,b,c)[2])**0.5

print("la coordenada del centro del círculo es ({0:.2f},{1:.2f}) cuyo radio es {2:.3f}".format(h,k,r))

#def mid_point_circle(a,b,c,d):



#6

class SMS_store:
    #inbox outbox of text messages

    def __init__(self):
        self.SMS_messages = []

    def show(self):
        print(self.SMS_messages)
        return self.SMS_messages

    def add_new_arrival(self,from_number, time_arrived, text_of_SMS):
        a = (False,from_number,time_arrived,text_of_SMS)
        self.SMS_messages.append(a)
        return self.SMS_messages

    def messagecount(self):
        return len(self.SMS_messages)

    def get_unread_indexes(self):
        list_indexes = []
        for i,message in enumerate(self.SMS_messages):
            if message[0] == False:
                list_indexes.append(i)
        print(list_indexes)
        return list_indexes

    def get_message(self,i):
        if i not in range(len(self.SMS_messages)):
            return None
        else:
            a = (True,self.SMS_messages[i][1],self.SMS_messages[i][2],self.SMS_messages[i][3])
            self.SMS_messages = self.SMS_messages[0:i] +[a]+ self.SMS_messages[i + 1:]

            print(self.SMS_messages[i])
            return self.SMS_messages[i]

    def delete(self,i):
        if i not in range(len(self.SMS_messages)):
            return None
        else:
            self.SMS_messages = self.SMS_messages[0:i]+self.SMS_messages[i+1:]
            return self.SMS_messages

    def clear(self):
        self.SMS_messages = []

a = (1159237644,"12:15am","hola amor, por favor comprá frutas")

my_inbox = SMS_store()

my_inbox.add_new_arrival(1159237644,"12:15am","hola amor, por favor comprá frutas")
my_inbox.add_new_arrival(1153254205,"12:01pm","Maty, vamos a almorzar?")
my_inbox.add_new_arrival(1161782815,"14:30am","hola hijo ! felicitaciones")
my_inbox.add_new_arrival(1169437018,"13:30pm","Maty tenemos un problema")
my_inbox.add_new_arrival(123123132,"12:00am","error message")
my_inbox.add_new_arrival(1151390283,"12:34am","Maty terminá veterinarias")

my_inbox.show()

print(my_inbox.messagecount())

my_inbox.get_message(5)
my_inbox.get_message(1)

my_inbox.get_unread_indexes()

my_inbox.delete(4)

my_inbox.show()

my_inbox.clear()

my_inbox.show()


#el capítulo cambia en excepciones

#1,2,3
from Point import point

class Rectangle:
    #dibuja un rectangulo dando su esquina superior izquierda

    def __init__(self,position,width,height):
        self.left_lower_corner = position
        self.width = width
        self.height = height

    def __str__(self):
        return "({0},{1},{2})".format(self.left_lower_corner,self.width,self.height)

    def area(self):
        return (self.width)*(self.height)

    def perimeter(self):
        return 2*(self.width)+2*(self.height)

    def flip(self):
        a,b = self.width,self.height
        self.width = b
        self.height = a

    def contains(self,test):
        ok1 = False # test for x coordinate
        ok2 = False # test for y coordinate

        #lógica para verificar que pertenece al intervalo en x

        lx = self.left_lower_corner.x
        ux = self.left_lower_corner.x+self.width
        if test.x == ux:
            return False
        if lx <= ux:
            if lx <= test.x < ux:
                ok1 = True
        elif ux <= lx:
            if ux < test.x <= lx:
                ok1 = True

        # lóica para verificar que pertenece al intervalo en y

        ly = self.left_lower_corner.y
        uy = self.left_lower_corner.y + self.height
        if test.y == uy:
            return False
        if ly <= uy:
            if ly <= test.y < uy:
                ok2 = True
        elif uy <= ly:
            if uy < test.y <= ly:
                ok2 = True

        if ok1 and ok2:
            return True
        else:
            return False

    def collide_with(self,r):
        if r.left_lower_corner.x <= r.left_lower_corner.x + r.width:
            rlx = r.left_lower_corner.x
            rux = r.left_lower_corner.x + r.width
        else:
            rux = r.left_lower_corner.x
            rlx = r.left_lower_corner.x + r.width

        if r.left_lower_corner.y <= r.left_lower_corner.y+r.height:
            rly = r.left_lower_corner.y
            ruy = r.left_lower_corner.y + r.height
        else:
            ruy = r.left_lower_corner.y
            rly = r.left_lower_corner.y+r.height

        if self.left_lower_corner.x <= self.left_lower_corner.x + self.width:
            lx = self.left_lower_corner.x
            ux = self.left_lower_corner.x + self.width
        else:
            ux = self.left_lower_corner.x
            lx = self.left_lower_corner.x + self.width

        if self.left_lower_corner.y <= self.left_lower_corner.y + self.height:
            ly = self.left_lower_corner.y
            uy = self.left_lower_corner.y + self.height
        else:
            uy = self.left_lower_corner.y
            ly = self.left_lower_corner.y + self.height

        # 3 casos de colisión, primer caso:
        #algún vértice dentro del primero
        # segundo caso algún lado atraviesa completo el cuadrado primero (lado vertical u horizontal)
        # tercer caso: el cuadrado contiene al primero

        if self.contains(r.left_lower_corner)\
                or self.contains(point(r.left_lower_corner.x,r.left_lower_corner.y-r.height)) \
                or self.contains(point(r.left_lower_corner.x+r.width,r.left_lower_corner.y)) \
                or self.contains(point(r.left_lower_corner.x+r.width,r.left_lower_corner.y-r.height)):
            return True

        if r.contains(self.left_lower_corner)\
                or r.contains(point(self.left_lower_corner.x,self.left_lower_corner.y-self.height)) \
                or r.contains(point(self.left_lower_corner.x+self.width,self.left_lower_corner.y)) \
                or r.contains(point(self.left_lower_corner.x+self.width,self.left_lower_corner.y-self.height)):
            return True

        if (rlx <= lx) and (ux <= rux) and ((ly <= rly <= uy) or (ly <= ruy <= uy)):
            return True

        if (rly <= ly) and (uy <= ruy) and ((lx <= rlx <= ux) or (lx <= rux <= ux)):
            return True

        return False



r = Rectangle(point(0,0),10,5)

print(str(r))
print(r.area())
print(r.area() == 50)

print(r.perimeter())
print(r.perimeter() == 30)

print(r.width == 10 and r.height == 5)
print(r.width,r.height)
# r.flip()
print(r.width,r.height)
print(r.width == 5 and r.height == 10)

#4
def test(a):
    print(a)
print("sadsdasda")
test(r.contains(point(0, 0)))
test(r.contains(point(3, 3)))
test(not r.contains(point(3, 7)))
test(not r.contains(point(3, 5)))
test(r.contains(point(3, 4.99999)))
test(not r.contains(point(-3, -3)))

#5

r1 = Rectangle(point(1,1),10,5)
r2 = Rectangle(point(3,3),3,4)
r3 = Rectangle(point(5,1),10,3)
r4 = Rectangle(point(55,55),20,10)

print(r1.collide_with(r4))


#EVEN MORE OOP (OBJECT ORIENTED PROGRAMMING) !

#1

class My_time:

    def __init__(self,h=0,m=0,s=0):

        #Calcula el tiempo en horas, minutos y segundos como atributos. Puede ser creado pasando cualquier número en cualuquiera
        #de los 3 campos.

        totalsecs = 3600*h+60*m+s
        totalhours = totalsecs//3600
        segundos_sobrantes = totalsecs % 3600
        totalminutes = segundos_sobrantes // 60
        finalseconds = segundos_sobrantes % 60

        self.h = totalhours
        self.m = totalminutes
        self.s = finalseconds

    def __str__(self):
        return "({0} hs.,{1} mins.,{2} segs.)".format(self.h, self.m, self.s)

    def to_secs(self):
        return 3600*self.h+60*self.m+self.s

    def __eq__(self,t1):
        return My_time.to_secs(self) == My_time.to_secs(t1)

    def __lt__(self,t1):
        return My_time.to_secs(self) < My_time.to_secs(t1)

    def __gt__(self,t1):
        return My_time.to_secs(self) > My_time.to_secs(t1)

    def __le__(self,t1):
        return My_time.to_secs(self) <= My_time.to_secs(t1)

    def __ge__(self,t1):
        return My_time.to_secs(self) >= My_time.to_secs(t1)

    def __add__(self,t1):
        x = My_time(0,0,My_time.to_secs(self)+My_time.to_secs(t1))
        if x.to_secs()<0:
            return "No existe el tiempo negativo, la entropía del universo siempre crece, con lo cual no puede volverse al estado anterior de menor entropía, los sistemas reversibles son ideales" \
                   "y no existen en la naturaleza"
        else:
            return x

    def between(self,t1,t2):
        return t1 <= self < t2



t0 = My_time(487,2554,2156)
print(str(t0))

t1 = My_time(484,2554,2156)
t2 = My_time(489,2554,2156)

print(t0.between(t1,t2))

#2 Lo hice así de una

#3
t4 = My_time(434343,2342,323)
t5 = My_time(22,22323,333333333)
print(t2 <= t4)
print(t2 == t2)
print(t5 > t4)

#4

t6 = My_time(0,0,-335)
t7 = My_time(0,1,15)

print(t6+t7)
"""
#tema CARTAS ESTÁ EN EL ARCHIVO "CARDS"

#MÁS EJERCICIOS

#1 ya está implementado en el módulo "CARDS"

#2
from turtle import Turtle,Screen

class TurtleGTX(Turtle):

    dist_total = 0
    dist_rodando = 0
    dist_volando = 0
    random_number = 0
    tyre_flat = False
    import random
    rng = random.Random()
    random_number = rng.randrange(dist_rodando, dist_rodando + 10000)

    def jump_forward(self,distance):
        TurtleGTX.penup(self)
        TurtleGTX.forward(self,distance)
        TurtleGTX.pendown(self)
        if distance < 0 :
            self.dist_total += -distance
            self.dist_volando += -distance
        else:
            self.dist_total += distance
            self.dist_volando += distance

    def forward2(self, distance):
        if self.dist_rodando == self.random_number or self.tyre_flat == True:
            self.tyre_flat = True
            raise AttributeError("la goma está pinchada")

        else:
            TurtleGTX.forward(self, distance)
            if distance < 0 :
                self.dist_total += -distance
                self.dist_rodando += -distance
            else:
                self.dist_total += distance
                self.dist_rodando += distance

    def change_tyre(self):
        if self.tyre_flat == True:
            self.dist_rodando += 1
            self.tyre_flat = False
            #print("se arregló goma")


alex = TurtleGTX()
window = Screen()
alex.forward2(100)

alex.jump_forward(-100)
try:
    alex.forward2(100)
except AttributeError:
    alex.change_tyre()
    print("la goma está arreglada")
else:
    print("auto funcionando perfectamente")
finally:
    print("gracias por su atención")

alex.forward2(100)
alex.forward2(100)

print("distancia total recorrida ",alex.dist_total,"m")
print("distancia rodando recorrida ",alex.dist_rodando,"m")
print("distancia volando recorrida ",alex.dist_volando,"m")


window.mainloop()









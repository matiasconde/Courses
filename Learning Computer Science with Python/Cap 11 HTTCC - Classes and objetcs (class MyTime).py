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

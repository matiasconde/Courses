class point:
    """Crea una clase de un punto en el plano R2"""

    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def show(self):
        print(self.x,self.y)
        return (self.x,self.y)

    def __str__(self):
        return "({0},{1})".format(self.x,self.y)

    def distance_pq(p,q):
        return(((p.x-q.x)**2+(p.y-q.y)**2)**0.5)

    def reflect_x(p):
        q = point(p.x,-p.y) #al no colocar self, hay que llamarla así: Point.point.reflect_x(p)
        return(q)

    def slope_from_origin(self): #se pone self porque es más facil llamarla desde un objeto ya creado de esta manera: sea un punto q luego, q.slope_from_origin()
        return (self.y/self.x)

    def get_line_to(self,q):
        a = (self.y-q.y)/(self.x-q.x)
        b = self.y-a*self.x
        return (a,b)

class point3:
    """Crea una clase de un punto en el plano R2"""

    def __init__(self,x=0,y=0,z=0):
        self.x = x
        self.y = y
        self.z = z

    def show(self):
        print(self.x,self.y,self.z)
        return (self.x,self.y,self.z)

    def distance_pq(p,q):
        return(((p.x-q.x)**2+(p.y-q.y)**2+(p.z-q.z)**2)**0.5)

    def reflect_xz(p):
        q = point(p.x,-p.y,p.z) #al no colocar self, hay que llamarla así: Point.point.reflect_x(p)
        return(q)

    def slope_from_origin_xy(self): #se pone self porque es más facil llamarla desde un objeto ya creado de esta manera: sea un punto q luego, q.slope_from_origin()
        return (self.y/self.x)

    def get_line_to_xy(self,q):
        a = (self.y-q.y)/(self.x-q.x)
        b = self.y-a*self.x
        return (a,b)



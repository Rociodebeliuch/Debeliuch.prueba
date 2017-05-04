class Persona(object):
    nombre=None
    fecha_nac=None
    platos=[]

    def __init__(self):
        self.platos=[]

    def setAgregarnombre(self,n):
        self.nombre=n

    def setAgregarfecha(self,f):
        self.fecha_nac=f

    def setAgregarPlato(self,p):
        self.platos.append(p)




class Vuelos(object):
    avion=None
    l_pasajeros=[]
    l_tripulacion=[]
    fecha=None
    hora=None
    origen=None
    destino=None

    def __init__(self):
        self.l_pasajeros=[]

    def __init__(self):
        self.l_tripulacion=[]

    def Agregaravion(self,av):
        self.avion=av

    def AgregarFecha(self,f):
        self.fecha=f

    def AgregarHora(self,h):
        self.hora=h

    def AgregarOrigen(self,o):
        self.origen=o

    def AgregarDestino(self,d):
        self.destino=d

    def AgregarP(self,p):
        self.l_pasajeros.append(p)

    def AgregarT(self,t):
        self.l_tripulacion.append(t)
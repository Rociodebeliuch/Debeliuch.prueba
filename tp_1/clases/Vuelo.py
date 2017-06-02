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

    def Personas_por_vuelo(self):
        lista_aux = []
        for item in self.l_tripulacion:
            lista_aux.append(item)

        for item2 in self.l_pasajeros:
            lista_aux.append(item2)

        return lista_aux

    def Persona_mas_joven(self):
        aux = self.l_pasajeros[1].fecha_nac
        persona_aux = None
        for item in self.l_pasajeros:
            if item.fecha_nac > aux:
                aux = item.fecha_nac
                persona_aux = item
        return persona_aux

    def NoseAlcanza(self):
        cant = True
        if len(self.l_tripulacion) < self.avion.cant_trip:
            cant = False
        return cant

    def EstaAutorizado(self):
        aux = None
        for item in self.l_tripulacion:
            for item2 in item.modelos_avion:
                if item2 == self.avion.codunico:
                    aux = True
                aux = False
            return aux

    def PersonasVipoNec(self):
        for item in self.l_pasajeros:
            if item.vip == True:
                return item
            if item.n_especiales != None:
                return item


class Equipo(object):
    nombreq=""
    capitan=None
    lista_Jug=[10]
    barrio=None
    listadisp=[]

    def __init__(self):
        self.listadisp=[]
        self.listadisp=[[False,False,False],[False,False,False],[False,False,False],[False,False,False],[False,False,False],[False,False,False]]



    def setAgregarNombreE(self,nomb):
        self.nombreq=str(nomb)

    def setAgregarJugador(self,nombre):
        self.lista_Jug.append(nombre)

    def setAgregarBarrio(self,nomb):
        self.barrio=str(nomb)

    def setAgregarCapitan(self,capitan):
        if capitan in self.lista_Jug:
            self.capitan = capitan
            return True

        return False

    def AgregarDisponibilidad(self,dia,turno):
        self.listadisp [dia][turno]=True






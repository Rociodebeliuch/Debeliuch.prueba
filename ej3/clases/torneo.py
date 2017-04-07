
class Torneo (object):
    listaPartidos=[]
    listaEquipos=[]

    def __init__(self):
        self.listaPartidos=[]

    def __init__(self):
        self.listaEquipos=[]

    def setAgregarEquipo(self,nombre):
        if nombre in self.listaEquipos:
            return False

        self.listaEquipos.append(nombre)
        return True

    def setAgregarPartido(self,partido):
        self.listaPartidos.append(partido)

    def calcularFixture(self):
        for item in self.listaEquipos:
            if





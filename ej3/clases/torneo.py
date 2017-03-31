
class Torneo (object):
    listaPartidos=[]
    listaEquipos=[]

    def setAgregarEquipo(self,nombre):
        if nombre in self.listaEquipos:
            return False
        self.listaEquipos.append(nombre)
        return True

    def setAgregarPartido(self,partido):
        self.listaPartidos.append(partido)
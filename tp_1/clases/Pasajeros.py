from .Personas import Personas


class Pasajeros(Personas):
    cant_millas = None
    pasajeros_vip = None
    n_especiales = None


    def vip(self, v):
        self.pasajeros_vip = v

    def NecesidadesEsp(self, n):
        self.n_especiales=n


    def millas(self, m):
        self.cant_millas = m
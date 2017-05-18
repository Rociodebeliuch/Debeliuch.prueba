class Pasajeros(Personas):
    cant_millas=None
    pasajeros_vip=False
    n_especiales=False

    def tipo(self):
        self.pasajeros_vip=True

    def necesidad_esp(self):
        self.n_especiales=True

    def millas(self,m):
        self.cant_millas=m
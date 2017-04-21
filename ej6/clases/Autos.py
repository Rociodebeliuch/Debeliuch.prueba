class Autos(Vehiculos):
    descapotable=True

    def setAgregar_patente(self, p):
        self.patente = p


    def setAgregar_cantruedas(self, can):
        self.cantidad_ruedas = can


    def setAgregar_añodef(self, fecha):
        self.a_fabricacion = fecha

    def setDescapotable(self,d):

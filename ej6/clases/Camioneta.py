class Camioneta(Vehiculos):
    capacidad_carga=None

    def setAgregar_capacidad(self,c):
        self.capacidad_carga=c

    def setAgregar_patente(self,p):
        self.patente=p

    def setAgregar_cantruedas(self,can):
        self.cantidad_ruedas=can

    def setAgregar_añodef(self,fecha):
        self.a_fabricacion=fecha

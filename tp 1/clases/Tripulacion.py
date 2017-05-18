class Tripulacion(Personas):
    modelos_avion=[]


    def __init__(self):
        self.modelos_avion=[]

    def AgregarModelo(self,mod):
        self.modelos_avion=mod

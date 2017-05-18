class Servicio(Tripulacion):
    idiomas=[]

    def __init__(self):
        self.idiomas=[]

    def AgregarIdiom(self,i):
        self.idiomas.append(i)
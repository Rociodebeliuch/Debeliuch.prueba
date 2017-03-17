class Materia(object):

    nombre=""
    ListaDeN=[]
    def __init__(self):
        self.ListaDeN=[]

    def setAgregarNota(self,nota):
        self.ListaDeN.append(nota)

    def setPromedioMat(self):
        return sum(self.ListaDeN)/len(self.ListaDeN)


from .materia import Materia
class Alumno(object):
    nombre= ""
    apellido=""
    fechaden=None
    Lista=[]
    ListaMaterias=[]
    aux=0

    def __init__(self):
        self.ListaMaterias=[]

    def setNombre(self,n):
        self.nombre=str(n)

    def setApellido(self,a):
        self.apellido=str(a)

    def setFecha(self,fecha):
        self.fechaden=fecha

    def agregarNota(self,nota):
        self.Lista.append(nota)

    def menorNota(self):
        return min(self.Lista)

    def mayorNota(self):
        return max(self.Lista)

    def prom(self):
        return sum(self.Lista)/len(self.Lista)

    def PromedioAlumnos (self):
        self.aux=0
        for Contador in self.ListaMaterias:
            self.aux=self.ListaMaterias[Contador].setPromedioMat()+self.aux

        return self.aux/len(self.ListaMaterias)

    def MenorProm (self):
        for Contador in self.ListaMaterias:
            return min(self.ListaMaterias.setPromedioMat())

    def MayorProm(self):
        for Contador in self.ListaMaterias:
            return max(self.ListaMaterias.setPromedioMat())

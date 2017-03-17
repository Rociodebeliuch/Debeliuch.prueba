from clases.materias import Materia
class Alumno(object):
    nombre= ""
    apellido=""
    fechaden=None
    Lista=[]
    materias=[]

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

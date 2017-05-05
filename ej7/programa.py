from Alumno import Alumno
from Pedido import Pedido
from Persona import Persona
from Plato import Plato
from Profesor import Profesor
listaP=[]




def Agregaralumno(n,a,d):
    alumno=Alumno()
    alumno.setAgregarNombre(n)
    alumno.setAgregarApellido(a)
    alumno.set_division(d)
    listaP.append(alumno)

def Agregarprofesor(n,a):
    profesor=Profesor()
    profesor.setAgregarNombre(n)
    profesor.setAgregarApellido(a)
    listaP.append(profesor)

def Modificaralumno(i):
    for item in listaP:
        if item.dni==i:







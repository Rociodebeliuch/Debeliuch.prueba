from clases.Persona import Persona
from clases.Alumno import Alumno
from Pedido import Pedido
from Plato import Plato
from clases.Profesor import Profesor
from datetime import date


listaPe=[]
listaP=[]
listaPl=[]
def main():
    print("1-Agregar Persona")
    print("2-Modificar Persona")
    print("3-Eliminar Persona")
    print("4-Agregar Pedido")
    print("5-Modificar Pedido")
    print("6-Eliminar Pedido")
    print("7-Agregar Plato")
    print("8-Modificar Plato")
    print("9-Eliminar Plato")
    nombre = None
    apellido = None
    division = None
    descuento = None
    dni = None
    fecha=None
    print("ingrese opcion")
    opcion=input()
    opcion2=input()
    if opcion== 1:
        print("1-Agregar Alumno")
        print("Agregar Profesor")
        opcion2=input()
        if opcion2==1:
            nombre = input()
            apellido = input()
            division = input()
            dni = input()
            Agregaralumno(nombre, apellido, division, dni)

        elif opcion2==2:
              nombre=input()
             apellido=input()
             descuento=input()
             dni=input()
             Agregarprofesor(nombre,apellido,dni,descuento)

    elif opcion==2:
        print("1-Modificar Alumno")
        print("2-Modificar Profesor")

        if opcion2==3:
            Modificaralumno(nombre,apellido,dni,division)

         elif opcion2== 4:
            nombre=input()
             apellido=input()
             dni=input()
            descuento=input()
            Modificarprofesor(nombre,apellido,dni,descuento)

    elif opcion==3:
        print("1-Eliminar Alumno")
        print("2-Eliminar Profesor")
        dni = input()
        if opcion2==5:
            Eliminaralumno(dni)

        elif opcion2==6:
            Eliminarprofesor(dni)

    elif opcion==4:

        Agregarpedido(fecha,hora,plato,entrega,persona,idd)

    elif opcion==5:
    elif
















def Agregaralumno(n,a,div,dni):
    alumno=Alumno()
    alumno.setAgregarNombre(n)
    alumno.setAgregarApellido(a)
    alumno.set_division(div)
    alumno.setAgregardni(dni)
    listaP.append(alumno)

def Agregarprofesor(n,a,dni,desc):
    profesor=Profesor()
    profesor.setAgregarNombre(n)
    profesor.setAgregarApellido(a)
    profesor.setAgregardni(dni)
    profesor.setAgregardesc(desc)
    listaP.append(profesor)

def Modificaralumno(nombre,apellido,dni,div):
    for item in listaP:
        if type(item) is Alumno:
            if item.dni==dni:
                item.setAgregarNombre(nombre)
                item.setAgregarApellido(apellido)
                item.set_division(div)

def Modificarprofesor(nombre,apellido,dni,descuento):
    for item in listaP:
        if type(item) is Profesor:
            if item.dni==dni:
                item.setAgregarNombre(nombre)
                item.setAgregarApellido(apellido)
                item.setAgregardesc(descuento)

def Eliminaralumno(dni):
    for item in listaP:
        if type(item) is Alumno:
            if item.dni==dni:
                listaP.remove(item)

def Eliminarprofesor(dni):
    for item in listaP:
        if type(item)is Profesor:
            if item.dni==dni:
                listaP.remove(item)

def Agregarplato(nombre,precio):
    plato=Plato()
    plato.setAgregarNombre(nombre)
    plato.setAgregarPrecio(precio)
    listaPl.append(plato)

def Modificarplato(nombre,n,precio):
    for item in listaPl:
        if item.nombre==nombre:
            item.setAgregarNombre(n)
            item.setAgregarPrecio(precio)

def Eliminarplato(nombre):
    for item in listaPl:
        if item.nombre==nombre:
            listaPl.remove(item)

def Agregarpedido(fecha,hora,plato,entrega,persona,idd):
    pedido=Pedido()
    pedido.setAgregarFecha(fecha)
    pedido.setHoraEntrega(hora)
    pedido.se_entrega(entrega)
    pedido.setPersona(persona)
    pedido.setPlato(plato)
    pedido.setid(idd)
    listaPe.append(pedido)

def Modificarpedido(idd,fecha,hora,plato,entrega,persona):
    for item in listaPe:
        if item.id_pedido==idd:
            item.setAgregarFecha(fecha)
            item.setHoraEntrega(hora)
            item.se_entrega(entrega)
            item.setPersona(persona)
            item.setPlato(plato)

def Eliminarpedido(idd):
    for item in listaPe:
        if item.id_pedido==idd:
            listaPe.remove(item)





























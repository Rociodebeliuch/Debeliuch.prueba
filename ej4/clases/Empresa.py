class Empresa(object):
    lista_empleados=[]

    def __init__(self):
        self.lista_empleados=[]

    def setAgregar_empleado(self,empleado):
        self.lista_empleados.append(empleado)
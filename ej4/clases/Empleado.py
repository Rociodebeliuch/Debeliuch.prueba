class Empleado(object):
    nombre=None
    apellido=None
    telefono=None
    fecha_nac=None
    disponibilidad=[]
    asistencias=[]


    def __init__(self):
        self.disponibilidad=[]

    def setNombre(self,n):
        self.nombre=n

    def setApellido(self,ap):
        self.apellido=ap

    def setTel(self,tel):
        self.telefono=tel

    def setFechaNac(self,fecha):
        self.fecha_nac=fecha

    def AgregarDisponibilidad(self, dia):
        self.disponibilidad[dia] = True

    def setAgregarAsistencia(self,a):
        self.lista_empleados.append(a)
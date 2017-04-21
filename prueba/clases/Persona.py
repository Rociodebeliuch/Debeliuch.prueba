class Persona (object):
    nombre=None
    apellido=None
    fecha_nac=None

    def setAgregarNombre(self,n):
        self.nombre=n

    def setAgregarApellido(self,a):
        self.apellido=a

    def setAgregarFechaNac(self,fecha):
        self.fecha_nac=fecha
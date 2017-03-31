class Jugador(object):
    nombre=""
    fecha_nac=None
    nro_cam=None


    def setNombre(self,nom):
        self.nombre=str(nom)

    def setFechaDeNac(self,fecha_nacimiento):
        self.fecha_nac=fecha_nacimiento

    def setNroCam(self,nro_camiseta):
        self.nro_cam=nro_camiseta

class Pedido(object):
    fechaCreacion=None
    HoraEntrega=None
    Plato=None
    Se_entrega=False
    persona=None
    id_pedido=None



    def setAgregarFecha(self,f):
        self.fechaCreacion=f

    def setHoraEntrega(self,h):
        self.HoraEntrega=h

    def se_entrega(self):
        self.Se_entrega=True

    def setPlato(self,pl):
        self.Plato=pl

    def setPersona(self,p):
        self.persona=p

    def setid(self,idd):
        self.id_pedido=idd
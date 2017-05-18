from clases.Aviones import Aviones
from clases.Pasajeros import Pasajeros
from clases.Personas import Personas
from clases.Piloto import Piloto
from clases.ServicioBordo import Servicio
from clases.Tripulacion import Tripulacion
from clases.Vuelos import Vuelos

    listaP=[]

    def AgregarPasajero(nom,ap,fec,di,mill):
        un_pasajero=Pasajeros()
        un_pasajero.setAgregarNombre(nom)
        un_pasajero.setAgregarApellido(ap)
        un_pasajero.setAgregarFechaN(fec)
        un_pasajero.setAgregarDni(di)
        un_pasajero.millas(mill)
        listaP.append(un_pasajero)

    def AgregarPiloto(nom,ap,fec,di):
        un_piloto=Piloto()
        un_piloto.setAgregarNombre(nom)
        un_piloto.setAgregarApellido(ap)
        un_piloto.setAgregarFechaN(fec)
        un_piloto.setAgregarDni(di)

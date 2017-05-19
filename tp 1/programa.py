from clases.Aviones import Aviones
from clases.Pasajeros import Pasajeros
from clases.Personas import Personas
from clases.Piloto import Piloto
from clases.ServicioBordo import Servicio
from clases.Tripulacion import Tripulacion
from clases.Vuelos import Vuelos
    listaV=[]
    listaPasj=[]
    listaTrip=[]
    listaAv=[]
    listaP=[]

    f=open('/home/alumno/Descargas/personas.txt')

    for persona in f:
        listaP=persona.split("|")
        unPasajero=Pasajeros

        





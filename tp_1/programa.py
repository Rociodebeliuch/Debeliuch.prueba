from clases.Avion import Aviones
from clases.Pasajeros import Pasajeros
from clases.Personas import Personas
from clases.Piloto import Piloto
from clases.ServaBordo import Servicio
from clases.Tripulantes import Tripulacion
from clases.Vuelo import Vuelos

listaVuelos = []
listaAv = []
listaPer = []


def AgregarAviones():
    f = open('/home/alumno/Descargas/aviones.dat', 'r')
    for line in f:
        un_avion = Aviones()
        lista = line.split('|')
        un_avion.setcod(lista[0])
        un_avion.setAgregarCantP(lista[1])
        un_avion.setAgregarCantT(lista[2])
        listaAv.append(un_avion)

    f.close()

def AgregarPersonas():
    f=open('/home/alumno/Descargas/personas.dat', 'r')
    for line in f:
        una_persona=Personas()
        l=line.split('|')
        if l[0]=="Pasajero":
            un_pasajero=Pasajeros()
            un_pasajero.setAgregarNombre(l[1])
            un_pasajero.setAgregarApellido(l[2])
            un_pasajero.setAgregarFechaN(l[3])
            un_pasajero.setAgregarDni(l[4])
            if l[5]==0:
                un_pasajero.vip(None)
            else:
                 un_pasajero.vip(l[5])
            if len(l)==6:
                un_pasajero.NecesidadesEsp(l[6])
            else:
                un_pasajero.NecesidadesEsp(None)
            listaPer.append(un_pasajero)

        if l[0]=="Piloto":
            un_piloto=Piloto()
            un_piloto.setAgregarNombre(l[1])
            un_piloto.setAgregarApellido(l[2])
            un_piloto.setAgregarFechaN(l[3])
            un_piloto.setAgregarDni(l[4])
            if (l)==5:
                x=l.split(',')
                largo=len(x)
                while largo <0:
                    for avion in listaAv:
                        if avion.codigo==x[largo]:
                            un_piloto.AgregarModelo(avion)
                    largo=largo-1

            listaPer.append(un_piloto)

        if l[0]=="Servicio":
            un_servicio=Servicio()
            un_servicio.setAgregarNombre(l[1])
            un_servicio.setAgregarApellido(l[2])
            un_servicio.setAgregarFechaN(l[3])
            un_servicio.setAgregarDni(l[4])
            if (l)==5:
                x=l.split(',')
                largo=len(x)
                while largo<0:
                    for item in listaAv:
                        if item.codigo==x[largo]:
                            un_servicio.AgregarModelo(item)
                largo=largo-1
            if(l)==6:
                y=l.split(',')
                long=len(y)
                while long<0:
                    un_servicio.AgregarIdiom(y[long])
                    long=long-1
            listaPer.append(un_servicio)






def AgregarVuelos():
    f = open('/home/alumno/Descargas/vuelos.dat', 'r')
    for line in f:
        l = line.split('|')
        un_vuelo = Vuelos()
        un_vuelo.Agregaravion(l[0])
        un_vuelo.AgregarFecha(l[1])
        un_vuelo.AgregarHora(l[2])
        un_vuelo.AgregarOrigen(l[3])
        un_vuelo.AgregarDestino(l[4])
        if (l)==5:
            x=l.split(',')
            long=len(x)
            while long<0:
                for tripulante in listaPer:
                    if tripulante.dni==x[long]:
                        un_vuelo.AgregarT(tripulante)
                long=long-1
        if(l)==6:
            y=l.split(',')
            largo=len(y)
            while largo<0:
                for pasajero in listaPer:
                    if pasajero.dni==y[largo]:
                         un_vuelo.AgregarP(pasajero)
                largo=largo-1

        listaVuelos.append(un_vuelo)

    f.close()


def TripViajaMas():
    for vuelo in listaVuelos:
        x=vuelo.fecha
        for trip in vuelo.l_tripulantes:
            y=trip.dni
            for item in listaVuelos:
                    if item.fecha==x:
                        for item2 in item.l_tripulantes:
                                if item2.dni==y:
                                    return item2


def mostrarListaAv():
    AgregarAviones()
    for item in listaAv:
        print (item.codigo)
        print (item.cant_pasaj)
        print (item.cant_trip)


mostrarListaAv()

def mostrarListaPersonas():
    AgregarPersonas()
    for item in listaPer:
        print(item.nombre)
        print(item.apellido)
        print(item.fecha_nac)
        print(item.dni)

mostrarListaPersonas()

def mostrarListaVuelos():
    AgregarVuelos()
    for item in listaVuelos:
        print (item.avion)
        print(item.fecha)
        print(item.hora)
        print(item.origen)
        print(item.destino)

        for item2 in item.l_pasajeros:
            print (item2.nombre)
        for item3 in item.l_tripulacion:
            print(item3.nombre)

mostrarListaVuelos()













from datetime import date
from clases.jugador import Jugador
from clases.equipo import Equipo
from clases.torneo import Torneo

jugador1= Jugador()
jugador2= Jugador()
jugador3= Jugador()
jugador4= Jugador()
torneo=Torneo()
equipo=Equipo()




jugador1.setNombre("Alario")
jugador1.setFechaDeNac(date(1990,4,12))
jugador1.setNroCam(7)

jugador2.setNombre("Maidana")
jugador2.setFechaDeNac(date(1986,5,11))
jugador2.setNroCam(10)

jugador3.setNombre("Lopez")
jugador3.setFechaDeNac(date(1986,5,11))
jugador3.setNroCam(10)

jugador4.setNombre("Perez")
jugador4.setFechaDeNac(date(1986,5,11))
jugador4.setNroCam(10)

equipo.setAgregarNombreE("River")
equipo.setAgregarJugador(jugador1)
equipo.setAgregarJugador(jugador2)
equipo.setAgregarJugador(jugador3)
equipo.setAgregarJugador(jugador4)
equipo.setAgregarBarrio("Nuñez")
equipo.setAgregarCapitan(jugador2)

torneo.setAgregarEquipo(equipo)

print(jugador3.nombre)
print(equipo.capitan.nombre)





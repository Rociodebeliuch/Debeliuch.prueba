class Partidos(object):
    dia=None
    turno=""
    equipo1=None
    equipo2=None
    ganador=None

    def DefinirDia(self,d):
        self.dia=d

    def DefinirTurno(self,t):
        self.turno=t

    def DefinirEquipos (self,e1,e2):
        self.equipo1=e1
        self.equipo2=e2

    def DefinirGanador(self,g):
        self.ganador=g




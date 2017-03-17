from clases.alumno import Alumno

from datetime import date
miAlumno=Alumno()
miAlumno.setNombre("A")
miAlumno.setApellido("B")
miAlumno.setFecha(date(2017,3,17))
miAlumno.agregarNota(4)
print(miAlumno.menorNota())
print(miAlumno.prom())
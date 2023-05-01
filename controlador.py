from vista import Vista
from modelo import Modelo

class Controlador:
    obview = Vista()
    obmodel = Modelo()
    obview.notas()
    obmodel.setNombre(obview.nombre)
    obmodel.setNota1(obview.nota1)
    obmodel.setNota2(obview.nota2)
    obmodel.setNota3(obview.nota3)

    name = obmodel.getNombre()
    nota1 = float(obmodel.getNota1())
    nota2 = float(obmodel.getNota2())
    nota3 = float(obmodel.getNota3())

    obmodel.Promediar(nota1,nota2,nota3)

    print("El promedio de nota del estudiante",name, "es", obmodel.getProm())
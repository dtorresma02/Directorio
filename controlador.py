from modelo import Modelo

class Controlador:
    def promediar(nota1, nota2, nota3):
        obmodel = Modelo()
        obmodel.setNota1(nota1)
        obmodel.setNota2(nota2)
        obmodel.setNota3(nota3)

        nota1 = float(obmodel.getNota1())
        nota2 = float(obmodel.getNota2())
        nota3 = float(obmodel.getNota3())

        obmodel.Promediar(nota1,nota2,nota3)

        # print("El promedio de nota del estudiante es", obmodel.getProm())
        return  obmodel.getProm()
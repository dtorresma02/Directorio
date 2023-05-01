class Vista:

    def __init__(self):
        self.nota1 = 0
        self.nota2 = 0
        self.nota3 = 0

        print("Bienvenido al directorio de notas")
        print("Ingrese la nota 1")
        self.nota1 = float(input())
        print("Ingrese la nota 2")
        self.nota2 = float(input())
        print("Ingrese la nota 3")
        self.nota3 = float(input())
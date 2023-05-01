class Modelo:

    def __init__(self):
        self.nombre = ""
        self.nota1 = 0
        self.nota2 = 0
        self.nota3 = 0
        self.prom = 0

    def setNombre(self, nombre):
        self.nombre = nombre

    def setNota1(self, nota1):
        self.nota1 = nota1

    def setNota2(self, nota2):
        self.nota2 = nota2
        
    def setNota3(self, nota3):
        self.nota3 = nota3

    def getNombre(self):
        return self.nombre

    def getNota1(self): 
        return self.nota1
        
    def getNota2(self):
        return self.nota2
        
    def getNota3(self):
        return self.nota3
        
    def getProm(self):
        return self.prom

    def Promediar(self, nota1, nota2, nota3):
        total=nota1+nota2+nota3
        self.prom=total/3

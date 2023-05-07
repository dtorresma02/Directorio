from tkinter import *

class Vista:

    def __init__(self):
        lib = Tk()
        Window = Frame(lib, width=300, height=400)
        Window.pack()

        lbltitulo = Label(Window, text="Bienvenido al directorio de notas").place(x=50, y=30)
        lblnombre = Label(Window, text="Nombre del estudiante:").place(x=20, y=70)
        txtnombre = Entry(Window)
        txtnombre.place(x=150, y=70)
        lblnota1 = Label(Window, text="Ingrese la nota 1:").place(x=20, y=100)
        txtnota1 = Entry(Window)
        txtnota1.place(x=150, y=100)
        lblnota2 = Label(Window, text="Ingrese la nota 2:").place(x=20, y=130)
        txtnota2 = Entry(Window)
        txtnota2.place(x=150, y=130)
        lblnota3 = Label(Window, text="Ingrese la nota 3:").place(x=20, y=160)
        txtnota3 = Entry(Window)
        txtnota3.place(x=150, y=160)

        lib.mainloop()

        """self.nombre = ""
        self.nota1 = 0
        self.nota2 = 0
        self.nota3 = 0

    def notas(self):
        print("Bienvenido al directorio de notas")
        print("Por favor ingrese el nombre del estudiante:")
        self.nombre = input()
        print("Ingrese la nota 1")
        self.nota1 = float(input())
        print("Ingrese la nota 2")
        self.nota2 = float(input())
        print("Ingrese la nota 3")
        self.nota3 = float(input())"""
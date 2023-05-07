from tkinter import *
from controlador import Controlador

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

        def Promediar():
            prom = Controlador.promediar(txtnota1.get(), txtnota2.get(), txtnota3.get())
            cadena = "El promedio del estudiante " + txtnombre.get() + " es " + str(prom)
            Label(Window, text=cadena).place(x=20, y=240)

        Button(Window, text="Promediar", command=Promediar).place(x=120, y=200)

        lib.mainloop()
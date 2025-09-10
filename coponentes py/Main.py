import tkinter as tk
from tkinter import *
import sys
import os




class Main(tk.Tk):
    def __init__(self):
        super().__init__()  # inicializa la ventana principal

        # Título
        self.title("_nombre empresa_")

        # Ventana maximizada
        self.state('zoomed')


# Crear y ejecutar la app
if __name__ == "__main__":
    app = Main()
    app.mainloop()

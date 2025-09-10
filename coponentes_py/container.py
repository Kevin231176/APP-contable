from tkinter import *
import tkinter as tk
from ventas import Ventas
from inventario import inventario
from informacion import info
from pedido import Pedido
from provedor import Provedor
from clientes import Clientes

class Container(tk.Frame):
    def __init__(self, padre, controlador=None):
        super().__init__(padre)  # NO usar pack() ni place() aquí
        self.controlador = controlador
        self.frames = {}

        # Subframes internos
        for F in (Ventas, inventario, Clientes, Pedido, Provedor, info):
            frame = F(self)
            self.frames[F] = frame
            frame.place(x=0, y=40, width=1100, height=610)  # solo para subframes
            frame.config(bg="#C6D9E3", highlightbackground="gray", highlightthickness=1)

        # Botones para cambiar entre subframes
        self.buttons_frame = Frame(self)
        self.buttons_frame.place(x=0, y=0, width=1100, height=40)
        for idx, F in enumerate((Ventas, inventario, Clientes, Pedido, Provedor, info)):
            btn = tk.Button(self.buttons_frame, text=F.__name__, command=lambda f=F: self.show_frame(f))
            btn.grid(row=0, column=idx, padx=5, pady=5)

        # Mostrar el primer subframe
        self.show_frame(Ventas)

    def show_frame(self, frame_class):
        self.frames[frame_class].tkraise()

from tkinter import *
import tkinter as tk
from ventas import Ventas
from inventario import inventario
from informacion import info
from pedido import Pedido
from provedor import Provedor
from clientes import Clientes
import sys
import os 

class Container(tk.Frame):
    def __init__(self, padre, controlador):
        super().__init__(padre) 
        self.controlador = controlador
        self.pack()
        self.place(x=0,y=0,width=1100,height=650)
        self.widgets()
        self.frames = {}
        self.buttons = []

        # Subframes internos
        for f in (Ventas, inventario, Clientes, Pedido, Provedor, info):
            frame = f(self)
            self.frames[f] = frame
            frame.pack()
            frame.config(bg="#C6D9E3", highlightbackground="gray", highlightthickness=1)
            frame.place(x=0, y=40, width=1100, height=610)  # solo para subframes
        # Mostrar el primer subframe
        self.show_frames(Ventas)   

    def show_frames(self, container):
        frame = self.frames[container]
        frame.tkraise()

    def ventas(self):
        self.show_frames(Ventas)
    
    def inventario(self):
        self.show_frames(inventario)
    
    def clientes(self):
        self.show_frames(Clientes)
    
    def pedido(self):
        self.show_frames(Pedido)
    
    def provedor(self):
        self.show_frames(Provedor)
    
    def info(self):
        self.show_frames(info)
    
    def widgets(self):
        frame2 = tk.Frame(self, bg="#ECECEC")
        frame2.place(x=0, y=0, width=1100, height=40)

        self.btn_ventas = Button(frame2, text="Ventas", font="sans 12 bold", command=self.ventas)
        self.btn_ventas.place(x=0, y=0, width=184, height=40)

        self.btn_inventario = Button(frame2, text="Inventario", font="sans 12 bold", command=self.inventario)
        self.btn_inventario.place(x=184, y=0, width=184, height=40)

        self.btn_clientes = Button(frame2, text="Clientes", font="sans 12 bold", command=self.clientes)
        self.btn_clientes.place(x=369, y=0, width=184, height=40)

        self.btn_pedido = Button(frame2, text="Pedido", font="sans 12 bold", command=self.pedido)
        self.btn_pedido.place(x=554, y=0, width=184, height=40)

        self.btn_provedor = Button(frame2, text="Provedor", font="sans 12 bold", command=self.provedor)
        self.btn_provedor.place(x=739, y=0, width=184, height=40)

        self.btn_info = Button(frame2, text="Info", font="sans 12 bold", command=self.info)
        self.btn_info.place(x=923, y=0, width=184, height=40)

        self.buttons = [self.btn_ventas,self.btn_inventario,self.btn_clientes,self.btn_pedido,self.btn_provedor,self.btn_info]
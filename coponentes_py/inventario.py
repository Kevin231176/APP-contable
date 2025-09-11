from tkinter import *
import tkinter as tk


class inventario(tk.Frame):
    
    def __init__(self, padre):
        super().__init__(padre)
        self.widgets()

    def widgets(self):
        label = Label(self,text="Inventario")
        label.pack()
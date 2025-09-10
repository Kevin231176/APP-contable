import tkinter as tk
from tkinter import *
from login import Login
from login import Register
from container import  Container
import sys
import os




class Main(tk.Tk):
    def __init__(self):
        super().__init__()  # inicializa la ventana principal

        # Título
        self.title("_nombre empresa_")
        # Ventana maximizada
        self.state('zoomed')
        self.resizable(False,False)

        container = Frame(self)
        container.configure(bg="#C6D9E3")

        self.frame = {}
        for i in ( container):
            frame = i (container, self)
            self.frames[i] = frame

            self.show_frame(container)
            self.style = ttk.style()
            self.style.theme_use("clam")
    
    def show_frame(self,container):
        frame = self.frame[container]
        frame.tkraise()

    def main():
        app = Main()
        app.mainloop()


if __name__ == "__main__":
    Main()

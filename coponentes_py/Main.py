import tkinter as tk
from tkinter import ttk, Frame
from login import login
from login import register
from container import Container

class Main(tk.Tk):
    def __init__(self):
        super().__init__()

        # Título
        self.title("_nombre empresa_")

        # Pantalla completa
        self.state("zoomed")  # Windows maximizado

        # Contenedor principal
        container = Frame(self)
        container.configure(bg="#C6D9E3")
        container.pack(fill="both", expand=True)

        self.frames = {}
        for F in (login, register, Container):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Mostrar login al inicio
        self.show_frame(login)

        # Estilo ttk
        self.style = ttk.Style()
        self.style.theme_use("clam")

    def show_frame(self, frame_class):
        self.frames[frame_class].tkraise()


if __name__ == "__main__":
    app = Main()
    app.mainloop()

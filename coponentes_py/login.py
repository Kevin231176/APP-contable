from tkinter import *
import tkinter as tk
import os
from tkinter import ttk, messagebox
from PIL import Image,ImageTk
import sqlite3
from container import Container

class Login(tk.Frame):
    db_name = "database.db"
    
    def __init__(self, padre, controlador):
        super().__init__(padre)
        self.place(x=0,y=0, width=1100, height=650)
        self.controlador = controlador
        self.widgets()

    def validation(self, user, pas):
        return len(user) > 0 and len (pas) > 0

    def login(self):
        user = self.username.get()
        pas = self.password.get()

        if self.validation(user, pas):
            query = "SELECT * FROM usuarios WHERE username = ? AND password = ?"
            parameters = (user,pas)

            try:
                with sqlite3.connect(self.db_name) as conn: 
                    cursor = conn.cursor()
                    cursor.execute(query, parameters)
                    result = cursor.fetchall()

                    if result:
                        self.control1()
                    else:
                        self.username.delete(0, 'end')
                        self.password.delete(0, 'end')
                        messagebox.showerror(title="Error", message="Usuario y/o contraseña incorrecta")

            except sqlite3.Error as e:
                messagebox.showerror(title="Error", message="No se conecto a la base de datos: {}".format(e))

        else:
            messagebox.showerror(title="Error", message="Llene todos los campos")

    def control1(self):
        self.controlador.show_frame(Container)

    def control2(self):
        self.controlador.show_frame(Register)

    def widgets(self):
        fondo = tk.Frame(self,bg= "#ECECEC")
        fondo.place(x=0,y=0, height=650, width=1100)

        self.bg_image = Image.open("coponentes_py/imagenes/8412987.png")  # poner imagen de fondo del logo
        self.bg_image = self.bg_image.resize((1100, 650), Image.Resampling.LANCZOS)
        self.bg_image = ImageTk.PhotoImage(self.bg_image)
        self.bg_label = ttk.Label(fondo, image=self.bg_image)
        self.bg_label.place(x=0, y=0, width=1100, height=650)

        frame1 = tk.Frame(self,bg="#FFFFFF",highlightbackground="black",highlightthickness=1) 
        frame1.place(x=40, y=10, width=400, height=630)
        #frame1.place(x=350, y=10, width=400, height=630)widgets centrado

        user = ttk.Label(frame1, text="Nombre de usuario", font="arial 16 bold", background="#FFFFFF")
        user.place(x=100, y=250)
        self.username = ttk.Entry(frame1, font="arial 16 bold")
        self.username.place(x=80, y=290, width=240, height=40)

        pas = ttk.Label(frame1, text="Contraseña", font="arial 16 bold", background="#FFFFFF")
        pas.place(x=100, y=340)
        self.password = ttk.Entry(frame1,show="*", font="arial 16 bold")
        self.password.place(x=80, y=380, width=240, height=40)

        btn1 = tk.Button(frame1, text="Iniciar", font="arial 16 bold", command=self.login)
        btn1.place(x=80, y=440, width=240, height=40)

        btn2 = tk.Button(frame1, text="Registrar", font="arial 16 bold", command=self.control2)
        btn2.place(x=80, y=500, width=240, height=40)


class Register(tk.Frame):
    db_name = "database.db"
    
    def __init__(self, padre, controlador):
        super().__init__(padre)
        self.place(x=0,y=0, width=1100, height=650)
        self.controlador = controlador
        self.widgets()

    def validation(self, user, pas):
        return len(user) > 0 and len (pas) > 0

    def exec_qry(self,query, parameters=()):
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute(query,parameters)
                conn.commit
        except sqlite3.Error as e:
            messagebox.showerror(title="Error", message="Error al ejecutar la consulta: {}".format(e))

    def register(self):
        user = self.username.get()
        pas = self.password.get()
        key = self.key.get()

        if self.validation(user,pas):
            if len(pas) < 6: 
                messagebox.showinfo(title="Error", message="Contraseña demasiado corta")
                self.username.delete(0,'end')
                self.password.delete(0,'end')
            else:
                if key == "1234":
                    query = "INSERT INTO usuarios VALUES (?,?,?)"
                    parameters = (None, user, pas)
                    self.exec_qry(query,parameters)
                    self.control1()
                else:
                    messagebox.showerror(title="Registro",message="Error al ingresar el codigo de registro")
        else:
            messagebox.showerror(title="Error",message="Llene todos los datos")

    def control1(self):
        self.controlador.show_frame(Container)

    def control2(self):
        self.controlador.show_frame = (Login)

    def widgets(self):
        fondo = tk.Frame(self,bg= "#ECECEC")
        fondo.place(x=0,y=0, height=650, width=1100)

        self.bg_image = Image.open("coponentes_py/imagenes/8412987.png")  # poner imagen de fondo del logo
        self.bg_image = self.bg_image.resize((1100, 650), Image.Resampling.LANCZOS)
        self.bg_image = ImageTk.PhotoImage(self.bg_image)
        self.bg_label = ttk.Label(fondo, image=self.bg_image)
        self.bg_label.place(x=0, y=0, width=1100, height=650)

        frame1 = tk.Frame(self,bg="#FFFFFF",highlightbackground="black",highlightthickness=1) 
        frame1.place(x=40, y=10, width=400, height=630)
        #frame1.place(x=350, y=10, width=400, height=630)

        user = ttk.Label(frame1, text="Nombre de usuario", font="arial 16 bold", background="#FFFFFF")
        user.place(x=100, y=250)
        self.username = ttk.Entry(frame1, font="arial 16 bold")
        self.username.place(x=80, y=290, width=240, height=40)

        pas = ttk.Label(frame1, text="Contraseña", font="arial 16 bold", background="#FFFFFF")
        pas.place(x=100, y=340)
        self.password = ttk.Entry(frame1,show="*", font="arial 16 bold")
        self.password.place(x=80, y=380, width=240, height=40)

        key = ttk.Label(frame1, text="Codigo de registro", font="arial 16 bold", background="#FFFFFF")
        key.place(x=100, y=430)
        self.key = ttk.Entry(frame1,show="*", font="arial 16 bold")
        self.key.place(x=80, y=470, width=240, height=40)

        btn3 = tk.Button(frame1, text="Registrarse", font="arial 16 bold",command=self.register)
        btn3.place(x=80, y=520, width=240, height=40)

        btn4 = tk.Button(frame1, text="Regresar", font="arial 16 bold",command=self.control2)
        btn4.place(x=80, y=570, width=240, height=40)
from tkinter import *
from tkinter import ttk
from login import Login
from login import Register
from container import Container
import sys
import os

class Main(Tk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.title("_nombre empresa_")
        self.geometry("1100x650+120+20")
        self.resizable(False,False)
    
        container= Frame(self)
        container.pack(side=TOP,fill=BOTH,expand=True)
        container.configure(bg="#C6D9E3")

        self.frames = {}
        for f in (Login,Register,Container):
            frame = f(container,self)
            self.frames[f] = frame

        self.show_frame(Container)

        self.style = ttk.Style()
        self.style.theme_use("clam")

    def show_frame(self,container):
        frame = self.frames[container]
        frame.tkraise()

    def main():
        app = Main()
        app.mainloop()

    if __name__ == "__main__":
        main()
        
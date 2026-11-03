#MENU
from tkinter import *
import os

root = Tk()

root.title("Menu")
root.geometry("300x500+480+80")
root.resizable(0, 0)
root.config(bg="#08051A")

def facil():
    os.startfile("juegoFacil.pyw")
    root.destroy()

def medio():
    os.startfile("juegoMedio.pyw")
    root.destroy()

def dificil():
    os.startfile("juegoDificil.pyw")
    root.destroy()



Label(root, text="Elige la dificultad:", font=("Consolas", 20, "bold"), bg="#08051A", fg="#FF9D00").grid(row=0, column=0)

Facil = Button(root, 
               text="Facil", 
               font=("Consolas", 20, "bold"), 
               bg="#FFE7A0", 
               activebackground="#FF9D00", 
               bd=0, 
               cursor="hand2",
               command=facil)
Facil.grid(row=1, column=0, pady=30)

Medio = Button(root, 
               text="Medio", 
               font=("Consolas", 20, "bold"), 
               bg="#FFE7A0", 
               activebackground="#FF9D00", 
               bd=0, 
               cursor="hand2",
               command=medio)
Medio.grid(row=2, column=0, pady=30)

Dificil = Button(root, 
               text="Dificil", 
               font=("Consolas", 20, "bold"), 
               bg="#FFE7A0", 
               activebackground="#FF9D00", 
               bd=0, 
               cursor="hand2",
               command=dificil)
Dificil.grid(row=3, column=0, pady=30)

def easyE(event):
    Facil.config(bg="#FF9D00", fg="white")
def easyS(event):
    Facil.config(bg="#FFE7A0", fg="black")

def MediumE(event):
    Medio.config(bg="#FF9D00", fg="white")
def MediumS(event):
    Medio.config(bg="#FFE7A0", fg="black")

def HardE(event):
    Dificil.config(bg="#FF9D00", fg="white")
def HardS(event):
    Dificil.config(bg="#FFE7A0", fg="black")


Facil.bind("<Enter>", easyE)
Facil.bind("<Leave>", easyS)

Medio.bind("<Enter>", MediumE)
Medio.bind("<Leave>", MediumS)

Dificil.bind("<Enter>", HardE)
Dificil.bind("<Leave>", HardS)

root.mainloop()
#MEDIO
from tkinter import *
import random
import os

root = Tk()

root.title("Juego")
root.geometry("300x500+480+80")
root.resizable(0, 0)
root.config(bg="#08051A")

frame = Frame(root, bg="#17120C", width=300, height=300)
frame.pack(fill="x")

Titulo = Label(frame, 
              text="Adivina el Numero", 
              font=("Arial", 22, "bold"), 
              bg="#17120C", 
              fg="#FF9D00"
            )
Titulo.pack(pady=10)

Texto = Label(frame, 
              text="Elige un numero del 1 al 50", 
              font=("Consolas", 12, "bold"), 
              bg="#17120C", 
              fg="#FF9D00"
            )
Texto.pack(pady=20)

numero_ad = random.randint(1, 50)

numero = Spinbox(frame, 
                 from_=1, 
                 to=50, 
                 bg="#17120C", 
                 font=("Consolas", 20, "bold"),
                 fg="#FF9D00",
                 width=3,
                 buttonbackground="#17120C",
                 buttoncursor="hand2",
                 bd=0)
numero.pack(pady=20)

result = Label(root, text="JUEGA", bg="#08051A", fg="#FF9D00", font=("Consolas", 18, "bold"))
result.place(relx=0.5, rely=0.7, anchor="center")

ayuda = Label(root, bg="#08051A", fg="#FF9D00", font=("Consolas", 18, "bold"))
ayuda.place(relx=0.5, rely=0.9, anchor="center")

corazon = PhotoImage(file="Corazon.png")
corazon = corazon.subsample(35, 35)

corazon_vacio = PhotoImage(file="Vacio.png")
corazon_vacio = corazon_vacio.subsample(12, 12)

corazones = []

for i in range(5):
    corazon_label = Label(root, image=corazon, bg="#08051A", width=30, height=50)
    corazon_label.pack(side="left", anchor="n")
    corazones.append(corazon_label)

vidas = 5
ganar = False

def JugarAgain():
    os.startfile("juegoMedio.pyw")
    root.destroy()

def menu():
    os.startfile("Main.pyw")
    root.destroy()

PlayAgain = Button(root, text="Jugar de nuevo", bg="#08051A", fg="#FF9D00", font=("Consolas", 14, "bold"), command=JugarAgain)
main = Button(root, text="Ir al menu", bg="#08051A", fg="#FF9D00", font=("Consolas", 14, "bold"), command=menu)

def Adivinar():
    global vidas
    global ganar
    try:
        num = int(numero.get())
        if num != numero_ad:
            vidas-=1
            
            corazones[vidas].config(image=corazon_vacio, bg="#08051A", width=30, height=50)
            
            result.config(text="¡PERDISTE!", fg="red")

            print(f"Perdiste, el numero era {numero_ad}")

            if num < numero_ad:
                print("El numero es mayor")
                ayuda.config(text="El numero es mayor")
                
            elif num > numero_ad:
                print("El numero es menor")
                ayuda.config(text="El numero es menor")           

        else:
            ganar = True
            result.config(text="¡GANASTE!", fg="#08FD00")
            ayuda.destroy()
            PlayAgain.config(bd=0, activebackground="#FF9D00")
            PlayAgain.place(relx=0.5, rely=0.8, anchor="e")
            
            main.config(bd=0, activebackground="#FF9D00")
            main.place(relx=0.6, rely=0.8, anchor="w")
            print("Adivinastee")


        if vidas <= 0:
            PlayAgain.config(bd=0, activebackground="#FF9D00")
            PlayAgain.place(relx=0.5, rely=0.8, anchor="e")

            main.config(bd=0, activebackground="#FF9D00")
            main.place(relx=0.6, rely=0.8, anchor="w")
            Label(root, text=f"Ya no tienes vidas", bg="#08051A", fg="#FF9D00", font=("Consolas", 18, "bold")).place(relx=0.5, rely=0.9, anchor="center")
            Label(root, text=f"El numero era {numero_ad}", bg="#08051A", fg="#FF9D00", font=("Consolas", 18, "bold")).place(relx=0.5, rely=0.95, anchor="center")
            
    except ValueError:
        print("No se permite texto")

    if vidas <= 0 or ganar:
        adivinar.config(bg="#7c5500", cursor="", state="disabled")

adivinar = Button(
    frame,
    text="Adivinar",
    bg="#FFE7A0",
    activebackground="#FF9D00",
    relief="flat",
    bd=0,
    cursor="hand2",
    command=Adivinar,
    width=30,
    font=("Consolas", 18, "bold")
)
adivinar.pack(pady=20)

    
def entrarB(event):
    adivinar.config(bg="#FF9D00", fg="white")
    if vidas <= 0 or ganar:
        adivinar.config(bg="#7c5500", cursor="")

def salirB(event):
    adivinar.config(bg="#FFE7A0", fg="black")
    if vidas <= 0 or ganar:
        adivinar.config(bg="#7c5500", cursor="")

def entrarN(event):
    numero.config(bg="#FF9D00", fg="black", buttonbackground="#FF9D00")

def salirN(event):
    numero.config(bg="#17120C", fg="#FF9D00", buttonbackground="#17120C")

def entrarJ(event):
    PlayAgain.config(bg="#FF9D00", fg="black")

def salirJ(event):
    PlayAgain.config(bg="#08051A", fg="#FF9D00")

def entrarM(event):
    main.config(bg="#FF9D00", fg="black")

def salirM(event):
    main.config(bg="#08051A", fg="#FF9D00")
    

adivinar.bind("<Enter>", entrarB)
adivinar.bind("<Leave>", salirB)

numero.bind("<Enter>", entrarN)
numero.bind("<Leave>", salirN)

PlayAgain.bind("<Enter>", entrarJ)
PlayAgain.bind("<Leave>", salirJ)

main.bind("<Enter>", entrarM)
main.bind("<Leave>", salirM)
    
root.mainloop()



# ----------- Imports ----------

import random
from tkinter import *
from tkinter import messagebox, simpledialog


# ----------- CONFIG -------------

resolucion = "1300x700"


rondas = 3 # Numero de rondas

# ------------ CONSTANTES ----------

Player1Puntos = 0
Player2Puntos = 0

InvalidarEleccion = True


opciones = ["piedra","papel","tijera"]


ventana = Tk()
ventana.title("Piedra papel o tijera")
ventana.geometry(resolucion)


# ----------- INPUTS ---------------


Eleccion = Entry(ventana)


# --------------- FUNCIONES SECUNDARIAS ------------------


def ElegirOpcion():

    global InvalidarEleccion

    while True:
            Seleccionado = Eleccion.get().lower()

            if Seleccionado in opciones:
                return Seleccionado

            messagebox.showerror('Opcion no valida!', 'Debes ingresar un valor valido. intentalo otra vez. (Disponibles: "piedra","papel","tijera")')
            InvalidarEleccion = False
            break


def ElegirOpcionMaquina(a):
    return random.choice(a)


def Resultado(Ply,Mqn):

    # EMPATES
     
    if Ply == 'piedra' and Mqn == 'piedra':
        return 'Empate'
    elif Ply == 'papel' and Mqn == 'papel':
        return 'Empate'
    elif Ply == 'tijera' and Mqn == 'tijera':
        return 'Empate'
    
    # Player win

    if Ply == 'piedra' and Mqn == 'tijera':
        return 'Jugador1'
    elif Ply == 'papel' and Mqn == 'piedra':
        return 'Jugador1'
    elif Ply == 'tijera' and Mqn == 'papel':
        return 'Jugador1'
    
    # Maquina win

    if Mqn == 'piedra' and Ply == 'tijera':
        return 'Jugador2'
    elif Mqn == 'papel' and Ply == 'piedra':
        return 'Jugador2'
    elif Mqn == 'tijera' and Ply == 'papel':
        return 'Jugador2'
    

# ------------------- MAIN ---------------------


def main():
    global Player1Puntos, Player2Puntos, InvalidarEleccion

    # Codigo:

    InvalidarEleccion = True

    RondaPly1 = ElegirOpcion()

    if InvalidarEleccion == False:
        return
        
    modificable.config(text="\n\nLa maquina esta eligiendo...\n\n")
    RondaPly2 = ElegirOpcionMaquina(opciones)
    

    ganador = Resultado(RondaPly1,RondaPly2)

    if ganador == 'Jugador1':
        Player1Puntos += 1
        modificable.config(text=f"""Jugador 1 gano.

PUNTOS:
Jugador 1: {Player1Puntos}
Jugador 2: {Player2Puntos}""")
        
    elif ganador == 'Jugador2':
        Player2Puntos += 1
        modificable.config(text=f"""Jugador 2 (Maquina) gano.

PUNTOS:
Jugador 1: {Player1Puntos}
Jugador 2: {Player2Puntos}""")
        

    elif ganador == 'Empate':
        modificable.config(text="Empate!, no se da puntos a nadie")

    if Player1Puntos == rondas:
        modificable.config(text="\n\nEl jugador 1 ha ganado!\n\n")
    if Player2Puntos == rondas:
        modificable.config(text="\n\nEl jugador 2 (maquina) ha ganado el juego!\n\n")

# ------------- LABELS -----------

Texto1 = Label(ventana, text="""Buenas, por favor ingrese una de las siguientes opciones
1. Piedra
2. Papel
3. Tijera
Opcion: """)
modificable = Label(ventana, text='')


# ------------- BOTONES ---------------

Enviar = Button(ventana,text="Enviar",command=main)

# ------------ PACKS --------------

Texto1.pack()
Eleccion.pack()
Enviar.pack()
modificable.pack()

ventana.mainloop()
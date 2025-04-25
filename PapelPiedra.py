# ----------- Imports ----------

import random
from tkinter import *
from tkinter import messagebox, simpledialog


# ----------- CONFIG -------------

resolucion = "1300x700"


Nrondas = 3 # Numero de rondas default

# ------------ CONSTANTES ----------

Player1Puntos = 0
Player2Puntos = 0

InvalidarEleccion = True


opcionesL = ["piedra","papel","tijera"]


ventana = Tk()
ventana.title("Piedra papel o tijera")
ventana.geometry(resolucion)


# ----------- INPUTS ---------------


Eleccion = Entry(ventana)


# --------------- FUNCIONES SECUNDARIAS ------------------


def ElegirOpcion():

    global InvalidarEleccion

    Seleccionado = Eleccion.get().lower()

    if Seleccionado in opcionesL:
        return Seleccionado

    messagebox.showerror('Opcion no valida!', 'Debes ingresar un valor valido. intentalo otra vez. (Disponibles: "piedra","papel","tijera")')
    InvalidarEleccion = False

def actualizar_texto(texto):
    modificable.config(text=texto)

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
    global Player1Puntos, Player2Puntos, InvalidarEleccion, Nrondas


    Nrondas = int(rondas.get())


    # Codigo:

    InvalidarEleccion = True

    RondaPly1 = ElegirOpcion()

    if InvalidarEleccion == False:
        return
        
    actualizar_texto("\n\nLa maquina esta eligiendo...\n\n")
    RondaPly2 = ElegirOpcionMaquina(opcionesL)
    

    ganador = Resultado(RondaPly1,RondaPly2)

    if ganador == 'Jugador1':
        Player1Puntos += 1
        actualizar_texto(f"""Jugador 1 gano.
                           
Maquina: {RondaPly2}

PUNTOS:
Jugador 1: {Player1Puntos}
Jugador 2: {Player2Puntos}""")
        
    elif ganador == 'Jugador2':
        Player2Puntos += 1
        actualizar_texto(f"""Jugador 2 (Maquina) gano.
                           
Maquina: {RondaPly2}

PUNTOS:
Jugador 1: {Player1Puntos}
Jugador 2: {Player2Puntos}""")
        

    elif ganador == 'Empate':
        actualizar_texto("Empate!, no se da puntos a nadie")

    if Player1Puntos >= Nrondas:
        actualizar_texto("\n\nEl jugador 1 ha ganado!\n\n")
        Player1Puntos = 0
        Player2Puntos = 0
    if Player2Puntos >= Nrondas:
        Player1Puntos = 0
        Player2Puntos = 0
        actualizar_texto("\n\nEl jugador 2 (maquina) ha ganado el juego!\n\n")

# ------------- LABELS -----------

Texto1 = Label(ventana, text="""Buenas, por favor ingrese una de las siguientes opciones
1. Piedra
2. Papel
3. Tijera
Opcion: """)
modificable = Label(ventana, text='')
Texto2 = Label(ventana, text='Numero de puntos necesarios para ganar: ')


# ------------- BOTONES ---------------

Enviar = Button(ventana,text="Enviar",command=main)

rondas = StringVar()
opciones = OptionMenu(ventana, rondas, '2','3','4','5','6','7','8','9','10')

# ------------ PACKS --------------

rondas.set('3')

Texto1.pack()
Eleccion.pack()
Enviar.pack()
modificable.pack()
Texto2.pack()
opciones.pack()

ventana.mainloop()
from tkinter import *
import random
import time



##Entorno Grafico

v0 = Tk()
v0.title("Siete y Media")
v0.geometry("400x400")

imagen1=PhotoImage(file="images/fondop.gif")
label1 = Label(v0, image=imagen1)
label1.pack()
imagenb=PhotoImage(file="images/fondob.gif")
imagenj=PhotoImage(file="images/fondoj.gif")


###Variables:
scorejug = 0 #puntuacion de el jugador.
scorebanc = 0 #puntuacion de la banca.
punt = 0
num = 0
puntuacionjug=[]
turno = 1
tamar=0
totalpuntjug = 0.0
totalpuntbanc = 0.0
contar = StringVar()
contar2 = StringVar()
contar3 = StringVar()
contar4 = StringVar()
contar5 = StringVar()
contar6 = StringVar()
var4 = StringVar()
botonP=Button
boton=Button

cartas = ["1O", "2O", "3O", "4O", "5O", "6O", "7O", "SO", "CO", "RO", "1E", "2E",
          "3E", "4E", "5E", "6E", "7E", "SE", "CE", "RE", "1C", "2C", "3C", "4C",
          "5C", "6C", "7C", "SC", "CC", "RC", "1B", "2B", "3B", "4B", "5B", "6B",
          "7B", "SB", "CB", "RB"]
random.shuffle(cartas)




###Metodos
def reinicia_juego():
    global cartas
    global turno
    global totalpuntbanc
    global totalpuntjug
    global scorebanc
    global scorejug
    global tamar

    cartas = ["1O", "2O", "3O", "4O", "5O", "6O", "7O", "SO", "CO", "RO", "1E", "2E",
          "3E", "4E", "5E", "6E", "7E", "SE", "CE", "RE", "1C", "2C", "3C", "4C",
          "5C", "6C", "7C", "SC", "CC", "RC", "1B", "2B", "3B", "4B", "5B", "6B",
          "7B", "SB", "CB", "RB"]
    random.shuffle(cartas)

    turno = 1
    totalpuntjug = 0.0
    totalpuntbanc = 0.0
    scorebanc = 0
    scorejug = 0
    tamar=0
    v0.update()
    ImgCartaJugador.config(file="images/REVERSO.GIF")
    ImgCartaBanca.config(file="images/REVERSO.GIF")
    contar.set(totalpuntbanc)
    contar2.set(totalpuntbanc)
    contar3.set(scorebanc)
    contar4.set(scorejug)

def sacar_carta():

    global cartas
    global puntuacionjug
    global totalpuntjug
    global punt
    global num
    global tamar
    num = len(cartas)
    CartaActual=cartas[tamar]
    CartaActualGIF = "images/" + CartaActual + ".gif"
    puntuacionjug = list(cartas[tamar])
    ImgCartaJugador.config(file=CartaActualGIF)
    punt=puntuacionjug[0]
    comprobar_valor_cartas_jug()
    if tamar < num:
        tamar = tamar+1
    else:
        tamar
    print(tamar)

def sacar_cartas_banca():
    global cartas
    global puntuacionban
    global totalpuntbanc
    global num
    global tamar
    num = len(cartas)-1

    CartaActual = cartas[tamar]
    CartaActualGIF = "images/" + CartaActual + ".gif"

    puntuacionban = list(cartas[tamar])
    ImgCartaBanca.config(file=CartaActualGIF)
    punt=puntuacionban[0]

    if punt == '1' or punt == '2' or punt == '3' or punt == '4' or punt == '5' or punt == '6' or punt == '7':
        totalpuntbanc = float(totalpuntbanc) + float(punt)
        label4 = Label(v0,textvariable=contar2)
        contar2.set(totalpuntbanc)
        print(totalpuntbanc)
    else:
        totalpuntbanc = float(totalpuntbanc)+(0.5)
        label4 = Label(v0,textvariable=contar2)
        contar2.set(totalpuntbanc)
        print(totalpuntbanc)
    if tamar < num:
        tamar = tamar + 1
    else:
        tamar=tamar
    print(tamar)


def plantarse():
    global turno
    turno=2
    juego()



def juego():
    global turno
    global scorebanc
    global scorejug
    global tamar
    if turno == 1:
        botonP.config(state='normal')
        boton.config(state='normal')
        sacar_carta()
    elif turno == 2:
        botonP.config(state='disabled')
        boton.config(state='disabled')
        while totalpuntbanc < 7.5 and totalpuntbanc <= totalpuntjug and tamar < 40:
            v0.update()
            time.sleep(1)
            sacar_cartas_banca()

    comprobacion_ganador()


def comprobar_valor_cartas_jug():
    global punt
    global totalpuntbanc
    global totalpuntjug
    if punt == '1' or punt == '2' or punt == '3' or punt == '4' or punt == '5' or punt == '6' or punt == '7':
        totalpuntjug = float(totalpuntjug) + float(punt)
        label1 = Label(v0,textvariable=contar)
        contar.set(totalpuntjug)
        print(totalpuntjug)
    else:
        totalpuntjug = float(totalpuntjug)+(0.5)
        label1 = Label(v0,textvariable=contar)
        contar.set(totalpuntjug)
        print(totalpuntjug)

def comprobacion_ganador():
    global totalpuntbanc
    global totalpuntjug
    global scorebanc
    global scorejug
    global turno
    global tamar
    if totalpuntjug == 7.5:
        print("gana el jugador")
        scorejug+=1
        contar4.set(scorejug)
        turno = 1
        juego()

        time.sleep(4)
    elif totalpuntjug <= 7.5 and totalpuntbanc > 7.5 and turno == 2:
        print("Gana el jugador")
        turno = 1
        totalpuntjug = 0.0
        totalpuntbanc = 0.0
        v0.update()
        ImgCartaJugador.config(file = "images/REVERSO.GIF")
        ImgCartaBanca.config(file = "images/REVERSO.GIF")
        contar.set(totalpuntbanc)
        contar2.set(totalpuntbanc)
        scorejug+=1
        contar4.set(scorejug)
        juego()
        time.sleep(4)
    elif totalpuntjug < 7.5 and totalpuntbanc > totalpuntjug and turno == 2:
        print("Gana la banca")
        turno = 1
        totalpuntjug = 0.0
        totalpuntbanc = 0.0
        v0.update()
        ImgCartaJugador.config(file="images/REVERSO.GIF")
        ImgCartaBanca.config(file="images/REVERSO.GIF")
        contar.set(totalpuntbanc)
        contar2.set(totalpuntbanc)
        turno = 1
        scorebanc+=1
        contar3.set(scorebanc)
        juego()
        time.sleep(4)
    elif totalpuntjug > 7.5:
        print("Gana la banca")
        turno = 1
        totalpuntjug = 0.0
        totalpuntbanc = 0.0
        v0.update()
        ImgCartaJugador.config(file = "images/REVERSO.GIF")
        ImgCartaBanca.config(file = "images/REVERSO.GIF")
        contar.set(totalpuntbanc)
        contar2.set(totalpuntbanc)
        scorebanc+=1
        contar3.set(scorebanc)
        juego()
        time.sleep(4)
    else:
        print("")

    if turno == 1 and tamar == 40:
        scorejug+=50
        if scorejug > scorebanc:
            ventana_gana_jug()
            reinicia_juego()
        else:
            ventana_gana_ban()
            reinicia_juego()

    elif turno == 2 and tamar == 40:
        scorebanc+=50
        if scorebanc > scorejug:
            ventana_gana_ban()
            reinicia_juego()
        else:
            ventana_gana_jug()
            reinicia_juego()

def ventana_gana_jug():
    global scorejug
    global imagenj
    v1=Toplevel(v0)
    v1.deiconify
    v1.geometry("500x500")
    label1 = Label(v1, image=imagenj)
    label1.pack()

    label8 = Label(v1,textvariable=contar5)
    contar5.set(scorejug)
    label8.place(x=250,y=115)

def ventana_gana_ban():
    global scorebanc
    global imagenb
    v2=Toplevel(v0)
    v2.deiconify
    v2.geometry("500x500")

    label15 = Label(v2, image=imagenb)
    label15.pack()

    label9 = Label(v2,textvariable=contar6)
    contar6.set(scorebanc)
    label9.place(x=250,y=115)



#Cartas del Jugador y Botones
ImgCartaJugador = PhotoImage()
CartaJugador=Label(v0,image=ImgCartaJugador)
CartaJugador.place(x=170,y=300)

CartaJugador.config(width=64, height=100)

ImgCartaJugador.config(file = "images/REVERSO.GIF")

boton=Button(v0, text = "Pedir Carta", command=lambda:juego())
boton.place(x=250,y=300)

botonP=Button(v0,text = "Plantarse",command=lambda:plantarse())
botonP.place(x=250,y=327)

botonR=Button(v0,text = "Reiniciar",command=lambda:reinicia_juego())
botonR.place(x=250,y=354)
#######################################

##Carta de la banca
ImgCartaBanca = PhotoImage()
CartaBanca=Label(v0,image=ImgCartaBanca)
CartaBanca.place(x=170,y=0)
CartaBanca.config(width=64, height=100)
ImgCartaBanca.config(file = "images/REVERSO.GIF")

##labels
#label con la cantidad de puntos de las cartas del jugador
puntuvar=totalpuntjug
label1 = Label(v0,textvariable=contar)
contar.set(totalpuntjug)
label1.place(x=100, y=327)

#label con la cantidad de puntos de las cartas de la banca
label4 = Label(v0,textvariable=contar2)
contar2.set(totalpuntbanc)
label4.place(x=260, y=40)

#Label de la banca
label2 = Label(v0,text="Banca",bg="#771402",fg="White")
label2.place(x=250,y=15)

#Label del nombre del jugador
label3 = Label(v0,text="Jugador",bg="#771402",fg="White")
label3.place(x=86,y=300)

##puntuacion de la partida total de la banca
label5 = Label(v0,textvariable=contar3)
contar3.set(scorebanc)
label5.place(x=265,y=65)

##puntuacion de la partida total del jugador
label6 = Label(v0,textvariable=contar4)
contar4.set(scorejug)
label6.place(x=105,y=350)


v0.mainloop()

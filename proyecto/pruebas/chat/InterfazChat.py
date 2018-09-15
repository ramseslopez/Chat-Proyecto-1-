#librería
from tkinter import *

# declaración de objeto
raiz = Tk()
#Titulo de la ventana
raiz.title("ChatApp")
#dimension de la ventana
raiz.geometry("1100x650")
#dejar que cambie de tamaño
raiz.resizable(0,0)
#fondo
raiz.configure(bg="pink")
#cursor 
raiz.configure(cursor="star")

#salida = Entry(raiz, font=("arial", 20), width=58, bg="white", justify="right").place(x=20,y=60)

miFrame = Frame(raiz, width= 500, height= 500)

miFrame.pack(side="bottom")
#miImagen = PhotoImage(file="Captura de pantalla de 2018-08-10 09-22-07.png")
miFrame.configure(bg="purple")
miFrame.configure(width="1100", height="100")
miFrame.configure(relief="groove")
miFrame.configure(cursor="hand2")

miLabel = Label(raiz, fg="black", font=("Comic Sans MS",18)).place(x="100", y="200")


cuadroTexto=Entry(miFrame)
cuadroTexto.place(x="140", y="10")
nombreLabel=Label(miFrame,text="Escribe tu mensaje:")
nombreLabel.place(x="6",y="10")

cuadroMensaje=Text(miFrame, width=100,height=5)
cuadroMensaje.place(x="140",y="10")

miBoton = Button(miFrame, text="Enviar").place(x="900", y="23")
miBoton2 = Button(miFrame, text="Archivo").place(x="898", y= "57")

raiz.mainloop()


    

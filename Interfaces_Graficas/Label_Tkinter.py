from tkinter import *

raiz = Tk ()

Miframe= Frame(raiz, width=500,height=450)

Miframe.pack()

#Milabel=Label(Miframe,text="primer texto en un frame",fg="orange",font=23)

imagen=PhotoImage(file="Interfaces_Graficas\Label sintaxis.png")

Milabel=Label(Miframe,image= imagen )


#Milabel.place(x=1,y=1) #empaquetado del widget con la especificaciond de la colocacion dado que si lo hacemos con .pack se adapta el pack al texto

Milabel.pack()

#Label(Miframe,text="primer texto en un frame").place(x=140,y=125) es exactamente lo mismo que lo de arriba

Miframe.mainloop()
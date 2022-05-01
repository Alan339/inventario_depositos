from tkinter import *

from tkinter import ttk

raiz=Tk()

raiz.resizable(1,1)

raiz.title("Modificar tablas de otros")


menubar = Menu(raiz)
raiz.config(menu=menubar)

########################## Menú ##########################

def SalirFUN():
	salir = messagebox.askquestion("Salir", "¿Desea salir de la aplicacion?")
	if salir == "yes":
		raiz.destroy()

def sobreque():
	messagebox.showinfo("Acerca de...", "Esta aplicacion fue diseñada por los alumnos de 6to Informatica" )


tablamenu = Menu(menubar, tearoff=0)
tablamenu.add_command(label="Monitores")
tablamenu.add_command(label="Teclados")
tablamenu.add_command(label="Gabinete")
tablamenu.add_command(label="Otros")

modmenu = Menu(menubar, tearoff=0)
modmenu.add_command(label="Ver Datos")
modmenu.add_command(label="Modificar Datos")

herramientasmenu= Menu(menubar, tearoff=0)
herramientasmenu.add_command(label="Guardar")
herramientasmenu.add_command(label="Acerca de...", command=sobreque)
herramientasmenu.add_separator()
herramientasmenu.add_command(label="Salir", command=SalirFUN)

menubar.add_cascade(label="Tablas", menu=tablamenu)
menubar.add_cascade(label="Modo", menu=modmenu)
menubar.add_cascade(label="Herramientas", menu=herramientasmenu)




miFrame=Frame(raiz, width=1000, height=500)
miFrame.pack()


Label(miFrame, text="TABLAS DE OTROS", fg="black", font=("Comic Sans MS", 18)).grid(row=0, column=1, columnspan=3)



miImagen=PhotoImage(file="i.png")
Label(miFrame, image=miImagen).grid(row=1, column=2)

cuadroID=Entry(miFrame)
cuadroID.grid(row=3, column=1, padx=10, pady=10)
cuadroID.config(justify="center")

cuadroDeposito=Entry(miFrame)
cuadroDeposito.grid(row=3, column=2, padx=10, pady=10)
cuadroDeposito.config(justify="center")

cuadroMonitor=Entry(miFrame)
cuadroMonitor.grid(row=3, column=3, padx=10, pady=10)
cuadroMonitor.config(justify="center")


#-------------------------------------------


IDLabel=Label(miFrame, text="ID:")
IDLabel.grid(row=2, column=1, padx=5)

DepositoLabel=Label(miFrame, text="Deposito:")
DepositoLabel.grid(row=2, column=2, padx=5)

MonitorLabel=Label(miFrame, text="Cantidad:")
MonitorLabel.grid(row=2, column=3, padx=5)






miFrame2=Frame(raiz, width=500, height=300)
miFrame2.pack()

miFrame2.config(bd=5)



def codigoBoton():

	pass

botonEnvio=Button(miFrame2, text="Guardar", command=codigoBoton, width=10, height=2)
botonEnvio.grid(row=2,column=1, pady=10, padx=20)


botonEnvio=Button(miFrame2, text="Cancelar", command=codigoBoton, width=10, height=2)
botonEnvio.grid(row=2,column=2,pady=10, padx=20)

miFrame3=Frame(raiz, width=30, height=30)
miFrame3.pack()

scroll = Scrollbar(miFrame3)
scroll.pack(side=RIGHT,fill=Y)

tabla=ttk.Treeview(miFrame3,yscrollcommand=scroll.set,height=5,show="headings",columns=('#1','#2','#3'))
tabla.pack(pady=10,padx=10)
tabla.column('#1',width=40)
tabla.heading('#1',text="ID",anchor=CENTER)
tabla.column('#2',width=200)
tabla.heading('#2',text="Dispositivo",anchor=CENTER)
tabla.column('#3',width=100)
tabla.heading('#3',text="Cantidad",anchor=CENTER)

scroll.config(command=tabla.yview)

footer=Frame(raiz)
footer.pack()

imagenF=PhotoImage(file="f1.png")
Label(footer,image=imagenF).pack()


raiz.mainloop()
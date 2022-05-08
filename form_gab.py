from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector as database
import inicio
import mon
import tec
import gab
import otros

def gabinetes():

	root=Tk()

	root.resizable(0,0)


	root.title("Modificar tablas de gabinetes")

	conexion= database.connect(
			host="localhost",
			user="root",
			password="",
			database="inventario")

	cursor = conexion.cursor()

	menubar = Menu(root)
	root.config(menu=menubar)

	########################## Menú ##########################

	def SalirFUN():
		salir = messagebox.askquestion("Salir", "¿Desea salir de la aplicacion?")
		if salir == "yes":
			root.destroy()

	def sobreque():
		messagebox.showinfo("Acerca de...", "Esta aplicacion fue diseñada por los alumnos de 6to Informatica" )

	def menu1():

		root.destroy()

		mon.monitores()

	def menu2():

		root.destroy()

		tec.teclados()

	def menu4():

		root.destroy()

		otros.otrosv()

	def cambiar_modo():

		root.destroy()

		gab.gabinetes()

	def ir_inicio():

		root.destroy()

		inicio.ventana_1()

	tablamenu = Menu(menubar, tearoff=0)
	tablamenu.add_command(label="Inicio",command=ir_inicio)
	tablamenu.add_separator()
	tablamenu.add_command(label="Monitores",command=menu1)
	tablamenu.add_command(label="Teclados",command=menu2)
	tablamenu.add_command(label="Gabinete",state="disabled")
	tablamenu.add_command(label="Otros",command=menu4)

	modmenu = Menu(menubar, tearoff=0)
	modmenu.add_command(label="Ver Datos",command=cambiar_modo)
	modmenu.add_command(label="Modificar Datos",state="disabled")

	herramientasmenu= Menu(menubar, tearoff=0)
	herramientasmenu.add_command(label="Acerca de...", command=sobreque)
	herramientasmenu.add_separator()
	herramientasmenu.add_command(label="Salir", command=SalirFUN)

	menubar.add_cascade(label="Secciones", menu=tablamenu)
	menubar.add_cascade(label="Modo", menu=modmenu)
	menubar.add_cascade(label="Otros", menu=herramientasmenu)

	miFrame=Frame(root, width=1000, height=500)
	miFrame.pack()

	def llenar_tabla():

		vaciar_tabla()

		instruccion="SELECT * FROM gabinetes"

		cursor.execute(instruccion)

		filas=cursor.fetchall()

		for fila in filas:

			registro=fila[0]

			tabla.insert("",END,registro,text='re',values=fila)

	def vaciar_tabla():

		filas=tabla.get_children()

		for fila in filas:
			tabla.delete(fila)

	def seleccionar(event):

		registro=tabla.selection()[0]

		if int(registro)>0:

			ide.set(tabla.item(registro, "values")[0])
			deposito.set(tabla.item(registro, "values")[1])
			gabinete.set(tabla.item(registro, "values")[2])
			marca.set(tabla.item(registro, "values")[3])
			so.set(tabla.item(registro, "values")[4])
			check.set(tabla.item(registro, "values")[5])
			observaciones.set(tabla.item(registro, "values")[6])
			componentes_faltantes.set(tabla.item(registro, "values")[7])

	Label(miFrame, text="TABLAS DE GABINETES", fg="black", font=("Comic Sans MS", 18)).grid(row=0, column=1, columnspan=3)

	miImagen=PhotoImage(file="i.png")
	Label(miFrame, image=miImagen).grid(row=1, column=2)

	ide=IntVar()
	deposito=IntVar()
	gabinete=IntVar()
	marca=StringVar()
	so=StringVar()
	check=IntVar()
	observaciones=StringVar()
	componentes_faltantes=StringVar()

	cuadroID=Entry(miFrame,textvariable=ide,state="disabled")
	cuadroID.grid(row=3, column=1, padx=10)
	cuadroID.config(justify="center")

	cuadroDeposito=Entry(miFrame,textvariable=deposito,state="disabled")
	cuadroDeposito.grid(row=3, column=2, padx=10)
	cuadroDeposito.config(justify="center")

	cuadroGabinete=Entry(miFrame,textvariable=gabinete,state="disabled")
	cuadroGabinete.grid(row=3, column=3, padx=10)
	cuadroGabinete.config(justify="center")

	cuadroMarca=Entry(miFrame,textvariable=marca)
	cuadroMarca.grid(row=5, column=1, columnspan=2, padx=10, pady=10)
	cuadroMarca.config(justify="center")

	cuadroSO=Entry(miFrame,textvariable=so)
	cuadroSO.grid(row=5, column=2, columnspan=3, padx=10, pady=5)
	cuadroSO.config(justify="center")

	cuadroCheck=Checkbutton(miFrame,variable=check,onvalue=1,offvalue=0)
	cuadroCheck.grid(row=7, column=2, pady=5)
	cuadroCheck.config(justify="center")

	cuadroObservaciones=Entry(miFrame,textvariable=observaciones,width=70)
	cuadroObservaciones.grid(row=9, column=1, pady=10,columnspan=3)
	cuadroObservaciones.config(justify="center")

	cuadroComponentes=Entry(miFrame,textvariable=componentes_faltantes,width=70)
	cuadroComponentes.grid(row=11, column=1, pady=10,columnspan=3)
	cuadroComponentes.config(justify="center")


	#-------------------------------------------


	IDLabel=Label(miFrame, text="ID:")
	IDLabel.grid(row=2, column=1, padx=10, pady=10)

	DepositoLabel=Label(miFrame, text="Deposito:")
	DepositoLabel.grid(row=2, column=2, padx=10, pady=5)

	MonitorLabel=Label(miFrame, text="Gabinete:")
	MonitorLabel.grid(row=2, column=3, padx=10, pady=5)

	MarcaLabel=Label(miFrame, text="Marca:")
	MarcaLabel.grid(row=4, column=1, columnspan=2)

	ModeloLabel=Label(miFrame, text="S.O:")
	ModeloLabel.grid(row=4, column=2, columnspan=3)

	FuncionaLabel=Label(miFrame, text="¿Funciona?")
	FuncionaLabel.grid(row=6, column=2)

	ObservacionesLabel=Label(miFrame, text="Observaciones:")
	ObservacionesLabel.grid(row=8, column=2)

	RecomendacionesLabel=Label(miFrame, text="Componentes faltantes:")
	RecomendacionesLabel.grid(row=10, column=2)


	#----------------------------------------------


	miFrame2=Frame(root, width=500, height=300)
	miFrame2.pack()

	miFrame2.config(bd=5)



	def boton1():

		registro=tabla.selection()[0]

		val=(marca.get(),so.get(),check.get(),observaciones.get(),componentes_faltantes.get())

		instruccion="UPDATE gabinetes SET MARCA=%s, SO=%s, FUNCIONA=%s, OBSERVACIONES=%s, COMPONENTES_FALTANTES=%s WHERE ID="+registro

		cursor.execute(instruccion,val)

		conexion.commit()

		messagebox.showinfo("Registro actualizado","Registro actualizado exitosamente")

		llenar_tabla()

		boton2()

	def boton2():

		ide.set(0)
		deposito.set(0)
		gabinete.set(0)
		marca.set("")
		so.set("")
		check.set(0)
		observaciones.set("")
		componentes_faltantes.set("")

	def boton3():

		root.destroy()

		gab.gabinetes()

	botonGuardar=Button(miFrame2, text="Guardar", command=boton1, width=10, height=2)
	botonGuardar.grid(row=2,column=1, pady=10, padx=20)


	botonCancelar=Button(miFrame2, text="Cancelar", command=boton2, width=10, height=2)
	botonCancelar.grid(row=2,column=2,pady=10, padx=20)

	botonVer=Button(miFrame2, text="Ver", command=boton3, width=10, height=2)
	botonVer.grid(row=2,column=3,pady=10, padx=20)


	miFrame3=Frame(root, width=30, height=30)
	miFrame3.pack()

	scroll = Scrollbar(miFrame3)
	scroll.pack(side=RIGHT,fill=Y)

	tabla=ttk.Treeview(miFrame3,yscrollcommand=scroll.set,height=5,show="headings",columns=('#1','#2','#3','#4','#5','#6','#7','#8'))
	tabla.pack(pady=10,padx=10)
	tabla.column('#1',width=40)
	tabla.heading('#1',text="ID",anchor=CENTER)
	tabla.column('#2',width=60)
	tabla.heading('#2',text="Deposito",anchor=CENTER)
	tabla.column('#3',width=60)
	tabla.heading('#3',text="Gabinete",anchor=CENTER)
	tabla.column('#4',width=80)
	tabla.heading('#4',text="Marca",anchor=CENTER)
	tabla.column('#5',width=80)
	tabla.heading('#5',text="S.O",anchor=CENTER)
	tabla.column('#6',width=60)
	tabla.heading('#6',text="Funciona",anchor=CENTER)
	tabla.column('#7',width=200)
	tabla.heading('#7',text="Observaciones",anchor=CENTER)
	tabla.column('#8',width=200)
	tabla.heading('#8',text="Componentes faltantes",anchor=CENTER)
	tabla.bind("<<TreeviewSelect>>",seleccionar)

	scroll.config(command=tabla.yview)



	footer=Frame(root)
	footer.pack()

	imagenF=PhotoImage(file="f1.png")
	Label(footer,image=imagenF).pack()

	llenar_tabla()

	root.mainloop()
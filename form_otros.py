from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector as database
import inicio
import mon
import tec
import gab
import otros

def otrosf():

	root=Tk()

	root.resizable(0,0)

	root.title("Modificar tablas de otros")

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

	def menu3():

		root.destroy()

		gab.gabinetes()

	def cambiar_modo():

		root.destroy()

		otros.otrosv()

	def ir_inicio():

		root.destroy()

		inicio.ventana_1()

	tablamenu = Menu(menubar, tearoff=0)
	tablamenu.add_command(label="Inicio",command=ir_inicio)
	tablamenu.add_separator()
	tablamenu.add_command(label="Monitores",command=menu1)
	tablamenu.add_command(label="Teclados",command=menu2)
	tablamenu.add_command(label="Gabinete",command=menu3)
	tablamenu.add_command(label="Otros",state="disabled")

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

		instruccion="SELECT * FROM otros"

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
			dispositivo.set(tabla.item(registro, "values")[1])
			cantidad.set(tabla.item(registro, "values")[2])

	Label(miFrame, text="TABLAS DE OTROS", fg="black", font=("Comic Sans MS", 18)).grid(row=0, column=1, columnspan=3)

	ide=IntVar()
	dispositivo=StringVar()
	cantidad=IntVar()

	miImagen=PhotoImage(file="i.png")
	Label(miFrame, image=miImagen).grid(row=1, column=2)

	cuadroID=Entry(miFrame,textvariable=ide,state="disabled")
	cuadroID.grid(row=3, column=1, padx=10, pady=10)
	cuadroID.config(justify="center")

	cuadroDispositivo=Entry(miFrame,textvariable=dispositivo)
	cuadroDispositivo.grid(row=3, column=2, padx=10, pady=10)
	cuadroDispositivo.config(justify="center")

	cuadroCantidad=Entry(miFrame,textvariable=cantidad)
	cuadroCantidad.grid(row=3, column=3, padx=10, pady=10)
	cuadroCantidad.config(justify="center")


	#-------------------------------------------


	IDLabel=Label(miFrame, text="ID:")
	IDLabel.grid(row=2, column=1, padx=5)

	DepositoLabel=Label(miFrame, text="Deposito:")
	DepositoLabel.grid(row=2, column=2, padx=5)

	MonitorLabel=Label(miFrame, text="Cantidad:")
	MonitorLabel.grid(row=2, column=3, padx=5)


	miFrame2=Frame(root, width=500, height=300)
	miFrame2.pack()

	miFrame2.config(bd=5)

	def boton1():

		registro=tabla.selection()[0]

		val=(dispositivo.get(),cantidad.get())

		instruccion="UPDATE otros SET DISPOSITIVO=%s, CANTIDAD=%s WHERE ID="+registro

		cursor.execute(instruccion,val)

		conexion.commit()

		messagebox.showinfo("Registro actualizado","Registro actualizado exitosamente")

		llenar_tabla()

		boton2()

	def boton2():

		ide.set(0)
		dispositivo.set("")
		cantidad.set(0)

	def boton3():

			root.destroy()

			otros.otrosv()

	botonEnvio=Button(miFrame2, text="Guardar", command=boton1, width=10, height=2)
	botonEnvio.grid(row=2,column=1, pady=10, padx=20)

	botonEnvio=Button(miFrame2, text="Cancelar", command=boton2, width=10, height=2)
	botonEnvio.grid(row=2,column=2,pady=10, padx=20)

	botonVer=Button(miFrame2, text="Ver", command=boton3, width=10, height=2)
	botonVer.grid(row=2,column=3,pady=10, padx=20)

	miFrame3=Frame(root, width=30, height=30)
	miFrame3.pack()

	scroll = Scrollbar(miFrame3)
	scroll.pack(side=RIGHT,fill=Y)

	tabla=ttk.Treeview(miFrame3,yscrollcommand=scroll.set,height=5,show="headings",columns=('#1','#2','#3'))
	tabla.pack(pady=10,padx=10)
	tabla.column('#1',width=40)
	tabla.heading('#1',text="ID",anchor=CENTER)
	tabla.column('#2',width=180)
	tabla.heading('#2',text="Dispositivo",anchor=CENTER)
	tabla.column('#3',width=80)
	tabla.heading('#3',text="Cantidad",anchor=CENTER)
	tabla.bind("<<TreeviewSelect>>",seleccionar)

	scroll.config(command=tabla.yview)

	footer=Frame(root)
	footer.pack()

	imagenF=PhotoImage(file="f1.png")
	Label(footer,image=imagenF).pack()

	llenar_tabla()

	root.mainloop()
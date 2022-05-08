from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector as database
import form_tec
import inicio
import mon
import gab
import otros

def teclados():

	root=Tk()

	root.resizable(0,0)

	root.title("Modificar tablas de teclados")

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

	def menu3():

		root.destroy()

		gab.gabinetes()

	def menu4():

		root.destroy()

		otros.otrosv()

	def cambiar_modo():

		root.destroy()

		form_tec.teclados()

	def ir_inicio():

		root.destroy()

		inicio.ventana_1()

	tablamenu = Menu(menubar, tearoff=0)
	tablamenu.add_command(label="Inicio",command=ir_inicio)
	tablamenu.add_separator()
	tablamenu.add_command(label="Monitores",command=menu1)
	tablamenu.add_command(label="Teclados",state="disabled")
	tablamenu.add_command(label="Gabinete",command=menu3)
	tablamenu.add_command(label="Otros",command=menu4)

	modmenu = Menu(menubar, tearoff=0)
	modmenu.add_command(label="Ver Datos",state="disabled")
	modmenu.add_command(label="Modificar Datos",command=cambiar_modo)

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

		instruccion="SELECT * FROM teclados"

		cursor.execute(instruccion)

		filas=cursor.fetchall()

		for fila in filas:

			registro=fila[0]

			tabla.insert("",END,registro,text='re',values=fila)

	def boton1():

		root.destroy()

		form_tec.teclados()

	def boton2():

		root.destroy()

		inicio.ventana_1()

	Label(miFrame, text="TABLAS DE TECLADOS", fg="black", font=("Comic Sans MS", 18)).grid(row=0, column=1, columnspan=3)

	miImagen=PhotoImage(file="i.png")
	Label(miFrame, image=miImagen).grid(row=1, column=2)

	miFrame2=Frame(root, width=500, height=300)
	miFrame2.pack()

	botonVer=Button(miFrame2, text="Modificar", command=boton1, width=10, height=2)
	botonVer.grid(row=2,column=2,pady=10, padx=20)

	volver=Button(miFrame2,text="Volver",padx=5,pady=5,command=boton2,width=10).grid(row=2,column=1,padx=5,pady=2)


	miFrame3=Frame(root, width=30, height=30)
	miFrame3.pack()

	scroll = Scrollbar(miFrame3)
	scroll.pack(side=RIGHT,fill=Y)

	tabla=ttk.Treeview(miFrame3,yscrollcommand=scroll.set,height=5,show="headings",columns=('#1','#2','#3','#4','#5','#6','#7','#8','#9'),selectmode="none")
	tabla.pack(pady=10,padx=10)
	tabla.column('#1',width=40)
	tabla.heading('#1',text="ID",anchor=CENTER)
	tabla.column('#2',width=60)
	tabla.heading('#2',text="Deposito",anchor=CENTER)
	tabla.column('#3',width=60)
	tabla.heading('#3',text="Teclado",anchor=CENTER)
	tabla.column('#4',width=80)
	tabla.heading('#4',text="Marca",anchor=CENTER)
	tabla.column('#5',width=80)
	tabla.heading('#5',text="Modelo",anchor=CENTER)
	tabla.column('#6',width=80)
	tabla.heading('#6',text="Tipo de ficha",anchor=CENTER)
	tabla.column('#7',width=60)
	tabla.heading('#7',text="Funciona",anchor=CENTER)
	tabla.column('#8',width=200)
	tabla.heading('#8',text="Observaciones",anchor=CENTER)
	tabla.column('#9',width=200)
	tabla.heading('#9',text="Recomendaciones",anchor=CENTER)

	scroll.config(command=tabla.yview)



	footer=Frame(root)
	footer.pack()

	imagenF=PhotoImage(file="f1.png")
	Label(footer,image=imagenF).pack()

	llenar_tabla()

	root.mainloop()
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector as database
import inicio_user
import mon_user
import tec_user
import gab_user

def otrosv():

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

		mon_user.monitores()

	def menu2():

		root.destroy()

		tec_user.teclados()

	def menu3():

		root.destroy()

		gab_user.gabinetes()

	def ir_inicio():

		root.destroy()

		inicio_user.ventana_1()

	tablamenu = Menu(menubar, tearoff=0)
	tablamenu.add_command(label="Inicio",command=ir_inicio)
	tablamenu.add_separator()
	tablamenu.add_command(label="Monitores",command=menu1)
	tablamenu.add_command(label="Teclados",command=menu2)
	tablamenu.add_command(label="Gabinete",command=menu3)
	tablamenu.add_command(label="Otros",state="disabled")

	herramientasmenu= Menu(menubar, tearoff=0)
	herramientasmenu.add_command(label="Acerca de...", command=sobreque)
	herramientasmenu.add_separator()
	herramientasmenu.add_command(label="Salir", command=SalirFUN)

	menubar.add_cascade(label="Secciones", menu=tablamenu)
	menubar.add_cascade(label="Otros", menu=herramientasmenu)

	miFrame=Frame(root, width=1000, height=500)
	miFrame.pack()


	Label(miFrame, text="TABLAS DE OTROS", fg="black", font=("Comic Sans MS", 18)).grid(row=0, column=1, columnspan=3)

	miImagen=PhotoImage(file="i.png")
	Label(miFrame, image=miImagen).grid(row=1, column=2)

	miFrame2=Frame(root, width=500, height=300)
	miFrame2.pack()

	def llenar_tabla():

		instruccion="SELECT * FROM otros"

		cursor.execute(instruccion)

		filas=cursor.fetchall()

		for fila in filas:

			registro=fila[0]

			tabla.insert("",END,registro,text='re',values=fila)

	def boton2():

		root.destroy()

		inicio_user.ventana_1()

	botonEnvio=Button(miFrame2, text="Volver", command=boton2, width=10, height=2)
	botonEnvio.grid(row=2,column=1,pady=10, padx=20)

	miFrame3=Frame(root, width=30, height=30)
	miFrame3.pack()

	scroll = Scrollbar(miFrame3)
	scroll.pack(side=RIGHT,fill=Y)

	tabla=ttk.Treeview(miFrame3,yscrollcommand=scroll.set,height=5,show="headings",columns=('#1','#2','#3'),selectmode="none")
	tabla.pack(pady=10,padx=10)
	tabla.column('#1',width=40)
	tabla.heading('#1',text="ID",anchor=CENTER)
	tabla.column('#2',width=180)
	tabla.heading('#2',text="Dispositivo",anchor=CENTER)
	tabla.column('#3',width=80)
	tabla.heading('#3',text="Cantidad",anchor=CENTER)

	scroll.config(command=tabla.yview)

	footer=Frame(root)
	footer.pack()

	imagenF=PhotoImage(file="f1.png")
	Label(footer,image=imagenF).pack()

	llenar_tabla()

	root.mainloop()
from tkinter import *
from tkinter import messagebox
import mysql.connector as database
from tkinter import ttk
import inicio_alumnos
import primero_admin_m

def v_primero():

	root=Tk()
	root.title("Primero")
	root.resizable(False,False)

	conexion= database.connect(
		host="localhost",
		user="root",
		password="",
		database="alumnos")

	cursor = conexion.cursor()

	########################## Estructura ventana ##########################

	frame=Frame(root)
	frame.pack()

	def llenar_tabla():

		instruccion="SELECT * FROM primero"

		cursor.execute(instruccion)

		filas=cursor.fetchall()

		for fila in filas:

			registro=fila[0]

			tabla.insert("",END,registro,text='re',values=fila)

	Label(frame, text="ADMINISTRACIÓN DE ALUMNOS",font=("Calibri",20,"bold")).grid(row=0,column=0,padx=5,pady=2)
	Label(frame, text="Primero",font=("Calibri",12,"bold")).grid(row=1,column=0,padx=5,pady=2)

	imagen=PhotoImage(file="i.png")
	Label(frame,image=imagen,anchor=CENTER).grid(row=0,column=1,padx=5,pady=5,rowspan=2)

	fr=Frame(root)
	fr.pack()

	def boton():

		root.destroy()

		inicio_alumnos.ventana_1()

	def boton2():

		root.destroy()

		primero_admin_m.v_primero()
		

	volver=Button(fr,text="Volver",padx=5,pady=5,command=boton,width=10).grid(row=3,column=0,padx=5,pady=2)
	modificar=Button(fr,text="Modificar",padx=5,pady=5,command=boton2,width=10).grid(row=3,column=1,padx=5,pady=2)

	frame2=LabelFrame(root,text="Curso de primero:")
	frame2.pack()

	scroll = Scrollbar(frame2)
	scroll.pack(side=RIGHT,fill=Y)

	tabla=ttk.Treeview(frame2,yscrollcommand=scroll.set,height=10,show="headings",columns=('#1','#2','#3','#4','#5','#6'),selectmode="none")
	tabla.pack(pady=10,padx=10)
	tabla.column('#1',width=50)
	tabla.heading('#1',text="ID",anchor=CENTER)
	tabla.column('#2',width=160)
	tabla.heading('#2',text="Nombre",anchor=CENTER)
	tabla.column('#3',width=160)
	tabla.heading('#3',text="Apellido",anchor=CENTER)
	tabla.column('#4',width=80)
	tabla.heading('#4',text="DNI",anchor=CENTER)
	tabla.column('#5',width=80)
	tabla.heading('#5',text="Fecha Ingreso",anchor=CENTER)
	tabla.column('#6',width=350)
	tabla.heading('#6',text="Observaciones",anchor=CENTER)

	scroll.config(command=tabla.yview)

	llenar_tabla()

	root.mainloop()
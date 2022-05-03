from tkinter import *
from tkinter import messagebox
import mysql.connector as database
from tkinter import ttk
import inicio_alumnos
import primero_admin

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

		vaciar_tabla()

		instruccion="SELECT * FROM primero"

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
			nombres.set(tabla.item(registro, "values")[1])
			apellidos.set(tabla.item(registro, "values")[2])
			dni.set(tabla.item(registro, "values")[3])
			fecha_ingreso.set(tabla.item(registro, "values")[4])
			observacion.set(tabla.item(registro, "values")[5])


	Label(frame, text="ADMINISTRACIÓN DE ALUMNOS",font=("Calibri",20,"bold")).grid(row=0,column=0,padx=5,pady=2)
	Label(frame, text="Primero",font=("Calibri",12,"bold")).grid(row=1,column=0,padx=5,pady=2)

	imagen=PhotoImage(file="i.png")
	Label(frame,image=imagen,anchor=CENTER).grid(row=0,column=1,padx=5,pady=5,rowspan=2)

	miFrame=Frame(root, width=1000, height=500)
	miFrame.pack()

	ide=IntVar()
	nombres=StringVar()
	apellidos=StringVar()
	dni=IntVar()
	fecha_ingreso=StringVar()
	observacion=StringVar()

	cuadroID=Entry(miFrame,state="disabled",width=10,textvariable=ide)
	cuadroID.grid(row=1, column=0, padx=10, pady=10)
	cuadroID.config(justify="center")

	cuadroNombre=Entry(miFrame,width=20,textvariable=nombres)
	cuadroNombre.grid(row=1, column=1, padx=10, pady=10)
	cuadroNombre.config(justify="center")

	cuadroApellido=Entry(miFrame,width=20,textvariable=apellidos)
	cuadroApellido.grid(row=1, column=2, padx=10, pady=10)
	cuadroApellido.config(justify="center")

	cuadroDNI=Entry(miFrame,textvariable=dni)
	cuadroDNI.grid(row=3, column=0, columnspan=1, padx=10, pady=10)
	cuadroDNI.config(justify="center")

	cuadroFechaDeIngreso=Entry(miFrame,textvariable=fecha_ingreso)
	cuadroFechaDeIngreso.grid(row=3, column=1, columnspan=1, padx=10, pady=10)
	cuadroFechaDeIngreso.config(justify="center")

	cuadroObservaciones=Entry(miFrame,textvariable=observacion)
	cuadroObservaciones.grid(row=3, column=2, pady=10)
	cuadroObservaciones.config(justify="center")


	IDLabel=Label(miFrame, text="ID:")
	IDLabel.grid(row=0, column=0, padx=10, pady=10)

	DepositoLabel=Label(miFrame, text="Nombre:")
	DepositoLabel.grid(row=0, column=1, padx=10, pady=5)

	MonitorLabel=Label(miFrame, text="Apellido:")
	MonitorLabel.grid(row=0, column=2, padx=10, pady=5)

	MarcaLabel=Label(miFrame, text="DNI:")
	MarcaLabel.grid(row=2, column=0, columnspan=1)

	ModeloLabel=Label(miFrame, text="Fecha de Ingreso:")
	ModeloLabel.grid(row=2, column=1, columnspan=1)

	ObservacionesLabel=Label(miFrame, text="Observaciones:")
	ObservacionesLabel.grid(row=2, column=2)

	fr=Frame(root)
	fr.pack()

	def boton():

		root.destroy()

		inicio_alumnos.ventana_1()

	def boton2():

		root.destroy()

		primero_admin.v_primero()

	def boton3():

		registro=tabla.selection()[0]

		val=(nombres.get(),apellidos.get(),dni.get(),fecha_ingreso.get(),observacion.get())

		instruccion="UPDATE primero SET NOMBRES=%s, APELLIDOS=%s, DNI=%s, FECHA_INGRESO=%s, OBSERVACION=%s WHERE ID="+registro

		cursor.execute(instruccion,val)

		conexion.commit()

		messagebox.showinfo("Registro actualizado","Registro actualizado exitosamente")

		llenar_tabla()

		ide.set(0)
		nombres.set("")
		apellidos.set("")
		dni.set(0)
		fecha_ingreso.set("")
		observacion.set("")
		

	volver=Button(fr,text="Volver",padx=5,pady=5,command=boton,width=10).grid(row=3,column=0,padx=5,pady=2)
	ver=Button(fr,text="Ver",padx=5,pady=5,command=boton2,width=10).grid(row=3,column=1,padx=5,pady=2)
	guardar=Button(fr,text="Guardar",padx=5,pady=5,command=boton3,width=10).grid(row=3,column=2,padx=5,pady=2)

	frame2=LabelFrame(root,text="Curso de primero:")
	frame2.pack()

	scroll = Scrollbar(frame2)
	scroll.pack(side=RIGHT,fill=Y)

	tabla=ttk.Treeview(frame2,yscrollcommand=scroll.set,height=10,show="headings",columns=('#1','#2','#3','#4','#5','#6'))
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
	tabla.bind("<<TreeviewSelect>>",seleccionar)

	scroll.config(command=tabla.yview)

	llenar_tabla()

	root.mainloop()
from tkinter import *
from tkinter import messagebox
import mysql.connector as database
from werkzeug.security import generate_password_hash, check_password_hash

root = Tk()
root.title("Login")

conexion= database.connect(
	host="localhost",
	user="root",
	password="",
	database="alumnos")

cursor = conexion.cursor()

frame=LabelFrame(root,text="Creación de usuarios:")
frame.pack()

titulo=Label(frame,text="Ingrese la información del nuevo usuario")
titulo.config(font=("Calibri",14))
titulo.grid(row=0,column=0,sticky="nsew",pady=5,padx=5,columnspan=2)

label1=Label(frame,text="Usuario:").grid(row=1,column=0,sticky="w",pady=5,padx=5)
label2=Label(frame,text="Contraseña:").grid(row=2,column=0,sticky="w",pady=5,padx=5)

usuario=StringVar()
contrasena=StringVar()
opcion=IntVar()
opcion.set(value=2)

Entrada1=Entry(frame,textvariable=usuario).grid(row=1,column=1,sticky="e",pady=5,padx=5)
Entrada2=Entry(frame,textvariable=contrasena,show="*").grid(row=2,column=1,sticky="e",pady=5,padx=5)
Radiobutton(frame,text="Admin",variable=opcion,value=1).grid(row=3,column=0,sticky="nsew",pady=5,padx=5)
Radiobutton(frame,text="Usuario",variable=opcion,value=2).grid(row=3,column=1,sticky="nsew",pady=5,padx=5)

def click_boton():

	p_encriptada=StringVar()

	p_encriptada.set(generate_password_hash(contrasena.get()))

	tipoUsuario=StringVar()

	if opcion.get()==2:

		tipoUsuario.set("USER")

	else:

		tipoUsuario.set("ADMIN")

	val=(usuario.get(),p_encriptada.get(),tipoUsuario.get())
	
	instruccion="INSERT INTO usuarios (USUARIO,CONTRASENA,TIPO_USUARIO) values (%s,%s,%s)"

	cursor.execute(instruccion,val)

	conexion.commit()

	messagebox.showinfo("Usuario creado","Usuario creado exitosamente")

	usuario.set("")
	contrasena.set("")
	opcion.set(value=2)

botonEnviar = Button(frame,text="Enviar",padx=5,pady=5,command=click_boton).grid(row=4,column=0,columnspan=2)

root.mainloop()
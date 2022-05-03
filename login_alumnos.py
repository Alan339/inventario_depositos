from tkinter import *
from tkinter import messagebox
import mysql.connector as database
from inicio_alumnos import *
from primero import *
from segundo import *
from tercero import *
from cuarto import *
from quinto import *
from sexto import *
from werkzeug.security import generate_password_hash, check_password_hash
from tkinter import messagebox

root = Tk()
root.title("Login")

conexion= database.connect(
	host="localhost",
	user="root",
	password="",
	database="alumnos")

cursor = conexion.cursor()

frame=LabelFrame(root,text="Inicio de sesión:")
frame.pack()

titulo=Label(frame,text="Login")
titulo.config(font=("Calibri",14))
titulo.grid(row=0,column=0,sticky="nsew",pady=5,padx=5,columnspan=2)

label1=Label(frame,text="Usuario:").grid(row=1,column=0,sticky="w",pady=5,padx=5)
label2=Label(frame,text="Contraseña:").grid(row=2,column=0,sticky="w",pady=5,padx=5)

usuario=StringVar()
contrasena=StringVar()

Entrada1=Entry(frame,textvariable=usuario).grid(row=1,column=1,sticky="e",pady=5,padx=5)
Entrada2=Entry(frame,textvariable=contrasena,show="*").grid(row=2,column=1,sticky="e",pady=5,padx=5)

def click_boton():

	v=IntVar()
	v.set(0)
	
	instruccion="SELECT * FROM usuarios"

	cursor.execute(instruccion)

	filas=cursor.fetchall()

	for i in filas:

		if usuario.get()==i[1] and check_password_hash(i[2],contrasena.get())==True and i[4]=="ADMIN":

			messagebox.showinfo("Inicio exitoso", "El inicio de sesión ha sido exitoso.")

			v.set(1)

			root.destroy()

			ventana_1()

		elif usuario.get()==i[1] and check_password_hash(i[2],contrasena.get())==True and i[4]=="USER":

			messagebox.showinfo("Inicio exitoso", "El inicio de sesión ha sido exitoso.")

			v.set(1)

			t=int(i[3])

			if t==2:

				root.destroy()

				v_segundo()

			if t==3:

				root.destroy()

				v_tercero()

			if t==4:

				root.destroy()

				v_cuarto()

			if t==5:

				root.destroy()

				v_quinto()

			if t==6:

				root.destroy()

				v_sexto()

			if t==1:

				root.destroy()

				v_primero()

	if v.get()==0:

		messagebox.showwarning("No se pudo iniciar,","No se puedo iniciar sesión.")

botonEnviar = Button(frame,text="Enviar",padx=5,pady=5,command=click_boton).grid(row=3,column=0,columnspan=2)

root.bind("<Return>", lambda _: click_boton())

root.bind("<KP_Enter>", lambda _: click_boton())

root.mainloop()
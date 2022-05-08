from tkinter import *
from tkinter import messagebox
import mysql.connector as database
import inicio
import inicio_user
from werkzeug.security import generate_password_hash, check_password_hash
from tkinter import messagebox

root = Tk()
root.title("Login")

conexion= database.connect(
	host="localhost",
	user="root",
	password="",
	database="inventario")

cursor = conexion.cursor()

frame=LabelFrame(root,text="Administrador de inventario:")
frame.pack()

titulo=Label(frame,text="Login")
titulo.config(font=("Calibri",14))
titulo.grid(row=0,column=0,sticky="nsew",pady=5,padx=5,columnspan=2)

label1=Label(frame,text="Usuario:").grid(row=1,column=0,sticky="w",pady=5,padx=5)
label2=Label(frame,text="Contraseña:").grid(row=2,column=0,sticky="w",pady=5,padx=5)

usuario=StringVar()
contrasena=StringVar()

Entrada1=Entry(frame,textvariable=usuario)
Entrada1.grid(row=1,column=1,sticky="e",pady=5,padx=5)
Entrada1.focus()
Entrada2=Entry(frame,textvariable=contrasena,show="*").grid(row=2,column=1,sticky="e",pady=5,padx=5)

def click_boton():

	v=IntVar()
	v.set(0)
	
	instruccion="SELECT * FROM usuarios"

	cursor.execute(instruccion)

	filas=cursor.fetchall()

	for i in filas:

		if usuario.get()==i[1] and check_password_hash(i[2],contrasena.get())==True and i[3]=="ADMIN":

			messagebox.showinfo("Inicio exitoso", "El inicio de sesión ha sido exitoso.")

			v.set(1)

			root.destroy()

			inicio.ventana_1()

		if usuario.get()==i[1] and check_password_hash(i[2],contrasena.get())==True and i[3]=="USER":

			messagebox.showinfo("Inicio exitoso", "El inicio de sesión ha sido exitoso.")

			v.set(1)

			root.destroy()

			inicio_user.ventana_1()

	if v.get()==0:

		messagebox.showwarning("No se pudo iniciar,","No se puedo iniciar sesión.")

botonEnviar = Button(frame,text="Enviar",padx=5,pady=5,command=click_boton).grid(row=3,column=0,columnspan=2)

root.bind("<Return>", lambda _: click_boton())

root.bind("<KP_Enter>", lambda _: click_boton())

root.mainloop()
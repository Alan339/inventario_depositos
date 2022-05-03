from tkinter import *
from tkinter import messagebox
from primero_admin import *
from segundo_admin import *
from tercero_admin import *
from cuarto_admin import *
from quinto_admin import *
from sexto_admin import *

def ventana_1():

	inicio=Tk()
	inicio.title("Selección de curso")
	inicio.resizable(False,False)

	########################## Estructura ventana ##########################

	def click_botonA():

		inicio.destroy()

		v_primero()

	def click_botonB():

		inicio.destroy()

		v_segundo()

	def click_botonC():

		inicio.destroy()

		v_tercero()

	def click_botonD():

		inicio.destroy()

		v_cuarto()

	def click_botonE():

		inicio.destroy()

		v_quinto()

	def click_botonF():

		inicio.destroy()

		v_sexto()

	frame=Frame(inicio)
	frame.pack()

	Label(frame, text="ADMINISTRACIÓN DE ALUMNOS",font=("Calibri",12,"bold")).grid(row=0,column=0,padx=5,pady=2)

	imagen=PhotoImage(file="i.png")
	Label(frame,image=imagen).grid(row=0,column=1,padx=5,pady=5,rowspan=2)

	frame2=LabelFrame(inicio,text="Cursos")
	frame2.pack()

	primero=Button(frame2,text="Primero",font=("Sitka Heading",10,"bold"),width=10,command=click_botonA).grid(row=0,column=0,padx=15,pady=10)
	segundo=Button(frame2,text="Segundo",font=("Sitka Heading",10,"bold"),width=10,command=click_botonB).grid(row=0,column=1,padx=15,pady=10)
	tercero=Button(frame2,text="Tercero",font=("Sitka Heading",10,"bold"),width=10,command=click_botonC).grid(row=0,column=2,padx=15,pady=10)
	cuarto=Button(frame2,text="Cuarto",font=("Sitka Heading",10,"bold"),width=10,command=click_botonD).grid(row=0,column=3,padx=15,pady=10)
	quinto=Button(frame2,text="Quinto",font=("Sitka Heading",10,"bold"),width=10,command=click_botonE).grid(row=0,column=4,padx=15,pady=10)
	sexto=Button(frame2,text="Sexto",font=("Sitka Heading",10,"bold"),width=10,command=click_botonF).grid(row=0,column=5,padx=15,pady=10)





	inicio.mainloop()
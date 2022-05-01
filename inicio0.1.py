from tkinter import *
from tkinter import messagebox
import mysql.connector as database
from menu import *

inicio=Tk()
inicio.title("Menu Inventario Informatica")
#inicio.geometry("700x500")

menubar = Menu(inicio)
inicio.config(menu=menubar)

########################## Menú ##########################

def SalirFUN():
	salir = messagebox.askquestion("Salir", "¿Desea salir de la aplicacion?")
	if salir == "yes":
		inicio.destroy()

def sobreque():
	messagebox.showinfo("Acerca de...", "Esta aplicacion fue diseñada por los alumnos de 6to Informatica" )


tablamenu = Menu(menubar, tearoff=0)
tablamenu.add_command(label="Monitores")
tablamenu.add_command(label="Teclados")
tablamenu.add_command(label="Gabinete")
tablamenu.add_command(label="Otros")

modmenu = Menu(menubar, tearoff=0)
modmenu.add_command(label="Ver Datos")
modmenu.add_command(label="Modificar Datos")

guardarmenu = Menu(menubar, tearoff=0)

acercademenu = Menu(menubar, tearoff=0)

herramientasmenu= Menu(menubar, tearoff=0)
herramientasmenu.add_command(label="Acerca de...", command=sobreque)
herramientasmenu.add_separator()
herramientasmenu.add_command(label="Salir", command=SalirFUN)

menubar.add_cascade(label="Tablas", menu=tablamenu)
menubar.add_cascade(label="Modo", menu=modmenu)
menubar.add_cascade(label="Guardar", menu=guardarmenu)
menubar.add_cascade(label="Herramientas", menu=herramientasmenu)

########################## Estructura ventana ##########################

frame=Frame(inicio)
frame.pack()

Label(frame, text="INVENTARIOS DE LOS DEPOSITOS INFORMATICOS",font=("Calibri",24,"bold")).grid(row=0,column=0,padx=5,pady=2)

imagen=PhotoImage(file="i.png")
Label(frame,image=imagen).grid(row=0,column=1,padx=5,pady=5)

frame2=LabelFrame(inicio,text="Tablas")
frame2.pack()

m=PhotoImage(file="m2.png")
t=PhotoImage(file="t2.png")
g=PhotoImage(file="g2.png")
o=PhotoImage(file="o2.png")

b_monitor=Button(frame2,image=m,compound="bottom",text="Monitores",font=("Sitka Heading",10,"bold")).grid(row=0,column=0,padx=50,pady=30)
b_teclado=Button(frame2,image=t,compound="bottom",text="Teclados",font=("Sitka Heading",10,"bold")).grid(row=0,column=1,padx=50,pady=30)
b_gabinete=Button(frame2,image=g,compound="bottom",text="Gabinetes",font=("Sitka Heading",10,"bold")).grid(row=1,column=0,padx=50,pady=30)
b_otros=Button(frame2,image=o,compound="bottom",text="Otros",font=("Sitka Heading",10,"bold")).grid(row=1,column=1,padx=50,pady=30)

footer=Frame(inicio)
footer.pack()



inicio.mainloop()
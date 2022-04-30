from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename

# Configuración de la raíz
root = Tk()
root.title("Menu Inventario Informatica")
root.geometry("700x500")
root.iconbitmap("inventario.ico")
menubar = Menu(root)
root.config(menu=menubar)

def SalirFUN():
	salir = messagebox.askquestion("Salir", "¿Desea salir de la aplicacion?")
	if salir == "yes":
		root.quit()

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
herramientasmenu.add_command(label="Salir", command=SalirFUN)
herramientasmenu.add_command(label="Acerca de...", command=sobreque)

menubar.add_cascade(label="Tablas", menu=tablamenu)
menubar.add_cascade(label="Modo", menu=modmenu)
menubar.add_cascade(label="Guardar", menu=guardarmenu)
menubar.add_cascade(label="Herrramientas", menu=herramientasmenu)


# Finalmente bucle de la aplicación
root.mainloop()
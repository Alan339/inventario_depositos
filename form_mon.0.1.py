from tkinter import *

raiz=Tk()

miFrame=Frame(raiz, width=1000, height=500)
miFrame.pack()


cuadroID=Entry(miFrame)
cuadroID.grid(row=1, column=1, padx=10)
cuadroID.config(justify="center")

cuadroDeposito=Entry(miFrame)
cuadroDeposito.grid(row=1, column=2, padx=10)
cuadroDeposito.config(justify="center")

cuadroMonitor=Entry(miFrame)
cuadroMonitor.grid(row=1, column=3, padx=10)
cuadroMonitor.config(justify="center")


cuadroMonitor=Entry(miFrame)
cuadroMonitor.grid(row=3, column=1, columnspan=2, padx=10)
cuadroMonitor.config(justify="center")

cuadroModelo=Entry(miFrame)
cuadroModelo.grid(row=3, column=2, columnspan=3)
cuadroModelo.config(justify="center")

cuadroCheck=Checkbutton(miFrame)
cuadroCheck.grid(row=5, column=2, padx=10)
cuadroCheck.config(justify="center")

cuadroObservaciones=Entry(miFrame)
cuadroObservaciones.grid(row=7, column=2, pady=10)
cuadroObservaciones.config(justify="center")

cuadroRecomendaciones=Entry(miFrame)
cuadroRecomendaciones.grid(row=9, column=2, pady=10)
cuadroRecomendaciones.config(justify="center")


#-------------------------------------------


IDLabel=Label(miFrame, text="ID:")
IDLabel.grid(row=0, column=1, padx=10, pady=10)

DepositoLabel=Label(miFrame, text="Deposito:")
DepositoLabel.grid(row=0, column=2, padx=10, pady=5)

MonitorLabel=Label(miFrame, text="Monitor:")
MonitorLabel.grid(row=0, column=3, padx=10, pady=5)

MarcaLabel=Label(miFrame, text="Marca:")
MarcaLabel.grid(row=2, column=1, columnspan=2,pady=10)

ModeloLabel=Label(miFrame, text="Modelo:")
ModeloLabel.grid(row=2, column=2, columnspan=3)

FuncionaLabel=Label(miFrame, text="¿Funciona?", pady=10)
FuncionaLabel.grid(row=4, column=2)

ObservacionesLabel=Label(miFrame, text="Observaciones:")
ObservacionesLabel.grid(row=6, column=2)

RecomendacionesLabel=Label(miFrame, text="Observaciones:")
RecomendacionesLabel.grid(row=8, column=2)

raiz.mainloop()
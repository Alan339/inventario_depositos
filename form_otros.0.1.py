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


#-------------------------------------------


IDLabel=Label(miFrame, text="ID:")
IDLabel.grid(row=0, column=1, padx=10, pady=10)

DepositoLabel=Label(miFrame, text="Deposito:")
DepositoLabel.grid(row=0, column=2, padx=10, pady=5)

MonitorLabel=Label(miFrame, text="Cantidad:")
MonitorLabel.grid(row=0, column=3, padx=10, pady=5)


raiz.mainloop()
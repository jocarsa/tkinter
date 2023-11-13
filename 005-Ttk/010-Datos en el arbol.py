import tkinter as tk
from tkinter import ttk

raiz = tk.Tk()

arbol = ttk.Treeview(raiz,columns=('nombre','apellidos','email'))
arbol.heading("#0",text="Identificador")
arbol.heading("nombre",text="Nombre")
arbol.heading("apellidos",text="Apellidos")
arbol.heading("email",text="Correo electrónico")

arbol.insert('','0','elemento1',text="Cliente 1",values=("Juan","Garcia Lopez","juan@jocarsa.com"))
arbol.insert('','1','elemento2',text="Cliente 2",values=("Jose Vicente","Carratalá Sanchis","info@jocarsa.com"))

arbol.pack(padx=50,pady=50)

raiz.mainloop()

import tkinter as tk

raiz = tk.Tk()

archivo = open("estructura.txt","r")
lineas = archivo.readlines()
for linea in lineas:
    elemento = linea.strip()
    if elemento == "entrada":
        tk.Entry(raiz).pack()
    elif elemento == "etiqueta":
        tk.Label(raiz,text="esto es una etiqueta").pack()
    elif elemento == "boton":
        tk.Button(raiz,text="esto es un botón").pack()

raiz.mainloop()

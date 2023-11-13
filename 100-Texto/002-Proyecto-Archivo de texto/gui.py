import tkinter as tk

raiz = tk.Tk()

archivo = open("estructura.txt","r")
lineas = archivo.readlines()
for linea in lineas:
    print(linea.strip())

raiz.mainloop()

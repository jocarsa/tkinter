import tkinter as tk

raiz = tk.Tk()
barramenu= tk.Menu(raiz)
raiz.config(menu=barramenu)
archivo = tk.Menu(barramenu,tearoff=1)
barramenu.add_cascade(label="Arhivo",menu=archivo)

raiz.mainloop()

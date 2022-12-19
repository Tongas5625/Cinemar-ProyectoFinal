import tkinter as tk
from tkinter import messagebox, ttk
def obtener_seleccion():
    # Esto es una tupla con los índices (= las posiciones)
    # de los ítems seleccionados por el usuario.
    indices = listbox.curselection()
    print (listbox.curselection())
    print(listbox.get(1))
    messagebox.showinfo(
        title="Ítems seleccionados",
        # Obtener el texto de cada ítem seleccionado
        # y mostrarlos separados por comas.
        message=", ".join(listbox.get(i) for i in indices)
    )
ventana = tk.Tk()
ventana.geometry("400x300")
ventana.title("Lista en Tk")
listbox = tk.Listbox(selectmode=tk.EXTENDED)
items = (
    "Python",
    "C",
    "C++",
    "Java"
)
listbox.insert(0, *items)
listbox.pack()
boton_obtener_seleccion = ttk.Button(
    text="Obtener selección",
    command=obtener_seleccion
)
boton_obtener_seleccion.pack()
ventana.mainloop()
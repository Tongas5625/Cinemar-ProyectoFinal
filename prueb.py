# Placeholder para inicio de session

import tkinter as tk

# Función para eliminar el texto del placeholder cuando el usuario comience a escribir
def on_entry_click(event):
    if entry.get() == 'Escribe aquí tu texto':
       entry.delete(0, "end") # elimina todo el texto
       entry.config(fg = 'black') # cambia el color del texto a negro

# Función para añadir el texto del placeholder si el usuario borra todo el texto
def on_focusout(event):
    if entry.get() == '':
        entry.insert(0, 'Escribe aquí tu texto')
        entry.config(fg = 'grey')

# Crea la ventana principal y el widget Entry
root = tk.Tk()
entry = tk.Entry(root, fg='grey')
entry.insert(0, 'Escribe aquí tu texto')
entry.pack()

# Asigna las funciones a los eventos focusin y focusout
entry.bind('<FocusIn>', on_entry_click)
entry.bind('<FocusOut>', on_focusout)

root.mainloop()

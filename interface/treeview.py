import tkinter as tk
from tkinter import messagebox, ttk
class Application(ttk.Frame):
    
    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Vista de árbol en Tkinter")
        self.treeview = ttk.Treeview(self)
        self.treeview.insert("", tk.END, text="Elemento 1")
        self.treeview.insert("", tk.END, text="Elemento 2")
        self.treeview.pack()
        self.button = ttk.Button(text="Mostrar selección",
                                 command=self.show_selection)
        self.button.pack(after=self.treeview)
        self.pack()
    
    def show_selection(self):
        try:
            # Obtener el ID del primer elemento seleccionado.
            item = self.treeview.selection()[0]
        except IndexError:
            # Si la tupla está vacía, entonces no hay ningún
            # elemento seleccionado.
            messagebox.showwarning(
                message="Debe seleccionar un elemento.",
                title="No hay selección"
            )
        else:
            # A partir de este ID retornar el texto del elemento.
            text = self.treeview.item(item, option="text")
            # Mostrarlo en un cuadro de diálogo.
            messagebox.showinfo(message=text, title="Selección")
main_window = tk.Tk()
app = Application(main_window)
app.mainloop()
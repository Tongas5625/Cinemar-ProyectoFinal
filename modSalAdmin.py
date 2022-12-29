from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
import tkinter.font as tkFont
from clases.usuarios import Usuario
from clases.sala import Sala
from salaypeli_adm import SalayPeli
from PIL import ImageTk, ImageColor, Image
import os

def valida(input): # funcion para validar box que solo recibe numeros
    if input.isdigit():
        print(input)
        return True
                          
    elif input is "":
        print(input)
        return True
  
    else:
        print(input)
        return False        


class ModificarSalAdmin:
    def __init__(self, root, id_usr):
        root.focus()
        root.grab_set()
        reg=root.register(valida)
        self.usr=Usuario()
        self.usr.recup_usr_db_id(id_usr)        
        #setting title
        root.title("Modifica Sala")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_286=tk.Label(root)
        ft = tkFont.Font(family='Comics',size=17)
        GLabel_286["font"] = ft
        GLabel_286["fg"] = "#333333"
        GLabel_286["justify"] = "center"
        GLabel_286["text"] = "Modificar Sala"
        GLabel_286.place(x=100,y=20,width=400,height=54)

        salatemp=Sala()
        listsalas=[]
        listsalas=salatemp.listsalas()
        self.treeview = ttk.Treeview(columns=("Numero","Tipos", "Asientos"))
        self.treeview.column("#0",anchor=CENTER, stretch=NO, width=50)
        self.treeview.column("#1",anchor=CENTER, stretch=NO, width=100)
        self.treeview.column("#2",anchor=CENTER, stretch=NO, width=50)
        self.treeview.column("#3",anchor=CENTER, stretch=NO, width=100)
        self.treeview.heading("#0", text="ID")
        self.treeview.heading("#1", text="Numero")
        self.treeview.heading("#2", text="Tipo")
        self.treeview.heading("#3", text="Asientos")
        print (listsalas)
        for i in listsalas:
            self.treeview.insert("",tk.END,text=f"{i[0]}",values=(f"{i[1]}", f"{i[2]}", f"{i[3]}"))
        self.treeview.place(x=150,y=100,width=300,height=170) 
        

        GLabel_801=tk.Label(root)
        ft = tkFont.Font(family='Comics',size=10)
        GLabel_801["font"] = ft
        GLabel_801["fg"] = "#333333"
        GLabel_801["justify"] = "center"
        GLabel_801["text"] = "Numero"
        GLabel_801.place(x=100,y=290,width=70,height=25)

        GLabel_79=tk.Label(root)
        ft = tkFont.Font(family='Comics',size=10)
        GLabel_79["font"] = ft
        GLabel_79["fg"] = "#333333"
        GLabel_79["justify"] = "center"
        GLabel_79["text"] = "Tipo"
        GLabel_79.place(x=260,y=290,width=70,height=25)

        GLabel_37=tk.Label(root)
        ft = tkFont.Font(family='Comics',size=10)
        GLabel_37["font"] = ft
        GLabel_37["fg"] = "#333333"
        GLabel_37["justify"] = "center"
        GLabel_37["text"] = "Asientos"
        GLabel_37.place(x=420,y=290,width=70,height=25)

        self.NumSalaBox=tk.Entry(root)
        self.NumSalaBox.config(validate="key", validatecommand=(reg, '%P'))
        self.NumSalaBox["borderwidth"] = "1px"
        ft = tkFont.Font(family='Comics',size=10)
        self.NumSalaBox["font"] = ft
        self.NumSalaBox["fg"] = "#333333"
        self.NumSalaBox["justify"] = "center"
        self.NumSalaBox["text"] = "NumeroSala"
        self.NumSalaBox.place(x=100,y=340,width=70,height=25)

        
        
        GListBox_980=tk.Listbox(root)
        GListBox_980["borderwidth"] = "1px"
        ft = tkFont.Font(family='Comics',size=10)
        GListBox_980["font"] = ft
        GListBox_980["fg"] = "#333333"
        GListBox_980["justify"] = "center"
        GListBox_980.place(x=260,y=340,width=80,height=25)

        self.NumAsientosBox=tk.Entry(root)
        self.NumAsientosBox.config(validate="key", validatecommand=(reg, '%P'))
        self.NumAsientosBox["borderwidth"] = "1px"
        ft = tkFont.Font(family='Comics',size=10)
        self.NumAsientosBox["font"] = ft
        self.NumAsientosBox["fg"] = "#333333"
        self.NumAsientosBox["justify"] = "center"
        self.NumAsientosBox["text"] = "Asientos Sala"
        self.NumAsientosBox.place(x=420,y=340,width=70,height=25)

        GButton_108=tk.Button(root)
        GButton_108["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Comics',size=10)
        GButton_108["font"] = ft
        GButton_108["fg"] = "#000000"
        GButton_108["justify"] = "center"
        GButton_108["text"] = "Modificar Sala"
        GButton_108.place(x=240,y=400,width=119,height=30)
        GButton_108["command"] = self.GButton_108_command
      
        
    def GButton_108_command(self):
        
        item = self.treeview.selection()
        # A partir de este ID retornar el texto del elemento.
        idsala = self.treeview.item(item, option="text")
        salatemp=Sala()
        salatemp.recup_sala_db_id(item)
        
        # Mostrarlo en un cuadro de diálogo.
        # messagebox.showinfo(message=text, title="Selección")
    

            
        
if __name__ == "__main__":
    root = tk.Tk()
    app = ModificarSalAdmin(root,3)
    root.mainloop()
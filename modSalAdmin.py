from tkinter import *
import tkinter as tk
import tkinter.font as tkFont
from clases.usuarios import Usuario
from clases.sala import Sala
from salaypeli_adm import SalayPeli
from PIL import ImageTk, ImageColor, Image
import os



class ModificarSalAdmin:
    def __init__(self, root, id_usr):
        root.focus()
        root.grab_set()
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
        ft = tkFont.Font(family='Times',size=17)
        GLabel_286["font"] = ft
        GLabel_286["fg"] = "#333333"
        GLabel_286["justify"] = "center"
        GLabel_286["text"] = "Modificar Sala"
        GLabel_286.place(x=100,y=20,width=400,height=54)

        salatemp=Sala()
        listsalas=[]
        listsalas=salatemp.listsalas()
        GListBox_101=tk.Listbox(root)
        GListBox_101.insert(0,*listsalas)
        GListBox_101["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_101["font"] = ft
        GListBox_101["fg"] = "#333333"
        GListBox_101["justify"] = "center"
        GListBox_101.place(x=60,y=80,width=485,height=188)

        GLabel_801=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_801["font"] = ft
        GLabel_801["fg"] = "#333333"
        GLabel_801["justify"] = "center"
        GLabel_801["text"] = "numero"
        GLabel_801.place(x=100,y=290,width=70,height=25)

        GLabel_79=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_79["font"] = ft
        GLabel_79["fg"] = "#333333"
        GLabel_79["justify"] = "center"
        GLabel_79["text"] = "tipo"
        GLabel_79.place(x=260,y=290,width=70,height=25)

        GLabel_37=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_37["font"] = ft
        GLabel_37["fg"] = "#333333"
        GLabel_37["justify"] = "center"
        GLabel_37["text"] = "asientos"
        GLabel_37.place(x=420,y=290,width=70,height=25)

        GLineEdit_840=tk.Entry(root)
        GLineEdit_840["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_840["font"] = ft
        GLineEdit_840["fg"] = "#333333"
        GLineEdit_840["justify"] = "center"
        GLineEdit_840["text"] = "NumeroSala"
        GLineEdit_840.place(x=100,y=340,width=70,height=25)

        
        
        GListBox_980=tk.Listbox(root)
        GListBox_980["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_980["font"] = ft
        GListBox_980["fg"] = "#333333"
        GListBox_980["justify"] = "center"
        GListBox_980.place(x=260,y=340,width=80,height=25)

        GLineEdit_381=tk.Entry(root)
        GLineEdit_381["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_381["font"] = ft
        GLineEdit_381["fg"] = "#333333"
        GLineEdit_381["justify"] = "center"
        GLineEdit_381["text"] = "AsientosSala"
        GLineEdit_381.place(x=420,y=340,width=70,height=25)

        GButton_108=tk.Button(root)
        GButton_108["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_108["font"] = ft
        GButton_108["fg"] = "#000000"
        GButton_108["justify"] = "center"
        GButton_108["text"] = "Button"
        GButton_108.place(x=240,y=400,width=119,height=30)
        GButton_108["command"] = self.GButton_108_command

    def GButton_108_command(self):
        print("command")

        
def main():
    root = tk.Tk()
    
    # Carpeta accedder al directorio
    carpeta_principal = os.path.dirname(__file__)
    print(carpeta_principal)
    # Carpeta acceder imagenes
    carpeta_Imagenes = os.path.join(carpeta_principal, "imagenes")
    print(carpeta_Imagenes)
    # Icono
    root.iconbitmap(os.path.join(carpeta_Imagenes, "iconoLogin.ico"))
    icoImg = ImageTk.PhotoImage(Image.open(os.path.join(carpeta_Imagenes, "fondoAdmin2.png")).resize((600, 500)))
    etiqueta = Label(image=icoImg)
    etiqueta.pack()
    app=ModificarSalAdmin(root,1)
    root.mainloop()


if __name__ == "__main__":
    main()
from tkinter import *
import tkinter as tk
import tkinter.font as tkFont
from clases.usuarios import Usuario
from salaypeli_adm import SalayPeli
from PIL import ImageTk, ImageColor, Image
import os



class ModificarDescuento:
    def __init__(self, root, id_usr):
        root.focus()
        root.grab_set()
        self.usr=Usuario()
        self.usr.recup_usr_db_id(id_usr)        
        #setting title
        root.title("Modificar Descuento - Cinemar")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_295=tk.Label(root)
        GLabel_295["bg"] = "#FFF"
        ft = tkFont.Font(family='Times',size=25)
        GLabel_295["font"] = ft
        GLabel_295["fg"] = "black"
        GLabel_295["justify"] = "center"
        GLabel_295["text"] = "Modificar Descuento"
        GLabel_295.place(x=150,y=10,width=300,height=40)
        
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
    app=ModificarDescuento(root,1)
    root.mainloop()


if __name__ == "__main__":
    main()
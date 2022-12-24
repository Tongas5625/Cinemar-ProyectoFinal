from tkinter import *
import tkinter as tk
import tkinter.font as tkFont
from clases.usuarios import Usuario
from salaypeli_adm import SalayPeli
from modSalAdmin import ModificarSalAdmin
from eliminarSala_adm import EliminarSala
from butacasDisp_admin import ButacasDisponibles
from reservaCientes_adm import ReservaClientes
from modifDesc import  ModificarDescuento

from PIL import ImageTk, ImageColor, Image
import os

class Menu_Admin:
    
    def __init__(self, root, id_usr):
        root.focus()
        root.grab_set()
        root.configure(bg='#1A120B')
        self.usr=Usuario()
        self.usr.recup_usr_db_id(id_usr)
        #setting title
        root.title("Administracion - Cinemar")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        
        GLabel_295=tk.Label(root)
        GLabel_295["bg"] ="#3C2A21"
        ft = tkFont.Font(family='Times',size=25)
        GLabel_295["font"] = ft
        GLabel_295["fg"] = "#D5CEA3"
        GLabel_295["justify"] = "center"
        GLabel_295["text"] = "ADMINISTRACIÓN "
        GLabel_295.place(x=150,y=10,width=300,height=40)
        
        CrearSalaConPeli=tk.Button(root)
        CrearSalaConPeli["bg"] = "#3C2A21"
        ft = tkFont.Font(family='Times',size=16)
        CrearSalaConPeli["font"] = ft
        CrearSalaConPeli["fg"] = "#D5CEA3"
        CrearSalaConPeli["justify"] = "center"
        CrearSalaConPeli["text"] = "Crear una sala"
        CrearSalaConPeli.place(x=175,y=90,width=250,height=40)
        CrearSalaConPeli.bind('<Button-1>', self.CrearSalaConPeli_command)
        
        ModificarSala=tk.Button(root)
        ModificarSala["bg"] = "#3C2A21"
        ft = tkFont.Font(family='Times',size=16)
        ModificarSala["font"] = ft
        ModificarSala["fg"] = "#D5CEA3"
        ModificarSala["justify"] = "center"
        ModificarSala["text"] = "Modificar una sala"
        ModificarSala.place(x=175,y=140,width=250,height=40)
        ModificarSala.bind('<Button-1>', self.ModificarSala_command)
        
        EliminarSala=tk.Button(root)
        EliminarSala["bg"] = "#3C2A21"
        ft = tkFont.Font(family='Times',size=16)
        EliminarSala["font"] = ft
        EliminarSala["fg"] = "#D5CEA3"
        EliminarSala["justify"] = "center"
        EliminarSala["text"] = "Eliminar una sala"
        EliminarSala.place(x=175,y=190,width=250,height=40)
        EliminarSala.bind('<Button-1>', self.EliminarSala_command)
            
        VerReservClientes=tk.Button(root)
        VerReservClientes["activebackground"] = "#0b0a0a"
        VerReservClientes["bg"] = "#3C2A21"
        ft = tkFont.Font(family='Times',size=16)
        VerReservClientes["font"] = ft
        VerReservClientes["fg"] = "#D5CEA3"
        VerReservClientes["justify"] = "center"
        VerReservClientes["text"] = "Ver reserva de los clientes "
        VerReservClientes.place(x=175,y=240,width=250,height=40)
        VerReservClientes.bind('<Button-1>', self.VerReservClientes_command)
        
        VerButcDisp=tk.Button(root)
        VerButcDisp["bg"] = "#3C2A21"
        ft = tkFont.Font(family='Times',size=16)
        VerButcDisp["font"] = ft
        VerButcDisp["fg"] = "#D5CEA3"
        VerButcDisp["justify"] = "center"
        VerButcDisp["text"] = "Ver butacas disponibles"
        VerButcDisp.place(x=175,y=290,width=250,height=40)
        VerButcDisp.bind('<Button-1>', self.VerButcDisp_command)
        
        ModificarDescuento=tk.Button(root)
        ModificarDescuento["bg"] = "#3C2A21"
        ft = tkFont.Font(family='Times',size=16)
        ModificarDescuento["font"] = ft
        ModificarDescuento["fg"] = "#D5CEA3"
        ModificarDescuento["justify"] = "center"
        ModificarDescuento["text"] = "Modificar descuentos"
        ModificarDescuento.place(x=175,y=340,width=250,height=40)
        ModificarDescuento.bind('<Button-1>', self.ModificarDescuento_command)

        AtrasButton=tk.Button(root, command=root.destroy)
        AtrasButton["bg"] = "#FF5722"
        ft = tkFont.Font(family='Comics',size=22)
        AtrasButton["font"] = ft
        AtrasButton["fg"] = "#EEEEEE"
        AtrasButton["justify"] = "center"
        AtrasButton["text"] = "Atras"
        AtrasButton.place(x=250,y=420,width=100,height=40)
        
    def CrearSalaConPeli_command(self,salaypeli):
        salaypeli=tk.Toplevel()
        SalayPeli(salaypeli,self.usr.id)
        
        
    def ModificarSala_command(self, modSalAdmin):
        modSalAdmin=tk.Toplevel()
        ModificarSalAdmin(modSalAdmin, self.usr.id)

    def EliminarSala_command(self,eliminSalAdmin):
       eliminSalAdmin=tk.Toplevel()
       EliminarSala(eliminSalAdmin,self.usr.id)
        
    def VerReservClientes_command(self, reservClients):
        reservClients=tk.Toplevel()
        ReservaClientes(reservClients,self.usr.id)

    def VerButcDisp_command(self, butDisp):
        butDisp=tk.Toplevel()
        ButacasDisponibles(butDisp,self.usr.id)
        
    def ModificarDescuento_command(self, modifDesc):
        modifDesc=tk.Toplevel()
        ModificarDescuento(modifDesc,self.usr.id)
        
    
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
    app=Menu_Admin(root,1)
    root.mainloop()


if __name__ == "__main__":
    main()
    
        
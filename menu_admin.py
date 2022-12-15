import tkinter as tk
import tkinter.font as tkFont
from clases.usuarios import Usuario
from salaypeli_adm import SalayPeli
class Menu_Admin:
    def __init__(self, root, id_usr):
        root.focus()
        root.grab_set()
        self.usr=Usuario()
        self.usr.recup_usr_db_id(id_usr)
        #setting title
        root.title("Administracion")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_295=tk.Label(root)
        GLabel_295["bg"] = "#37c1a1"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_295["font"] = ft
        GLabel_295["fg"] = "#333333"
        GLabel_295["justify"] = "center"
        GLabel_295["text"] = "ADMINISTRACION "
        GLabel_295.place(x=40,y=20,width=500,height=40)

        VerReservClientes=tk.Button(root)
        VerReservClientes["activebackground"] = "#0b0a0a"
        VerReservClientes["bg"] = "#9fd5ca"
        ft = tkFont.Font(family='Times',size=10)
        VerReservClientes["font"] = ft
        VerReservClientes["fg"] = "#000000"
        VerReservClientes["justify"] = "center"
        VerReservClientes["text"] = "Ver reserva de todos los clientes "
        VerReservClientes.place(x=160,y=80,width=250,height=30)
        VerReservClientes["command"] = self.VerReservClientes_command

        VerReservUser=tk.Button(root)
        VerReservUser["bg"] = "#9fd5ca"
        ft = tkFont.Font(family='Times',size=10)
        VerReservUser["font"] = ft
        VerReservUser["fg"] = "#000000"
        VerReservUser["justify"] = "center"
        VerReservUser["text"] = "Ver reserva de un cliente en particular"
        VerReservUser.place(x=160,y=130,width=250,height=30)
        VerReservUser["command"] = self.VerReservUser_command

        CrearSalaConPeli=tk.Button(root)
        CrearSalaConPeli["bg"] = "#9fd5ca"
        ft = tkFont.Font(family='Times',size=10)
        CrearSalaConPeli["font"] = ft
        CrearSalaConPeli["fg"] = "#000000"
        CrearSalaConPeli["justify"] = "center"
        CrearSalaConPeli["text"] = "Crear una sala con la pelicula"
        CrearSalaConPeli.place(x=160,y=180,width=250,height=30)
        CrearSalaConPeli["command"] = self.CrearSalaConPeli_command

        ModificarSala=tk.Button(root)
        ModificarSala["bg"] = "#9fd5ca"
        ft = tkFont.Font(family='Times',size=10)
        ModificarSala["font"] = ft
        ModificarSala["fg"] = "#000000"
        ModificarSala["justify"] = "center"
        ModificarSala["text"] = "Modificar una sala"
        ModificarSala.place(x=160,y=230,width=250,height=30)
        ModificarSala["command"] = self.ModificarSala_command

        EliminarSala=tk.Button(root)
        EliminarSala["bg"] = "#9fd5ca"
        ft = tkFont.Font(family='Times',size=10)
        EliminarSala["font"] = ft
        EliminarSala["fg"] = "#000000"
        EliminarSala["justify"] = "center"
        EliminarSala["text"] = "Eliminar una sala"
        EliminarSala.place(x=160,y=280,width=250,height=30)
        EliminarSala["command"] = self.EliminarSala_command

        ModificarDescuento=tk.Button(root)
        ModificarDescuento["bg"] = "#9fd5ca"
        ft = tkFont.Font(family='Times',size=10)
        ModificarDescuento["font"] = ft
        ModificarDescuento["fg"] = "#000000"
        ModificarDescuento["justify"] = "center"
        ModificarDescuento["text"] = "Modificar descuentos"
        ModificarDescuento.place(x=160,y=330,width=250,height=30)
        ModificarDescuento["command"] = self.ModificarDescuento_command
        
        AtrasButton=tk.Button(root, command=root.destroy)
        AtrasButton["bg"] = "#75FF46"
        ft = tkFont.Font(family='Comics',size=13)
        AtrasButton["font"] = ft
        AtrasButton["fg"] = "#000000"
        AtrasButton["justify"] = "center"
        AtrasButton["text"] = "Atras"
        AtrasButton.place(x=250,y=400,width=91,height=30)

    def VerReservClientes_command(self):
        print("command")


    def VerReservUser_command(self):
        print("command")


    def CrearSalaConPeli_command(self):
        salaypeli=tk.Toplevel()
        SalayPeli(salaypeli,self.usr.id)
        
        print("command")

    def ModificarSala_command(self):
        print("command")


    def EliminarSala_command(self):
        print("command")


    def ModificarDescuento_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = Menu_Admin(root,1)
    root.mainloop()
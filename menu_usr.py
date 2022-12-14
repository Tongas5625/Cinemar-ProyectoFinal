import tkinter as tk
import tkinter.font as tkFont
from clases.usuarios import Usuario
class Menu_Usr:
    def __init__(self, root, id_usr): #atencion recibe id de usuario
        self.usr=Usuario()
        self.usr.recup_usr_db_id(id_usr)#recuperamos datos de user de db
        #setting title
        root.title("Menu Usuario")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_254=tk.Label(root)
        GLabel_254["bg"] = "#8159de"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_254["font"] = ft
        GLabel_254["fg"] = "#0f0707"
        GLabel_254["justify"] = "center"
        GLabel_254["text"] = "BIENVENIDO"
        GLabel_254.place(x=90,y=20,width=400,height=35)

        CrearReserva=tk.Button(root)
        CrearReserva["bg"] = "#e6d49a"
        ft = tkFont.Font(family='Times',size=10)
        CrearReserva["font"] = ft
        CrearReserva["fg"] = "#000000"
        CrearReserva["justify"] = "center"
        CrearReserva["text"] = "CREAR RESERVA"
        CrearReserva.place(x=150,y=70,width=250,height=30)
        CrearReserva["command"] = self.CrearReserva_command

        ModificarReserva=tk.Button(root)
        ModificarReserva["bg"] = "#e6d49a"
        ft = tkFont.Font(family='Times',size=10)
        ModificarReserva["font"] = ft
        ModificarReserva["fg"] = "#000000"
        ModificarReserva["justify"] = "center"
        ModificarReserva["text"] = "MODIFICAR UNA RESERVA"
        ModificarReserva.place(x=150,y=120,width=250,height=30)
        ModificarReserva["command"] = self.ModificarReserva_command

        VerReservas=tk.Button(root)
        VerReservas["bg"] = "#e6d49a"
        ft = tkFont.Font(family='Times',size=10)
        VerReservas["font"] = ft
        VerReservas["fg"] = "#000000"
        VerReservas["justify"] = "center"
        VerReservas["text"] = "VER MIS RESERVAS"
        VerReservas.place(x=150,y=170,width=250,height=30)
        VerReservas["command"] = self.VerReservas_command

        HistoricoEntradas=tk.Button(root)
        HistoricoEntradas["bg"] = "#e6d49a"
        ft = tkFont.Font(family='Times',size=10)
        HistoricoEntradas["font"] = ft
        HistoricoEntradas["fg"] = "#000000"
        HistoricoEntradas["justify"] = "center"
        HistoricoEntradas["text"] = "HISTORICO DE ENTRADAS"
        HistoricoEntradas.place(x=150,y=220,width=250,height=30)
        HistoricoEntradas["command"] = self.HistoricoEntradas_command

    def CrearReserva_command(self):
        print("command")


    def ModificarReserva_command(self):
        print("command")


    def VerReservas_command(self):
        print("command")


    def HistoricoEntradas_command(self):
        print("command")

#if __name__ == "__main__":
#    root = tk.Tk()
#    app = Menu_Usr(root)
#    root.mainloop()
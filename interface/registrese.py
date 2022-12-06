import tkinter as tk
import tkinter.font as tkFont

class Registrese:
    def __init__(self, root):
        #setting title
        root.title("registrese")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_845=tk.Label(root)
        GLabel_845["bg"] = "#cb7dd0"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_845["font"] = ft
        GLabel_845["fg"] = "#0b0505"
        GLabel_845["justify"] = "center"
        GLabel_845["text"] = "Regístrese y crea un nuevo usuario"
        GLabel_845.place(x=130,y=20,width=300,height=40)

        NombreLab=tk.Label(root)
        NombreLab["bg"] = "#eed88f"
        ft = tkFont.Font(family='Times',size=10)
        NombreLab["font"] = ft
        NombreLab["fg"] = "#333333"
        NombreLab["justify"] = "center"
        NombreLab["text"] = "Nombre"
        NombreLab.place(x=50,y=90,width=250,height=30)

        self.NombreBox=tk.Entry(root)
        self.NombreBox["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.NombreBox["font"] = ft
        self.NombreBox["fg"] = "#333333"
        self.NombreBox["justify"] = "center"
        self.NombreBox["text"] = "Nombre"
        self.NombreBox.place(x=280,y=90,width=250,height=30)

        ApellidoLab=tk.Label(root)
        ApellidoLab["bg"] = "#eed88f"
        ft = tkFont.Font(family='Times',size=10)
        ApellidoLab["font"] = ft
        ApellidoLab["fg"] = "#333333"
        ApellidoLab["justify"] = "center"
        ApellidoLab["text"] = "Apellido"
        ApellidoLab.place(x=50,y=140,width=250,height=30)

        self.ApellidoBox=tk.Entry(root)
        self.ApellidoBox["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.ApellidoBox["font"] = ft
        self.ApellidoBox["fg"] = "#333333"
        self.ApellidoBox["justify"] = "center"
        self.ApellidoBox["text"] = "Apellido"
        self.ApellidoBox.place(x=280,y=140,width=250,height=30)

        DniLab=tk.Label(root)
        DniLab["bg"] = "#eed88f"
        ft = tkFont.Font(family='Times',size=10)
        DniLab["font"] = ft
        DniLab["fg"] = "#333333"
        DniLab["justify"] = "center"
        DniLab["text"] = "DNI"
        DniLab.place(x=50,y=190,width=250,height=30)

        self.DniBox=tk.Entry(root)
        self.DniBox["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.DniBox["font"] = ft
        self.DniBox["fg"] = "#333333"
        self.DniBox["justify"] = "center"
        self.DniBox["text"] = "DNI"
        self.DniBox.place(x=280,y=190,width=250,height=30)

        CorreoLab=tk.Label(root)
        CorreoLab["bg"] = "#eed88f"
        ft = tkFont.Font(family='Times',size=10)
        CorreoLab["font"] = ft
        CorreoLab["fg"] = "#333333"
        CorreoLab["justify"] = "center"
        CorreoLab["text"] = "Correo"
        CorreoLab.place(x=50,y=240,width=250,height=30)

        self.CorreoBox=tk.Entry(root)
        self.CorreoBox["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.CorreoBox["font"] = ft
        self.CorreoBox["fg"] = "#333333"
        self.CorreoBox["justify"] = "center"
        self.CorreoBox["text"] = "Correo"
        self.CorreoBox.place(x=280,y=240,width=250,height=30)

        PasswLab=tk.Label(root)
        PasswLab["bg"] = "#eed88f"
        ft = tkFont.Font(family='Times',size=10)
        PasswLab["font"] = ft
        PasswLab["fg"] = "#333333"
        PasswLab["justify"] = "center"
        PasswLab["text"] = "Contraseña"
        PasswLab.place(x=50,y=300,width=250,height=30)

        self.PasswBox=tk.Entry(root)
        self.PasswBox["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.PasswBox["font"] = ft
        self.PasswBox["fg"] = "#333333"
        self.PasswBox["justify"] = "center"
        self.PasswBox["text"] = "Contraseña"
        self.PasswBox.place(x=280,y=300,width=250,height=30)
        RegistrarseBot=tk.Button(root)
        RegistrarseBot["bg"] = "#bbafaf"
        ft = tkFont.Font(family='Times',size=10)
        RegistrarseBot["font"] = ft
        RegistrarseBot["fg"] = "#551a1a"
        RegistrarseBot["justify"] = "center"
        RegistrarseBot["text"] = "Registrarse"
        RegistrarseBot.place(x=130,y=410,width=300,height=30)
        RegistrarseBot["command"] = self.RegistrarseBot_command

    def RegistrarseBot_command(self):
        print(self.PasswBox.get())
        print(self.NombreBox.get())

if __name__ == "__main__":
    root = tk.Tk()
    app = Registrese(root)
    root.mainloop()

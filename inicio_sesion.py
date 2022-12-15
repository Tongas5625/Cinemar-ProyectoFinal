import tkinter as tk
import tkinter.font as tkFont
from clases.usuarios import Usuario
from registrese import Registrese
from menu_usr import Menu_Usr
from menu_admin import Menu_Admin
from tkinter import messagebox


class App:
    def __init__(self, root):
        # setting title
        root.title("inicio de sesion")
        # setting window size
        width = 600
        height = 500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height,
                                    (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_523 = tk.Label(root)
        GLabel_523["bg"] = "#b0b9bc"
        ft = tkFont.Font(family='Times', size=10)
        GLabel_523["font"] = ft
        GLabel_523["fg"] = "#131416"
        GLabel_523["justify"] = "center"
        GLabel_523["text"] = "Inicio de sesión"
        GLabel_523.place(x=200, y=20, width=150, height=50)

        CorreoLab = tk.Label(root)
        CorreoLab["bg"] = "#e47be6"
        ft = tkFont.Font(family='Times', size=10)
        CorreoLab["font"] = ft
        CorreoLab["fg"] = "#333333"
        CorreoLab["justify"] = "center"
        CorreoLab["text"] = "correo"
        CorreoLab.place(x=200, y=110, width=150, height=25)

        self.CorreoBox = tk.Entry(root)
        self.CorreoBox["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        self.CorreoBox["font"] = ft
        self.CorreoBox["fg"] = "#352c2c"
        self.CorreoBox["justify"] = "center"
        self.CorreoBox["text"] = "correo"
        self.CorreoBox.place(x=200, y=150, width=150, height=30)

        PasswdLab = tk.Label(root)
        PasswdLab["bg"] = "#e47be6"
        ft = tkFont.Font(family='Times', size=10)
        PasswdLab["font"] = ft
        PasswdLab["fg"] = "#141314"
        PasswdLab["justify"] = "center"
        PasswdLab["text"] = "contraseña"
        PasswdLab.place(x=200, y=200, width=150, height=30)

        self.PasswdBox = tk.Entry(root, show="*")
        ft = tkFont.Font(family='Times', size=10)
        self.PasswdBox["font"] = ft
        self.PasswdBox["fg"] = "#333333"
        self.PasswdBox["justify"] = "center"
        self.PasswdBox["text"] = "contraseña"
        self.PasswdBox.place(x=200, y=240, width=150, height=30)

        RegistreseLab = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        RegistreseLab["font"] = ft
        RegistreseLab["fg"] = "#333333"
        RegistreseLab["justify"] = "center"
        RegistreseLab["text"] = "Si desea registrarse presione *Registrese*"
        RegistreseLab.place(x=160, y=330, width=250, height=50)

        IniciarBot = tk.Button(root, command=self.IniciarBot_command)
        IniciarBot["bg"] = "#656bbc"
        ft = tkFont.Font(family='Times', size=10)
        IniciarBot["font"] = ft
        IniciarBot["fg"] = "#000000"
        IniciarBot["justify"] = "center"
        IniciarBot["text"] = "Iniciar sesión"
        IniciarBot.place(x=230, y=290, width=90, height=30)
        #IniciarBot["command"] = root.withdraw

        RegistreseBot = tk.Button(root)
        RegistreseBot["bg"] = "#3e7b76"
        ft = tkFont.Font(family='Times', size=10)
        RegistreseBot["font"] = ft
        RegistreseBot["fg"] = "#000000"
        RegistreseBot["justify"] = "center"
        RegistreseBot["text"] = "Regístrese"
        RegistreseBot.place(x=170, y=370, width=200, height=35)
        RegistreseBot["command"] = self.RegistreseBot_command
        # root.withdraw

    def IniciarBot_command(self):
        print(f"el usuario :{self.CorreoBox.get()} esta iniciando seccion")
        usr = Usuario()
        if (usr.recup_usr_db_mail(self.CorreoBox.get())):
            print(f"el usuario existe {self.CorreoBox.get()}")
            print("usuario encontrado en bases de datos logueando")

            if (usr.passw == self.PasswdBox.get()):
                messagebox.showinfo(
                    '', f'{usr} \ny su contraseña coinciden en bases de datos, logueando')
                print(usr)

                if (usr.esadmin()):
                    menu_admin = tk.Toplevel()
                    Menu_Admin(menu_admin, usr.id)
                else:
                    menu_usr = tk.Tk()
                    Menu_Usr(menu_usr, usr.id)

            else:
                messagebox.showerror('', 'Contraseña Incorrecta.')
        else:
            messagebox.showerror('', 'El usuario no esta registrado')

    def RegistreseBot_command(self):
        regist = tk.Tk()
        Registrese(regist)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

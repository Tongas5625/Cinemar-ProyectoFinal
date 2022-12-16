from tkinter import *
import tkinter as tk
import tkinter.font as tkFont
from clases.usuarios import Usuario
from registrese import Registrese
from menu_usr import Menu_Usr
from menu_admin import Menu_Admin
from tkinter import messagebox
from PIL import ImageTk, ImageColor, Image
import os

class App:

    def __init__(self, root):

        # setting title
        root.title('Inicio de sesion')
        # setting window size
        width = 600
        height = 500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height,(screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_523 = tk.Label(root)
        GLabel_523["bg"] = "#fff"
        ft = tkFont.Font(family='Times', size=30)
        GLabel_523["font"] = ft
        GLabel_523["fg"] = "black"
        GLabel_523["justify"] = "center"
        GLabel_523["text"] = "Inicio de sesión"
        GLabel_523.place(x=180, y=20, width=250, height=50)

        CorreoLab = tk.Label(root)
        CorreoLab["bg"] = "#FFD700"
        CorreoLab["borderwidth"] = "4px"
        ft = tkFont.Font(family='Times', size=25)
        CorreoLab["font"] = ft
        CorreoLab["fg"] = "black"
        CorreoLab["justify"] = "center"
        CorreoLab["text"] = "Correo"
        CorreoLab.place(x=240, y=100, width=120, height=40)

        self.CorreoBox = tk.Entry(root)
        self.CorreoBox.config()
        self.CorreoBox["borderwidth"] = "5px"
        ft = tkFont.Font(family='Times', size=12)
        self.CorreoBox["font"] = ft
        self.CorreoBox["fg"] = "black"
        self.CorreoBox["justify"] = "center"
        self.CorreoBox["text"] = "example@example.com"
        self.CorreoBox.place(x=220, y=150, width=160, height=40)

        PasswdLab = tk.Label(root)
        PasswdLab["bg"] = "#FFD700"
        ft = tkFont.Font(family='Times', size=19)
        PasswdLab["font"] = ft
        PasswdLab["fg"] = "#141314"
        PasswdLab["justify"] = "center"
        PasswdLab["text"] = "Contraseña"
        PasswdLab.place(x=240, y=220, width=120, height=40)

        self.PasswdBox = tk.Entry(root, show="*")
        self.PasswdBox["borderwidth"] = "5px"
        ft = tkFont.Font(family='Times', size=13)
        self.PasswdBox["font"] = ft
        self.PasswdBox["fg"] = "#333333"
        self.PasswdBox["justify"] = "center"
        self.PasswdBox["text"] = "contraseña"
        self.PasswdBox.place(x=220, y=270, width=160, height=40)

        IniciarBot = tk.Button(root)
        IniciarBot["borderwidth"] = "4px"
        IniciarBot["bg"] = "#5AF733"
        ft = tkFont.Font(family='Times', size=16)
        IniciarBot["font"] = ft
        IniciarBot["fg"] = "#000000"
        IniciarBot["justify"] = "center"
        IniciarBot["text"] = "Iniciar sesión"
        IniciarBot.place(x=220, y=350, width=160, height=40)
        IniciarBot.bind('<Button-1>', self.IniciarBot_command)
                 
        RegistreseLab = tk.Label(root)
        ft = tkFont.Font(family='Times', size=15)
        RegistreseLab["bg"] = "#fff"
        RegistreseLab["font"] = ft
        RegistreseLab["fg"] = "black"
        RegistreseLab["justify"] = "center"
        RegistreseLab["text"] = "No tiene cuenta aún? --> "
        RegistreseLab.place(x=200, y=450, width=210, height=30)
        
        RegistreseBot = tk.Button(root)
        RegistreseBot["bg"] = "#ffc75c"
        ft = tkFont.Font(family='Times', size=14)
        RegistreseBot["font"] = ft
        RegistreseBot["fg"] = "black"
        RegistreseBot["justify"] = "center"
        RegistreseBot["text"] = "Regístrarse"
        RegistreseBot.place(x=430, y=445, width=120, height=40)
        RegistreseBot.bind('<Button-1>', self.RegistreseBot_command)
        
        
    def IniciarBot_command(self,event):
        print(f"el usuario :{self.CorreoBox.get()} esta iniciando seccion")
        usr = Usuario()
        if (usr.recup_usr_db_mail(self.CorreoBox.get())):
            print(f"el usuario existe {self.CorreoBox.get()}")
            print("usuario encontrado en bases de datos logueando")
        
            if (usr.passw == self.PasswdBox.get()):
                messagebox.showinfo('Info Login', f'{usr}\n{usr.nombre} y su contraseña coinciden en la base de datos. \nLogueando')
                print(usr)

                if (usr.esadmin()):
                    menu_admin = tk.Toplevel()
                    Menu_Admin(menu_admin, usr.id)
                    
                else:
                    menu_usr = tk.Tk()
                    Menu_Usr(menu_usr, usr.id)
                   
            else:
                messagebox.showerror('Password not match', 'Contraseña Incorrecta.')
        else:
            messagebox.showerror('User do not exist', 'El usuario no existe')
            

    def RegistreseBot_command(self,event):
        regist = tk.Tk()
        Registrese(regist)

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
    lblImg = ImageTk.PhotoImage(Image.open(os.path.join(carpeta_Imagenes, "fondoCine.png")).resize((600, 500)))
    etiqueta = Label(image=lblImg)
    etiqueta.pack()
    
    app = App(root)
    root.mainloop()
  
if __name__ == "__main__":
    main()
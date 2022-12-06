import tkinter as tk
import tkinter.font as tkFont
from registrese import Registrese

class App:
    def __init__(self, root):
        #setting title
        root.title("inicio de sesion")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_523=tk.Label(root)
        GLabel_523["bg"] = "#b0b9bc"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_523["font"] = ft
        GLabel_523["fg"] = "#131416"
        GLabel_523["justify"] = "center"
        GLabel_523["text"] = "Inicio de sesión"
        GLabel_523.place(x=200,y=20,width=150,height=50)

        GLabel_697=tk.Label(root)
        GLabel_697["bg"] = "#e47be6"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_697["font"] = ft
        GLabel_697["fg"] = "#333333"
        GLabel_697["justify"] = "center"
        GLabel_697["text"] = "correo"
        GLabel_697.place(x=200,y=110,width=150,height=25)

        GLineEdit_56=tk.Entry(root)
        GLineEdit_56["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_56["font"] = ft
        GLineEdit_56["fg"] = "#352c2c"
        GLineEdit_56["justify"] = "center"
        GLineEdit_56["text"] = "Entry"
        GLineEdit_56.place(x=200,y=150,width=150,height=30)

        GLabel_108=tk.Label(root)
        GLabel_108["bg"] = "#e47be6"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_108["font"] = ft
        GLabel_108["fg"] = "#141314"
        GLabel_108["justify"] = "center"
        GLabel_108["text"] = "contraseña"
        GLabel_108.place(x=200,y=200,width=150,height=30)

        GLineEdit_184=tk.Entry(root)
        GLineEdit_184["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_184["font"] = ft
        GLineEdit_184["fg"] = "#333333"
        GLineEdit_184["justify"] = "center"
        GLineEdit_184["text"] = "Entry"
        GLineEdit_184.place(x=200,y=240,width=150,height=30)

        GLabel_987=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_987["font"] = ft
        GLabel_987["fg"] = "#333333"
        GLabel_987["justify"] = "center"
        GLabel_987["text"] = "Si desea registrarse presione *Registrese*"
        GLabel_987.place(x=160,y=330,width=250,height=50)

        GButton_627=tk.Button(root)
        GButton_627["bg"] = "#656bbc"
        ft = tkFont.Font(family='Times',size=10)
        GButton_627["font"] = ft
        GButton_627["fg"] = "#000000"
        GButton_627["justify"] = "center"
        GButton_627["text"] = "Iniciar sesión"
        GButton_627.place(x=230,y=290,width=90,height=30)
        GButton_627["command"] = self.GButton_627_command

        GButton_265=tk.Button(root)
        GButton_265["bg"] = "#3e7b76"
        ft = tkFont.Font(family='Times',size=10)
        GButton_265["font"] = ft
        GButton_265["fg"] = "#000000"
        GButton_265["justify"] = "center"
        GButton_265["text"] = "Regístrese"
        GButton_265.place(x=170,y=370,width=200,height=35)
        GButton_265["command"] = self.GButton_265_command

    def GButton_627_command(self):
        print("command")


    def GButton_265_command(self):
        pass
        

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

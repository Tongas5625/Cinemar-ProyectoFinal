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

        GLabel_282=tk.Label(root)
        GLabel_282["bg"] = "#eed88f"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_282["font"] = ft
        GLabel_282["fg"] = "#333333"
        GLabel_282["justify"] = "center"
        GLabel_282["text"] = "Nombre"
        GLabel_282.place(x=0,y=90,width=250,height=30)

        GLineEdit_238=tk.Entry(root)
        GLineEdit_238["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_238["font"] = ft
        GLineEdit_238["fg"] = "#333333"
        GLineEdit_238["justify"] = "center"
        GLineEdit_238["text"] = "Entry"
        GLineEdit_238.place(x=280,y=90,width=250,height=30)

        GLabel_69=tk.Label(root)
        GLabel_69["bg"] = "#eed88f"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_69["font"] = ft
        GLabel_69["fg"] = "#333333"
        GLabel_69["justify"] = "center"
        GLabel_69["text"] = "Apellido"
        GLabel_69.place(x=0,y=140,width=250,height=30)

        GLineEdit_51=tk.Entry(root)
        GLineEdit_51["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_51["font"] = ft
        GLineEdit_51["fg"] = "#333333"
        GLineEdit_51["justify"] = "center"
        GLineEdit_51["text"] = "Entry"
        GLineEdit_51.place(x=280,y=140,width=250,height=30)

        GLabel_24=tk.Label(root)
        GLabel_24["bg"] = "#eed88f"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_24["font"] = ft
        GLabel_24["fg"] = "#333333"
        GLabel_24["justify"] = "center"
        GLabel_24["text"] = "DNI"
        GLabel_24.place(x=0,y=190,width=250,height=30)

        GLineEdit_590=tk.Entry(root)
        GLineEdit_590["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_590["font"] = ft
        GLineEdit_590["fg"] = "#333333"
        GLineEdit_590["justify"] = "center"
        GLineEdit_590["text"] = "Entry"
        GLineEdit_590.place(x=280,y=190,width=250,height=30)

        GLabel_28=tk.Label(root)
        GLabel_28["bg"] = "#eed88f"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_28["font"] = ft
        GLabel_28["fg"] = "#333333"
        GLabel_28["justify"] = "center"
        GLabel_28["text"] = "Correo"
        GLabel_28.place(x=0,y=240,width=250,height=30)

        GLineEdit_467=tk.Entry(root)
        GLineEdit_467["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_467["font"] = ft
        GLineEdit_467["fg"] = "#333333"
        GLineEdit_467["justify"] = "center"
        GLineEdit_467["text"] = "Entry"
        GLineEdit_467.place(x=280,y=240,width=250,height=30)

        GLabel_929=tk.Label(root)
        GLabel_929["bg"] = "#eed88f"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_929["font"] = ft
        GLabel_929["fg"] = "#333333"
        GLabel_929["justify"] = "center"
        GLabel_929["text"] = "Contraseña"
        GLabel_929.place(x=0,y=300,width=250,height=30)

        GLineEdit_461=tk.Entry(root)
        GLineEdit_461["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_461["font"] = ft
        GLineEdit_461["fg"] = "#333333"
        GLineEdit_461["justify"] = "center"
        GLineEdit_461["text"] = "Entry"
        GLineEdit_461.place(x=280,y=300,width=250,height=30)

        GButton_295=tk.Button(root)
        GButton_295["bg"] = "#bbafaf"
        ft = tkFont.Font(family='Times',size=10)
        GButton_295["font"] = ft
        GButton_295["fg"] = "#551a1a"
        GButton_295["justify"] = "center"
        GButton_295["text"] = "Registrarse"
        GButton_295.place(x=130,y=410,width=300,height=30)
        GButton_295["command"] = self.GButton_295_command

    def GButton_295_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = Registrese(root)
    root.mainloop()

import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
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

        GButton_648=tk.Button(root)
        GButton_648["bg"] = "#e6d49a"
        ft = tkFont.Font(family='Times',size=10)
        GButton_648["font"] = ft
        GButton_648["fg"] = "#000000"
        GButton_648["justify"] = "center"
        GButton_648["text"] = "CREAR RESERVA"
        GButton_648.place(x=150,y=70,width=250,height=30)
        GButton_648["command"] = self.GButton_648_command

        GButton_224=tk.Button(root)
        GButton_224["bg"] = "#e6d49a"
        ft = tkFont.Font(family='Times',size=10)
        GButton_224["font"] = ft
        GButton_224["fg"] = "#000000"
        GButton_224["justify"] = "center"
        GButton_224["text"] = "MODIFICAR UNA RESERVA"
        GButton_224.place(x=150,y=120,width=250,height=30)
        GButton_224["command"] = self.GButton_224_command

        GButton_583=tk.Button(root)
        GButton_583["bg"] = "#e6d49a"
        ft = tkFont.Font(family='Times',size=10)
        GButton_583["font"] = ft
        GButton_583["fg"] = "#000000"
        GButton_583["justify"] = "center"
        GButton_583["text"] = "VER MIS RESERVAS"
        GButton_583.place(x=150,y=170,width=250,height=30)
        GButton_583["command"] = self.GButton_583_command

        GButton_464=tk.Button(root)
        GButton_464["bg"] = "#e6d49a"
        ft = tkFont.Font(family='Times',size=10)
        GButton_464["font"] = ft
        GButton_464["fg"] = "#000000"
        GButton_464["justify"] = "center"
        GButton_464["text"] = "HISTORICO DE ENTRADAS"
        GButton_464.place(x=150,y=220,width=250,height=30)
        GButton_464["command"] = self.GButton_464_command

    def GButton_648_command(self):
        print("command")


    def GButton_224_command(self):
        print("command")


    def GButton_583_command(self):
        print("command")


    def GButton_464_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

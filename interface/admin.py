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

        GLabel_295=tk.Label(root)
        GLabel_295["bg"] = "#37c1a1"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_295["font"] = ft
        GLabel_295["fg"] = "#333333"
        GLabel_295["justify"] = "center"
        GLabel_295["text"] = "ADMINISTRACION "
        GLabel_295.place(x=40,y=20,width=500,height=40)

        GButton_241=tk.Button(root)
        GButton_241["activebackground"] = "#0b0a0a"
        GButton_241["bg"] = "#9fd5ca"
        ft = tkFont.Font(family='Times',size=10)
        GButton_241["font"] = ft
        GButton_241["fg"] = "#000000"
        GButton_241["justify"] = "center"
        GButton_241["text"] = "Ver reserva de todos los clientes "
        GButton_241.place(x=160,y=80,width=250,height=30)
        GButton_241["command"] = self.GButton_241_command

        GButton_11=tk.Button(root)
        GButton_11["bg"] = "#9fd5ca"
        ft = tkFont.Font(family='Times',size=10)
        GButton_11["font"] = ft
        GButton_11["fg"] = "#000000"
        GButton_11["justify"] = "center"
        GButton_11["text"] = "Ver reserva de un cliente en particular"
        GButton_11.place(x=160,y=130,width=250,height=30)
        GButton_11["command"] = self.GButton_11_command

        GButton_572=tk.Button(root)
        GButton_572["bg"] = "#9fd5ca"
        ft = tkFont.Font(family='Times',size=10)
        GButton_572["font"] = ft
        GButton_572["fg"] = "#000000"
        GButton_572["justify"] = "center"
        GButton_572["text"] = "Crear una sala con la pelicula"
        GButton_572.place(x=160,y=180,width=250,height=30)
        GButton_572["command"] = self.GButton_572_command

        GButton_903=tk.Button(root)
        GButton_903["bg"] = "#9fd5ca"
        ft = tkFont.Font(family='Times',size=10)
        GButton_903["font"] = ft
        GButton_903["fg"] = "#000000"
        GButton_903["justify"] = "center"
        GButton_903["text"] = "Modificar una sala"
        GButton_903.place(x=160,y=230,width=250,height=30)
        GButton_903["command"] = self.GButton_903_command

        GButton_532=tk.Button(root)
        GButton_532["bg"] = "#9fd5ca"
        ft = tkFont.Font(family='Times',size=10)
        GButton_532["font"] = ft
        GButton_532["fg"] = "#000000"
        GButton_532["justify"] = "center"
        GButton_532["text"] = "Eliminar una sala"
        GButton_532.place(x=160,y=280,width=250,height=30)
        GButton_532["command"] = self.GButton_532_command

        GButton_635=tk.Button(root)
        GButton_635["bg"] = "#9fd5ca"
        ft = tkFont.Font(family='Times',size=10)
        GButton_635["font"] = ft
        GButton_635["fg"] = "#000000"
        GButton_635["justify"] = "center"
        GButton_635["text"] = "Modificar descuentos"
        GButton_635.place(x=160,y=330,width=250,height=30)
        GButton_635["command"] = self.GButton_635_command

    def GButton_241_command(self):
        print("command")


    def GButton_11_command(self):
        print("command")


    def GButton_572_command(self):
        print("command")


    def GButton_903_command(self):
        print("command")


    def GButton_532_command(self):
        print("command")


    def GButton_635_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

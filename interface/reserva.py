import tkinter as tk
import tkinter.font as tkFont


class App:
    def __init__(self, root):
        # setting title
        root.title("undefined")
        # setting window size
        width = 600
        height = 500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height,
                                    (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_300 = tk.Label(root)
        GLabel_300["bg"] = "#895e72"
        ft = tkFont.Font(family='Times', size=10)
        GLabel_300["font"] = ft
        GLabel_300["fg"] = "#0c0707"
        GLabel_300["justify"] = "center"
        GLabel_300["text"] = "Cree una reserva"
        GLabel_300.place(x=150, y=20, width=300, height=30)

        GLabel_139 = tk.Label(root)
        GLabel_139["bg"] = "#bf9d9d"
        ft = tkFont.Font(family='Times', size=10)
        GLabel_139["font"] = ft
        GLabel_139["fg"] = "#333333"
        GLabel_139["justify"] = "center"
        GLabel_139["text"] = "Targeta de descuento"
        GLabel_139.place(x=0, y=70, width=250, height=30)

        GLineEdit_850 = tk.Entry(root)
        GLineEdit_850["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        GLineEdit_850["font"] = ft
        GLineEdit_850["fg"] = "#333333"
        GLineEdit_850["justify"] = "center"
        GLineEdit_850["text"] = "Nª tarjeta"
        GLineEdit_850.place(x=270, y=70, width=250, height=30)

        GLabel_210 = tk.Label(root)
        GLabel_210["bg"] = "#bf9d9d"
        ft = tkFont.Font(family='Times', size=10)
        GLabel_210["font"] = ft
        GLabel_210["fg"] = "#333333"
        GLabel_210["justify"] = "center"
        GLabel_210["text"] = "Tipo de sala"
        GLabel_210.place(x=0, y=110, width=250, height=30)

        GListBox_94 = tk.Listbox(root)
        GListBox_94["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        GListBox_94["font"] = ft
        GListBox_94["fg"] = "#333333"
        GListBox_94["justify"] = "center"
        GListBox_94.place(x=270, y=110, width=250, height=30)

        GLabel_414 = tk.Label(root)
        GLabel_414["bg"] = "#bf9d9d"
        ft = tkFont.Font(family='Times', size=10)
        GLabel_414["font"] = ft
        GLabel_414["fg"] = "#333333"
        GLabel_414["justify"] = "center"
        GLabel_414["text"] = "Butacas"
        GLabel_414.place(x=0, y=150, width=250, height=30)

        GLineEdit_848 = tk.Entry(root)
        GLineEdit_848["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        GLineEdit_848["font"] = ft
        GLineEdit_848["fg"] = "#333333"
        GLineEdit_848["justify"] = "center"
        GLineEdit_848["text"] = "Cantidad de bustacas"
        GLineEdit_848.place(x=270, y=150, width=250, height=30)

        GLabel_537 = tk.Label(root)
        GLabel_537["bg"] = "#bf9d9d"
        ft = tkFont.Font(family='Times', size=10)
        GLabel_537["font"] = ft
        GLabel_537["fg"] = "#333333"
        GLabel_537["justify"] = "center"
        GLabel_537["text"] = "Peliculas disponibles"
        GLabel_537.place(x=0, y=190, width=250, height=30)

        GListBox_998 = tk.Listbox(root)
        GListBox_998["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        GListBox_998["font"] = ft
        GListBox_998["fg"] = "#333333"
        GListBox_998["justify"] = "center"
        GListBox_998.place(x=270, y=190, width=250, height=30)

        GLabel_637 = tk.Label(root)
        GLabel_637["bg"] = "#bf9d9d"
        ft = tkFont.Font(family='Times', size=10)
        GLabel_637["font"] = ft
        GLabel_637["fg"] = "#333333"
        GLabel_637["justify"] = "center"
        GLabel_637["text"] = "Horario "
        GLabel_637.place(x=0, y=230, width=250, height=30)

        GListBox_884 = tk.Listbox(root)
        GListBox_884["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        GListBox_884["font"] = ft
        GListBox_884["fg"] = "#333333"
        GListBox_884["justify"] = "center"
        GListBox_884.place(x=270, y=230, width=250, height=30)

        GButton_34 = tk.Button(root)
        GButton_34["bg"] = "#84c89b"
        ft = tkFont.Font(family='Times', size=10)
        GButton_34["font"] = ft
        GButton_34["fg"] = "#060303"
        GButton_34["justify"] = "center"
        GButton_34["text"] = "Crear reserva"
        GButton_34.place(x=210, y=310, width=150, height=35)
        GButton_34["command"] = self.GButton_34_command

    def GButton_34_command(self):
        print("command")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

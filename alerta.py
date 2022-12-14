import tkinter as tk
import tkinter.font as tkFont

class Alerta:
    def __init__(self, root, mensaje):
        self.mensaje=mensaje
        #setting title
        root.title("Alerta")
        #setting window size
        width=200
        height=100
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GMessage_798=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_798["font"] = ft
        GMessage_798["fg"] = "#333333"
        GMessage_798["justify"] = "center"
        GMessage_798["text"] = mensaje              #se pasa el mensaje
        GMessage_798.place(x=0,y=10,width=201,height=79)

if __name__ == "__main__":
    root = tk.Tk()
    app = Alerta(root,"alerta aeropuerto")
    root.mainloop()

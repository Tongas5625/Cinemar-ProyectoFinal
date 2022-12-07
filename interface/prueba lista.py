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
        items = [
        "Python",
        "C",
        "C++",
        "Java"
        ]
        ListBox=tk.Listbox(root)
        ListBox.insert(0, *items)
        ListBox["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        ListBox["font"] = ft
        ListBox["fg"] = "#333333"
        ListBox["justify"] = "center"
        ListBox.place(x=150,y=140,width=80,height=250)
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

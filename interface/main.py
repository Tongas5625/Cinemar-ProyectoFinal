import tkinter as tk
import tkinter.font as tkFont
from inicio_sesion import App
from registrese import Registrese

root = tk.Tk()
app = Registrese(root)
root.mainloop()

root = tk.Tk()
app = App(root)
root.mainloop()

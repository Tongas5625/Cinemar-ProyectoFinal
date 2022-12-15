import tkinter as tk
import tkinter.font as tkFont
from clases.pelicula import Pelicula
from clases.sala import Sala
import sqlite3
from audiyfecha_adm import AudiAdminMenu
class SalayPeli:
    def __init__(self, root,id_usr):
        root.focus()
        root.grab_set()
        self.usrid=id_usr
        self.mensaje=""
        self.director=""
        self.year=""
        self.dur=""
        #setting title
        root.title("Crear Sala y Pelicula")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_460=tk.Label(root)
        GLabel_460["bg"] = "#5fb878"
        ft = tkFont.Font(family='Comics',size=10)
        GLabel_460["font"] = ft
        GLabel_460["fg"] = "#333333"
        GLabel_460["justify"] = "center"
        GLabel_460["text"] = "ADMINISTACION"
        GLabel_460.place(x=50,y=40,width=500,height=40)

        GLabel_931=tk.Label(root)
        GLabel_931["bg"] = "#5fb878"
        ft = tkFont.Font(family='Comics',size=10)
        GLabel_931["font"] = ft
        GLabel_931["fg"] = "#333333"
        GLabel_931["justify"] = "center"
        GLabel_931["text"] = "Crear Sala Y Pelicula"
        GLabel_931.place(x=50,y=440,width=500,height=39)

        self.NumeroSalaBox=tk.Entry(root)
        self.NumeroSalaBox["borderwidth"] = "1px"
        ft = tkFont.Font(family='Comics',size=10)
        self.NumeroSalaBox["font"] = ft
        self.NumeroSalaBox["fg"] = "#333333"
        self.NumeroSalaBox["justify"] = "center"
        self.NumeroSalaBox["text"] = "Numero"
        self.NumeroSalaBox.place(x=160,y=170,width=70,height=25)

        self.AsientosSalaBox=tk.Entry(root)
        self.AsientosSalaBox["borderwidth"] = "1px"
        ft = tkFont.Font(family='Comics',size=10)
        self.AsientosSalaBox["font"] = ft
        self.AsientosSalaBox["fg"] = "#333333"
        self.AsientosSalaBox["justify"] = "center"
        self.AsientosSalaBox["text"] = "Asientos"
        self.AsientosSalaBox.place(x=160,y=270,width=70,height=25)

        GLabel_208=tk.Label(root)
        ft = tkFont.Font(family='Comics',size=10)
        GLabel_208["font"] = ft
        GLabel_208["fg"] = "#333333"
        GLabel_208["justify"] = "center"
        GLabel_208["text"] = "Numero"
        GLabel_208.place(x=80,y=170,width=70,height=25)

        GLabel_413=tk.Label(root)
        ft = tkFont.Font(family='Comics',size=10)
        GLabel_413["font"] = ft
        GLabel_413["fg"] = "#333333"
        GLabel_413["justify"] = "center"
        GLabel_413["text"] = "Tipo"
        GLabel_413.place(x=80,y=220,width=70,height=25)

        GLabel_173=tk.Label(root)
        ft = tkFont.Font(family='Comics',size=10)
        GLabel_173["font"] = ft
        GLabel_173["fg"] = "#333333"
        GLabel_173["justify"] = "center"
        GLabel_173["text"] = "Asientos"
        GLabel_173.place(x=80,y=270,width=70,height=25)

        GLabel_811=tk.Label(root)
        GLabel_811["bg"] = "#1e9fff"
        ft = tkFont.Font(family='Comics',size=10)
        GLabel_811["font"] = ft
        GLabel_811["fg"] = "#333333"
        GLabel_811["justify"] = "center"
        GLabel_811["text"] = "SALA"
        GLabel_811.place(x=50,y=120,width=223,height=30)
        self.tips=["2D","3D"]
        
        self.TipoListBox=tk.Listbox(root,exportselection=False)
        self.TipoListBox.insert(1,*self.tips)
        self.TipoListBox["borderwidth"] = "1px"
        ft = tkFont.Font(family='Comics',size=10)
        self.TipoListBox["font"] = ft
        self.TipoListBox["fg"] = "#333333"
        self.TipoListBox["justify"] = "center"
    #    self.TipoListBox["text"] = "tipo"
        self.TipoListBox.place(x=160,y=220,width=73,height=30)

        GLabel_570=tk.Label(root)
        GLabel_570["bg"] = "#1e9fff"
        ft = tkFont.Font(family='Comics',size=10)
        GLabel_570["font"] = ft
        GLabel_570["fg"] = "#333333"
        GLabel_570["justify"] = "center"
        GLabel_570["text"] = "PELICULA"
        GLabel_570.place(x=270,y=120,width=280,height=30)

        GLabel_40=tk.Label(root)
        ft = tkFont.Font(family='Comics',size=10)
        GLabel_40["font"] = ft
        GLabel_40["fg"] = "#333333"
        GLabel_40["justify"] = "center"
        GLabel_40["text"] = "Titulo"
        GLabel_40.place(x=280,y=170,width=70,height=25)

        GLabel_891=tk.Label(root)
        ft = tkFont.Font(family='Comics',size=10)
        GLabel_891["font"] = ft
        GLabel_891["fg"] = "#333333"
        GLabel_891["justify"] = "center"
        GLabel_891["text"] = "Director"
        GLabel_891.place(x=280,y=220,width=70,height=25)

        GLabel_593=tk.Label(root)
        ft = tkFont.Font(family='Comics',size=10)
        GLabel_593["font"] = ft
        GLabel_593["fg"] = "#333333"
        GLabel_593["justify"] = "center"
        GLabel_593["text"] = "Duracion"
        GLabel_593.place(x=280,y=270,width=70,height=25)

        GLabel_355=tk.Label(root)
        ft = tkFont.Font(family='Comics',size=10)
        GLabel_355["font"] = ft
        GLabel_355["fg"] = "#333333"
        GLabel_355["justify"] = "center"
        GLabel_355.configure(text="Año")
        GLabel_355.place(x=280,y=320,width=70,height=25)
        conexion=sqlite3.connect("movies.db")
        cursor=conexion.cursor()
        cursor.execute("SELECT Nombre FROM pelis;")
        pelist=cursor.fetchall()
        self.listapelis=[]
        for i in range(len(pelist)):
            a=(pelist[i])
            print(a[0])
            if len(a[0])<20:
                self.listapelis.append(a[0])
        self.TituloListbox=tk.Listbox(root,exportselection=False)
        self.TituloListbox.insert(1,*self.listapelis)
        self.TituloListbox["borderwidth"] = "1px"
        ft = tkFont.Font(family='Comics',size=12)
        self.TituloListbox["font"] = ft
        self.TituloListbox["fg"] = "#333333"
        self.TituloListbox["justify"] = "center"
       # self.TituloListbox["text"] = "titulo"
        self.TituloListbox.place(x=350,y=170,width=180,height=30)
                
        self.DirectorLabel=tk.Label(root)
        ft = tkFont.Font(family='Comics',size=10)
        self.DirectorLabel["font"] = ft
        self.DirectorLabel["fg"] = "#333333"
        self.DirectorLabel["justify"] = "center"
        self.DirectorLabel.configure(text=self.director)
        self.DirectorLabel.place(x=350,y=220,width=162,height=30)

        self.DurLabel=tk.Label(root)
        ft = tkFont.Font(family='Comics',size=10)
        self.DurLabel["font"] = ft
        self.DurLabel["fg"] = "#333333"
        self.DurLabel["justify"] = "center"
        self.DurLabel.configure(text=self.dur)
        self.DurLabel.place(x=400,y=270,width=70,height=25)

        self.YearLabel=tk.Label(root)
        ft = tkFont.Font(family='Comics',size=10)
        self.YearLabel["font"] = ft
        self.YearLabel["fg"] = "#333333"
        self.YearLabel["justify"] = "center"
        self.YearLabel.configure(text=self.year)
        self.YearLabel.place(x=400,y=320,width=70,height=25)

        GButton_857=tk.Button(root)
        GButton_857["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Comics',size=10)
        GButton_857["font"] = ft
        GButton_857["fg"] = "#000000"
        GButton_857["justify"] = "center"
        GButton_857["text"] = "CREAR"
        GButton_857.place(x=250,y=380,width=94,height=30)
        GButton_857["command"] = self.GButton_857_command

    def GButton_857_command(self):
        self.indice_peli=self.TituloListbox.curselection()
        print(self.indice_peli)
        peliactual=self.listapelis[self.indice_peli[0]]
        pelitemp=Pelicula()
        pelitemp.recup_peli_db_nombre(peliactual)
        print(pelitemp.duracion) #solo control consola
        self.director=pelitemp.director #actualiza labels
        self.dur=pelitemp.duracion      #si pueden ponerlo en alguna func
        self.year=pelitemp.fechaEstreno #hoy me volo las neuronas
        self.DirectorLabel.configure(text=self.director) #
        self.DurLabel.configure(text=self.dur) #
        self.YearLabel.configure(text=self.year)#
        salatemp=Sala()
        salatemp.numero=self.NumeroSalaBox.get()
        print(self.tips)
        self.indTipo=self.TipoListBox.curselection()
        print(self.indTipo)
        tipoact=self.tips[self.indTipo[0]]
        print(tipoact)
        salatemp.tipo=tipoact
        salatemp.asientos=self.AsientosSalaBox.get()
        salatemp.get_id_db()
        audifecha=tk.Toplevel()
        AudiAdminMenu(audifecha,pelitemp,salatemp)
        
        
       

if __name__ == "__main__":
    root = tk.Tk()
    app = SalayPeli(root,0)
    root.mainloop()
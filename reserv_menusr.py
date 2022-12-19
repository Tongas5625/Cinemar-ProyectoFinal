import sqlite3
from tkinter import *
import tkinter as tk
import tkinter.font as tkFont
from clases.usuarios import Usuario
from salaypeli_adm import SalayPeli
from clases.usuarios import Usuario
from clases.audicion import Audicion
from clases.pelicula import Pelicula
from PIL import ImageTk, ImageColor, Image
import os



class ReservaMenuUsr:
    def __init__(self, root, id_usr):
        root.focus()
        root.grab_set()
        self.usr=Usuario()
        self.usr.recup_usr_db_id(id_usr)        
    #setting title
        root.title("Reserva de Usuario")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        root.wm_attributes("-transparentcolor", 'grey')
        
        self.UsrLab=tk.Label(root)
        ft = tkFont.Font(family='Arial',size=12)
        self.UsrLab["font"] = ft
        self.UsrLab["fg"] = "white"
        self.UsrLab["bg"] = "black"
        self.UsrLab["justify"] = "center"
        self.UsrLab["text"] = "user@mail"
        self.UsrLab.place(x=250,y=10,width=350,height=35)

        self.MailLab=tk.Label(root)
        ft = tkFont.Font(family='Arial',size=12)
        self.MailLab["font"] = ft
        self.MailLab["fg"] = "white"
        self.MailLab["bg"] = "black"
        self.MailLab["justify"] = "center"
        self.MailLab["text"] = "fillmail"
        self.MailLab.place(x=250,y=40,width=359,height=35)

        GLabel_329=tk.Label(root)
        ft = tkFont.Font(family='Arial',size=20)
        GLabel_329["font"] = ft
        GLabel_329["fg"] = "white"
        GLabel_329["bg"] = "black"
        GLabel_329["justify"] = "center"
        GLabel_329["text"] = "Peliculas"
        GLabel_329.place(x=10,y=10,width=261,height=61)
        self.listPelis=self.pelist()
        self.fillPelis=tk.Listbox(root,exportselection=False)
        self.fillPelis.insert(1,*self.listPelis)
       #self.fillPelis=tk.Listbox(root)
        self.fillPelis["border"]= "1px"
        ft = tkFont.Font(family='Arial',size=14)
        self.fillPelis["font"] = ft
        self.fillPelis["fg"] = "white"
        self.fillPelis["bg"] = "black"
        self.fillPelis["justify"] = "center"
        self.fillPelis.place(x=20,y=80,width=242,height=30)

        PeliCheck=tk.Checkbutton(root)
        ft = tkFont.Font(family='Arial',size=12)
        PeliCheck["font"] = ft
        PeliCheck["fg"] = "white"
        PeliCheck["bg"] = "black"
        PeliCheck["justify"] = "center"
        PeliCheck["text"] = "Elegir"
        PeliCheck.place(x=270,y=80,width=85,height=33)
        PeliCheck["offvalue"] = "0"
        PeliCheck["onvalue"] = "1"
        PeliCheck["command"] = self.PeliCheck_command

        GLabel_83=tk.Label(root)
        ft = tkFont.Font(family='Arial',size=10)
        GLabel_83["font"] = ft
        GLabel_83["fg"] = "white"
        GLabel_83["bg"] = "black"
        GLabel_83["justify"] = "center"
        GLabel_83["text"] = "Titulo   :"
        GLabel_83.place(x=0,y=140,width=102,height=30)

        GLabel_449=tk.Label(root)
        ft = tkFont.Font(family='Arial',size=10)
        GLabel_449["font"] = ft
        GLabel_449["fg"] = "white"
        GLabel_449["bg"] = "black"
        GLabel_449["justify"] = "center"
        GLabel_449["text"] = "Director   :"
        GLabel_449.place(x=0,y=180,width=102,height=30)

        GLabel_541=tk.Label(root)
        ft = tkFont.Font(family='Arial',size=10)
        GLabel_541["font"] = ft
        GLabel_541["fg"] = "white"
        GLabel_541["bg"] = "black"
        GLabel_541["justify"] = "center"
        GLabel_541["text"] = "Año  :"
        GLabel_541.place(x=0,y=220,width=102,height=30)

        GLabel_217=tk.Label(root)
        ft = tkFont.Font(family='Arial',size=10)
        GLabel_217["font"] = ft
        GLabel_217["fg"] = "white"
        GLabel_217["bg"] = "black"
        GLabel_217["justify"] = "center"
        GLabel_217["text"] = "Genero  :"
        GLabel_217.place(x=0,y=260,width=100,height=30)

        self.FillTitulo=tk.Label(root)
        ft = tkFont.Font(family='Arial',size=10)
        self.FillTitulo["font"] = ft
        self.FillTitulo["fg"] = "white"
        self.FillTitulo["bg"] = "black"
        self.FillTitulo["justify"] = "center"
        self.FillTitulo["text"] = "filltitulo"
        self.FillTitulo.place(x=100,y=140,width=135,height=30)

        self.FillDirector=tk.Label(root)
        ft = tkFont.Font(family='Arial',size=10)
        self.FillDirector["font"] = ft
        self.FillDirector["fg"] = "white"
        self.FillDirector["bg"] = "black"
        self.FillDirector["justify"] = "center"
        self.FillDirector["text"] = "filldirector"
        self.FillDirector.place(x=100,y=180,width=130,height=30)

        self.FillYear=tk.Label(root)
        ft = tkFont.Font(family='Arial',size=10)
        self.FillYear["font"] = ft
        self.FillYear["fg"] = "white"
        self.FillYear["bg"] = "black"
        self.FillYear["justify"] = "center"
        self.FillYear["text"] = "fillaño"
        self.FillYear.place(x=100,y=220,width=130,height=30)

        self.FillGenero=tk.Label(root)
        ft = tkFont.Font(family='Arial',size=10)
        self.FillGenero["font"] = ft
        self.FillGenero["fg"] = "white"
        self.FillGenero["bg"] = "black"
        self.FillGenero["justify"] = "center"
        self.FillGenero["text"] = "fillgenero"
        self.FillGenero.place(x=100,y=260,width=130,height=30)

        GListBox_769=tk.Listbox(root)
        GListBox_769["borderwidth"] = "1px"
        ft = tkFont.Font(family='Arial',size=10)
        GListBox_769["font"] = ft
        GListBox_769["fg"] = "white"
        GListBox_769["bg"] = "black"
        GListBox_769["justify"] = "center"
        GListBox_769.place(x=375,y=150,width=101,height=30)

        GLabel_666=tk.Label(root)
        ft = tkFont.Font(family='Arial',size=10)
        GLabel_666["font"] = ft
        GLabel_666["fg"] = "white"
        GLabel_666["bg"] = "black"
        GLabel_666["justify"] = "center"
        GLabel_666["text"] = "Fecha"
        GLabel_666.place(x=280,y=150,width=92,height=31)

        GLabel_255=tk.Label(root)
        ft = tkFont.Font(family='Arial',size=10)
        GLabel_255["font"] = ft
        GLabel_255["fg"] = "white"
        GLabel_255["bg"] = "black"
        GLabel_255["justify"] = "center"
        GLabel_255["text"] = "Horarios"
        GLabel_255.place(x=290,y=210,width=70,height=31)

        GListBox_156=tk.Listbox(root)
        GListBox_156["borderwidth"] = "1px"
        ft = tkFont.Font(family='Arial',size=10)
        GListBox_156["font"] = ft
        GListBox_156["fg"] = "white"
        GListBox_156["bg"] = "black"
        GListBox_156["justify"] = "center"
        GListBox_156.place(x=370,y=210,width=101,height=31)

        GCheckBox_445=tk.Checkbutton(root)
        ft = tkFont.Font(family='Arial',size=10)
        GCheckBox_445["font"] = ft
        GCheckBox_445["fg"] = "white"
        GCheckBox_445["bg"] = "black"
        GCheckBox_445["justify"] = "center"
        GCheckBox_445["text"] = "FechaCheck"
        GCheckBox_445.place(x=370,y=180,width=85,height=31)
        GCheckBox_445["offvalue"] = "0"
        GCheckBox_445["onvalue"] = "1"
        GCheckBox_445["command"] = self.GCheckBox_445_command

        GCheckBox_747=tk.Checkbutton(root)
        ft = tkFont.Font(family='Arial',size=10)
        GCheckBox_747["font"] = ft
        GCheckBox_747["fg"] = "white"
        GCheckBox_747["bg"] = "black"
        GCheckBox_747["justify"] = "center"
        GCheckBox_747["text"] = "HorarioCheck"
        GCheckBox_747.place(x=370,y=240,width=85,height=31)
        GCheckBox_747["offvalue"] = "0"
        GCheckBox_747["onvalue"] = "1"
        GCheckBox_747["command"] = self.GCheckBox_747_command

        GListBox_419=tk.Listbox(root)
        GListBox_419["borderwidth"] = "1px"
        ft = tkFont.Font(family='Arial',size=10)
        GListBox_419["font"] = ft
        GListBox_419["fg"] = "white"
        GListBox_419["bg"] = "black"
        GListBox_419["justify"] = "center"
        GListBox_419.place(x=370,y=280,width=101,height=31)

        GLabel_301=tk.Label(root)
        ft = tkFont.Font(family='Arial',size=10)
        GLabel_301["font"] = ft
        GLabel_301["fg"] = "white"
        GLabel_301["bg"] = "black"
        GLabel_301["justify"] = "center"
        GLabel_301["text"] = "Butaca"
        GLabel_301.place(x=290,y=280,width=75,height=36)

        GCheckBox_127=tk.Checkbutton(root)
        ft = tkFont.Font(family='Arial',size=10)
        GCheckBox_127["font"] = ft
        GCheckBox_127["fg"] = "white"
        GCheckBox_127["bg"] = "black"
        GCheckBox_127["justify"] = "center"
        GCheckBox_127["text"] = "ButacaCheck"
        GCheckBox_127.place(x=370,y=310,width=85,height=33)
        GCheckBox_127["offvalue"] = "0"
        GCheckBox_127["onvalue"] = "1"
        GCheckBox_127["command"] = self.GCheckBox_127_command

        GButton_780=tk.Button(root)
        GButton_780["bg"] = "black"
        ft = tkFont.Font(family='Arial',size=10)
        GButton_780["font"] = ft
        GButton_780["fg"] = "white"
        GButton_780["justify"] = "center"
        GButton_780["text"] = "Button"
        GButton_780.place(x=210,y=420,width=137,height=38)
        GButton_780["command"] = self.GButton_780_command

        GListBox_14=tk.Listbox(root)
        GListBox_14["borderwidth"] = "1px"
        ft = tkFont.Font(family='Arial',size=10)
        GListBox_14["font"] = ft
        GListBox_14["fg"] = "white"
        GListBox_14["bg"] = "black"
        GListBox_14["justify"] = "center"
        GListBox_14.place(x=300,y=350,width=57,height=40)

        GLabel_828=tk.Label(root)
        ft = tkFont.Font(family='Arial',size=10)
        GLabel_828["font"] = ft
        GLabel_828["fg"] = "white"
        GLabel_828["bg"] = "black"
        GLabel_828["justify"] = "center"
        GLabel_828["text"] = "Entradas"
        GLabel_828["bg"] = "black"
        GLabel_828.place(x=200,y=350,width=91,height=40)

    def pelist(self):#rellena la una lista con los nombres de las pelis de audiciones
        conexion=sqlite3.connect("audiciones.db")#
        conexion2=sqlite3.connect("movies.db")
        cursor2=conexion2.cursor()
        cursor=conexion.cursor()#
        cursor.execute("SELECT Pelicula FROM audiciones;")#agarra id de pelis de audi...db
      # pelistid[]
        pelistid=cursor.fetchall()#
        cursor.close()
        listapelis=[]#
        for i in pelistid:#
            print (i[0])
            cursor2.execute(f"SELECT Nombre FROM pelis WHERE id={i[0]}")#agarra los nombre de las pelis de audi
            temp=cursor2.fetchone()
            listapelis.append(temp[0])#llena la lista para mostrar en lisbox
        return listapelis    #devuelve
    
    def pelistinfo(self):#rellena los labels con la info de las pelicula selecionada
        indice_peli=self.fillPelis.curselection()
        print(indice_peli)
        if (indice_peli):
            peliactual=self.listPelis[indice_peli[0]]
            pelitemp=Pelicula()
            pelitemp.recup_peli_db_nombre(peliactual)
            print(pelitemp.duracion) #solo control consola
            self.FillDirector.configure(text=pelitemp.director) #
            self.FillTitulo.configure(text=pelitemp.nombre) #
            self.FillYear.configure(text=pelitemp.fechaEstreno)#
            self.FillGenero.configure(text=pelitemp.clasificacion)
        else:
            print("indice vacio")
    def PeliCheck_command(self):
        self.pelistinfo()
        print("commando")


    def GCheckBox_445_command(self):
        print("command")


    def GCheckBox_747_command(self):
        print("command")


    def GCheckBox_127_command(self):
        print("command")


    def GButton_780_command(self):
        print("command")
        
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
    icoImg = ImageTk.PhotoImage(Image.open(os.path.join(carpeta_Imagenes, "fondoAdmin2.png")).resize((600, 500)))
    etiqueta = Label(image=icoImg)
    etiqueta.pack()
    app=ReservaMenuUsr(root,1)
    root.mainloop()


if __name__ == "__main__":
    main()
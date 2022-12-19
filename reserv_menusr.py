import sqlite3
from tkinter import *
import tkinter as tk
import tkinter.font as tkFont
from clases.usuarios import Usuario
from salaypeli_adm import SalayPeli
from clases.usuarios import Usuario
from clases.audicion import Audicion
from clases.pelicula import Pelicula
from clases.butaca import Butaca
from clases.reserva import Reserva
from PIL import ImageTk, ImageColor, Image
import os



class ReservaMenuUsr:
    def __init__(self, root, id_usr):
        self.idpeli=0# se usaran para pasar datos de metodo a metodo
        self.idaudi=0#
        self.idsala=0
        self.fechaselect=""#
        self.butacaselect=0
        root.configure(bg='black')
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
        self.UsrLab["text"] = f"{self.usr.nombre}"
        self.UsrLab.place(x=250,y=10,width=350,height=35)

        self.MailLab=tk.Label(root)
        ft = tkFont.Font(family='Arial',size=12)
        self.MailLab["font"] = ft
        self.MailLab["fg"] = "white"
        self.MailLab["bg"] = "black"
        self.MailLab["justify"] = "center"
        self.MailLab["text"] = f"{self.usr.mail}"
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

        self.audiFechaLBox=tk.Listbox(root)
        self.audiFechaLBox["borderwidth"] = "1px"
        ft = tkFont.Font(family='Arial',size=10)
        self.audiFechaLBox["font"] = ft
        self.audiFechaLBox["fg"] = "white"
        self.audiFechaLBox["bg"] = "black"
        self.audiFechaLBox["justify"] = "center"
        self.audiFechaLBox.place(x=375,y=150,width=101,height=30)

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
        
       
        self.audiHorarioListB=tk.Listbox(root,exportselection=False)
        self.audiHorarioListB["borderwidth"] = "1px"
        ft = tkFont.Font(family='Arial',size=10)
        self.audiHorarioListB["font"] = ft
        self.audiHorarioListB["fg"] = "white"
        self.audiHorarioListB["bg"] = "black"
        self.audiHorarioListB["justify"] = "center"
        self.audiHorarioListB.place(x=370,y=210,width=101,height=31)

        self.FechaCheck=tk.Checkbutton(root)
        ft = tkFont.Font(family='Arial',size=10)
        self.FechaCheck["font"] = ft
        self.FechaCheck["fg"] = "white"
        self.FechaCheck["bg"] = "black"
        self.FechaCheck["justify"] = "center"
        self.FechaCheck["text"] = "FechaCheck"
        self.FechaCheck.place(x=370,y=180,width=85,height=31)
        self.FechaCheck["offvalue"] = "0"
        self.FechaCheck["onvalue"] = "1"
        self.FechaCheck["command"] = self.FechaCheck_command

        self.HorarioCheck=tk.Checkbutton(root)
        ft = tkFont.Font(family='Arial',size=10)
        self.HorarioCheck["font"] = ft
        self.HorarioCheck["fg"] = "white"
        self.HorarioCheck["bg"] = "black"
        self.HorarioCheck["justify"] = "center"
        self.HorarioCheck["text"] = "HorarioCheck"
        self.HorarioCheck.place(x=370,y=240,width=85,height=31)
        self.HorarioCheck["offvalue"] = "0"
        self.HorarioCheck["onvalue"] = "1"
        self.HorarioCheck["command"] = self.HorarioCheck_command

        self.ButacasListBox=tk.Listbox(root,exportselection=False)
        self.ButacasListBox["borderwidth"] = "1px"
        ft = tkFont.Font(family='Arial',size=10)
        self.ButacasListBox["font"] = ft
        self.ButacasListBox["fg"] = "white"
        self.ButacasListBox["bg"] = "black"
        self.ButacasListBox["justify"] = "center"
        self.ButacasListBox.place(x=370,y=280,width=101,height=31)

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
        GButton_780["text"] = "Reservar"
        GButton_780.place(x=210,y=420,width=137,height=38)
        GButton_780["command"] = self.GButton_780_command

        self.EntradasListBox=tk.Listbox(root)
        self.EntradasListBox["borderwidth"] = "1px"
        ft = tkFont.Font(family='Arial',size=10)
        self.EntradasListBox["font"] = ft
        self.EntradasListBox["fg"] = "white"
        self.EntradasListBox["bg"] = "black"
        self.EntradasListBox["justify"] = "center"
        self.EntradasListBox.place(x=300,y=350,width=57,height=40)

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
            self.idpeli=pelitemp.id
            return pelitemp.id        
        else:
            print("indice vacio")
    
    def fillaudinfofecha(self):
        audi=Audicion()
        idlist=audi.recup_audi_pelisid(self.idpeli) # recibe un lista de tuplas de audicines con la misma peli
        print(idlist)
        if idlist:
            for i in idlist:
                print(i[0])
                audi.recup_audi_id(i[0])
                self.audiFechaLBox.insert(tk.END,(audi.fecha))  
    
    def PeliCheck_command(self):
        self.pelistinfo()
        self.fillaudinfofecha()
        print("commando")


    def FechaCheck_command(self):
        indice_fecha=self.audiFechaLBox.curselection()
        print(indice_fecha)
        if (indice_fecha):
            fechaselect=self.audiFechaLBox.get(indice_fecha[0])
            self.fechaselect=fechaselect
            auditemp=Audicion()
            listhorarios=auditemp.horarios_audiypeli(self.idpeli,fechaselect) #devolvera una lista de horarios para esa fecha y esa peli
            print (listhorarios)
            if listhorarios:
                for i in listhorarios:
                    print(i[0])
                    self.audiHorarioListB.insert(tk.END,(i[0])) #relleno listbox de horarios disponible para esa fecha y peli
                 
        else:
            print("indice vacio")
        print("command")


    def HorarioCheck_command(self):
        indice_horario=self.audiHorarioListB.curselection()
        print(indice_horario)
        if (indice_horario):
            horaselect=self.audiHorarioListB.get(indice_horario[0])
            auditemp=Audicion()
            auditemp.pelihorayfecha(self.idpeli,horaselect,self.fechaselect) #obtendremos id de audi a por el horario fecha y peli
            self.idaudi=auditemp.id
            print (auditemp.id)
            butacatemp=Butaca()
            listbutacas=butacatemp.getlibres(auditemp.id) #recibiremos butacas libres para esa audicion concreta
            if listbutacas:
                for i in listbutacas:
                    print(i[0])
                    self.ButacasListBox.insert(tk.END,(i[0])) #relleno listbox butacas libres para esa audicion
        else:
            print("indice vacio")
        

    def GCheckBox_127_command(self):#este es el butaca check
        indice_butaca=self.ButacasListBox.curselection()
        print(indice_butaca)
        if (indice_butaca):
            butacaselect=self.ButacasListBox.get(indice_butaca[0])
            auditemp=Audicion()
            auditemp.recup_audi_id(self.idaudi)
            butemp=Butaca()
            butemp.ocupar(self.idaudi,auditemp.sala,butacaselect)
            butemp.modificar()
            self.butacaselect=butemp.id
                
        print("command")


    def GButton_780_command(self):#este es para crear ya la reserva
        print("command")
        reserv=Reserva()
        reserv.audicion=self.idaudi
        reserv.butaca=self.butacaselect
        reserv.entradas=1
        reserv.usuario=self.usr.mail
        reserv.grabar_datos()
        
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
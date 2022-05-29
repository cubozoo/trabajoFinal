from turtle import color
import mutagen
from mutagen.mp3 import MP3
from tkinter import * 
import tkinter as tk
from tkinter import ttk
import pygame
import os

 



ventana = tk.Tk()
ventana.geometry('1200x800')
ventana.minsize(1200,800)
ventana.maxsize(1200,800)
ventana.iconphoto(False, tk.PhotoImage(file='C:/Users/Usuario/Desktop/ProyectoTFG/Logo.png'))
ventana.title('MuWusica')


listasRepro = []
listasRepro.append("Selecciona la lista") 
listasRepro.append("Lista 1")
    



#Funcion que muestra toda la informacion de la cancion actual   
def infoCancion():
    global longitud, posActual
    
    cancionActual=apartadoCanciones.get(tk.ACTIVE)
    
    posActual=pygame.mixer.music.get_pos()/1000 #Indica la posicion de la cancion en milisegundos, se divide entre 1000 para sacar los segundos

    rutaCancion= mutagen.File(f'C:/Users/Usuario/Desktop/trabajoFinal/cansiones/{cancionActual}') #Ruta de la cancion actual
    
    longitud=rutaCancion.info.length #Esta funcion permite obtener el valor de la longitud de la cancion actual
    
    lineaTiempo.set(posActual)

    lineaTiempo.after(1000,infoCancion)
    

def slide(x):
    sliderLabel.config(text=f'{int(lineaTiempo.get())} of {int(longitud)}') #Muestra los segundos de la cancion




####@~#@~@#~@~#@#@~@#~@#~ Seleccionar elementos en una lista y añadirlos a otra -> https://es.stackoverflow.com/questions/197852/tkinter-tclerror-bad-listbox-index-must-be-active-anchor-end-x-y-or-a

 

class funcionesBotones():
    global estado
    estado=""
    def btnPrueba():
            global comboListas
            listaSeleccion=comboListas.get()
            if(listaSeleccion!="Selecciona la lista"):
                print(listaSeleccion)

    def btnInsertar():       
        index=apartadoCanciones.curselection()
        value = apartadoCanciones.get(index[0])
        print(value)

        listaSeleccion=comboListas.get()
        if(listaSeleccion!="Selecciona la lista"):
            listasReproduccion.insert(tk.END, value)           


    def btnPlay():#Funcion para reproducir la cancion
        infoCancion()
        if(estado=="pause"):
            pygame.mixer.music.unpause()#Seguira la cancion por donde estaba
        else:
            pygame.mixer.music.load(apartadoCanciones.get(tk.ACTIVE)) #Carga la cancion que tiene seleccionada en ese momento
            pygame.mixer.music.play() #Reproduce la cancion

    
        slider_position = int(longitud)#Guardamos en una variable esa longitud
        lineaTiempo.config(to=slider_position)
        lineaTiempo.set(0)

        
    
    def btnPause():#Funcion para pausar la cancion
        global estado
        pygame.mixer.music.pause()#Pausa la cancion, haciendo que se cuando le volvamos a dar a Play continue desde ese punto
        estado="pause"

    def btnStop():#Funcion para parar la cancion
        global estado
        pygame.mixer.music.stop()#Para la cancion, haciendo que se cuando le volvamos a dar a Play se reinicie o poder cambiar de cancion
        apartadoCanciones.selection_clear(tk.ACTIVE)
        estado=""

    def btnPre():#Funcion para reproducir la cancion anterior
        infoCancion()
        cancionActual=apartadoCanciones.index(tk.ACTIVE) #Indica la posicion actual de la cancion activa
        #Si es la primera cancion
        if(cancionActual==0):
            seleccion=apartadoCanciones.curselection() #Indica la cancion que esta seleccionada en ese momento como tupla
            ultima=apartadoCanciones.size()-1 #Le indicamos la ultima cancion de la lista
            PreSong=seleccion[0]+ultima #Decimos que la anterior cancion a la primera es la ultima, creando asi un bucle

            pygame.mixer.music.load(apartadoCanciones.get(PreSong))
            pygame.mixer.music.play()

            apartadoCanciones.select_clear(0, END) #Quitamos la seleccion de la primera cancion
            apartadoCanciones.activate(PreSong)    #Activamos la anterior cancion
            apartadoCanciones.select_set(PreSong)

        #Si no es la primera cancion
        if(cancionActual!=0):
            seleccion = apartadoCanciones.curselection()
            PreSong=seleccion[0]-1

            pygame.mixer.music.load(apartadoCanciones.get(PreSong))
            pygame.mixer.music.play()

            apartadoCanciones.select_clear(0, END)
            apartadoCanciones.activate(PreSong)
            apartadoCanciones.select_set(PreSong)

        slider_position = int(longitud)#Guardamos en una variable esa longitud
        lineaTiempo.config(to=slider_position)
        lineaTiempo.set(0)

    def btnNext():#Funcion para reproducir la siguiente cancion
        infoCancion()
        cancionActual=apartadoCanciones.index(tk.ACTIVE) #Indica la posicion actual de la cancion activa
        numCanciones=apartadoCanciones.size()-1 #Le indicamos la ultima cancion de la lista
        if(cancionActual==numCanciones):
            pygame.mixer.music.load(apartadoCanciones.get(0))
            pygame.mixer.music.play()

            apartadoCanciones.select_clear(0, END) #Quitamos la seleccion de la primera cancion
            apartadoCanciones.activate(0)    #Activamos la anterior cancion
            apartadoCanciones.select_set(0)

        #Si no es la primera cancion
        if(cancionActual!=numCanciones):
            seleccion = apartadoCanciones.curselection()
            NextSong=seleccion[0]+1

            pygame.mixer.music.load(apartadoCanciones.get(NextSong))
            pygame.mixer.music.play()

            apartadoCanciones.select_clear(0, END)
            apartadoCanciones.activate(NextSong)
            apartadoCanciones.select_set(NextSong)
        
        slider_position = int(longitud)#Guardamos en una variable esa longitud
        lineaTiempo.config(to=slider_position)
        lineaTiempo.set(0)
        

##################################Creacion de menu###################################
menubar = Menu(ventana) #Creamos Barra de Menu 

menuArchivo = Menu(menubar, tearoff=0) #tearoff = Separa menus con una linea de puntos
menuArchivo.add_command(label="Añadir Cancion") #Añade un submenu con ese nombre

menuArchivo.add_separator() #Crea una linea de separacion

menuArchivo.add_command(label="Nueva Lista")
menuArchivo.add_command(label="Exportar Lista") #.asksaveasfilename
menuArchivo.add_command(label="Importar Lista") #.askopenfilename
menuArchivo.add_command(label="Eliminar Lista") 

menubar.add_cascade(label="Archivo", menu=menuArchivo) #Añade el menu a la barra de menu

menuUser = Menu(menubar, tearoff=0)
menuUser.add_command(label="Crear Usuario")
menuUser.add_command(label="Modificar Usuario")
menuUser.add_command(label="Eliminar Usuario")

menubar.add_cascade(label="Usuarios", menu=menuUser)


menuConf = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Configuracion", menu=menuConf)

menuHelp = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Ayuda", menu=menuHelp)

ventana.config(menu=menubar) #Añade el menu a la ventana


#-------------------------------------------------------------------------------------------------------

############################### APARTADOS #################################

#--GRUPOS--
lGrupos = tk.Label(text= "Grupos", font="Terminal 12", bg="black", fg="orange", relief=RAISED)
listaGrupos = tk.Listbox(ventana, font="Candara 12", bg="black", fg="white", selectmode=tk.SINGLE)

lGrupos.place(relx=0, rely=0, relwidth=0.25, relheight=0.05)
listaGrupos.place(relx=0, rely=0.05, relwidth=0.25, relheight=0.65)

#relx=Desplazamiento horizontal hacia la derecha entre 0.0 y 1.0. 
#rely=Desplazamiento vertical hacia abajo entre 0.0 y 1.0.


#--DISCOS--
lDiscos = tk.Label(text= "Discos", font="Terminal 12", bg="black", fg="orange", relief=RAISED)
listaDiscos = tk.Listbox(ventana, font="Candara 12", bg="black", fg="white", selectmode=tk.SINGLE)

lDiscos.place(relx=0.25, rely=0, relwidth=0.25, relheight=0.05)
listaDiscos.place(relx=0.25, rely=0.05, relwidth=0.25, relheight=0.65)


#--CANCIONES--

lCanciones = tk.Label(text= "Canciones", font="Terminal 12", bg="black", fg="orange", relief=RAISED)
apartadoCanciones = tk.Listbox(ventana, font="Candara 12", bg="black", fg="white", selectmode=tk.SINGLE)

lCanciones.place(relx=0.5, rely=0, relwidth=0.25, relheight=0.05)
apartadoCanciones.place(relx=0.5, rely=0.05, relwidth=0.25, relheight=0.65)

#--LISTAS DE REPRODUCCION--LightSteelBlue4 #237F90

lListas = tk.Label(text= "Listas de Reproducción", font="Terminal 12", bg="black", fg="orange", relief=RAISED)
listasReproduccion = tk.Listbox(ventana, font="Candara 12", bg="black", fg="white", selectmode=tk.SINGLE)

lListas.place(relx=0.75, rely=0, relwidth=0.25, relheight=0.05)
listasReproduccion.place(relx=0.75, rely=0.1, relwidth=0.25, relheight=0.65)

style = ttk.Style()    #SE SUPONE QUE CAMBIA EL ESTILO DEL COMBOBOX 
style.theme_use('clam')
style.configure("TCombobox", fieldbackground= "#237F90")


############################### COMBOBOX #################################
comboListas = ttk.Combobox(state="readonly",  values=listasRepro, font="gadugi", style="TCombobox")
comboListas.place(relx=0.75, rely=0.05, relwidth=0.25, relheight=0.05)
comboListas.current(0)




#--------------------------------------------------------------------------------------------------------------------------------------------


############################### IMAGEN CANCION #################################

imagenCancion = tk.Label(bg="black", relief=RAISED)
imagenCancion.place(relx=0, rely=0.7, relwidth=0.25, relheight=0.3)




############################### ZONA FUNCIONES #################################

zonaReproduccion = tk.Label(bg="black", relief=RAISED)
zonaReproduccion.place(relx=0.25, rely=0.7, relwidth=0.5, relheight=0.3)

#Boton que selecciona la cancion anterior
botonAnt = tk.Button(ventana, width=3, height=1, font="Helvetica 20 bold", text="Ι◀", bg="orange", fg="white", command=funcionesBotones.btnPre)
botonAnt.place(relx=0.32, rely=0.75)

#Boton que pausa la cancion actual
botonPause = tk.Button(ventana, width=3, height=1, font="Helvetica 20 bold", text="ΙΙ", bg='blue', fg="white", command=funcionesBotones.btnPause)
botonPause.place(relx=0.4, rely=0.75)

#Boton que reproduce la cancion seleccionada
botonPlay = tk.Button(ventana, width=3, height=1, font="Helvetica 20 bold", text="⫸", bg='green', fg="white", command=funcionesBotones.btnPlay)
botonPlay.place(relx=0.48, rely=0.75)

#Boton que para la cancion actual 
botonStop = tk.Button(ventana, width=3, height=1, font="Helvetica 20 bold", text="■", bg="red", fg="white", command=funcionesBotones.btnStop)
botonStop.place(relx=0.56, rely=0.75)

#Boton que selecciona la cancion posterior
botonNext = tk.Button(ventana, width=3, height=1, font="Helvetica 20 bold", text="▶Ι", bg='orange', fg="white", command=funcionesBotones.btnNext)
botonNext.place(relx=0.64, rely=0.75)

#Boton que inserta en una lista la cancion seleccionadas
botonInsertar = tk.Button(ventana, width=3, height=1, font="Helvetica 20 bold", text="insert", bg='pink', fg="black", command=funcionesBotones.btnInsertar)
botonInsertar.place(relx=0.10, rely=0.75)


lineaTiempo = tk.Scale(ventana, bg="orange", troughcolor="orange", from_=0, to=100, orient=HORIZONTAL, length=350, showvalue=0, command=slide)
lineaTiempo.place(relx=0.35, rely=0.9)

sliderLabel = Label(ventana, text=0)
sliderLabel.place(relx=0.485, rely=0.85)








############################### ZONA VOLUMEN (?) #################################

otraZona = tk.Label(text="Usuario000",font="Helvetica 12 bold", bg="black", fg="white", relief=RAISED)
otraZona.place(relx=0.75, rely=0.7, relwidth=0.25, relheight=0.3)

if __name__ == '__main__':
    pygame.init()
    pygame.mixer.init()

    directorio= "cansiones" #Selecciona el directorio"
    os.chdir(directorio) #Cambia a ese directorio
    canciones = os.listdir() #Lista el contenido de ese directorio

    for x in canciones: #Bucle para introducir las canciones en la lista de reproduccion
        if(x.endswith(".mp3")): #Filtra por la extension .mp3
            apartadoCanciones.insert(tk.END, x)
            #pygame.mixer.music.queue(x)


    ventana.mainloop()
    
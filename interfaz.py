from tkinter import * 
import tkinter as tk
from tkinter import ttk
import pygame
import os

 


ventana = tk.Tk()
ventana.geometry('1200x800')
ventana.minsize(1200,800)
ventana.maxsize(1200,800)
ventana.title('MuWusica')

listasRepro = []
listasRepro.append("Selecciona la lista") 
listasRepro.append("Lista 1")
    

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
lGrupos = tk.Label(text= "Grupos", font="Helvetica 12 bold", bg="LightSteelBlue4", relief=RAISED)
listaGrupos = tk.Listbox(ventana, font="Helvetica 12 bold", bg="#237F90", fg="white", selectmode=tk.SINGLE)

lGrupos.place(relx=0, rely=0, relwidth=0.25, relheight=0.05)
listaGrupos.place(relx=0, rely=0.05, relwidth=0.25, relheight=0.65)

#relx=Desplazamiento horizontal hacia la derecha entre 0.0 y 1.0. 
#rely=Desplazamiento vertical hacia abajo entre 0.0 y 1.0.


#--DISCOS--
lDiscos = tk.Label(text= "Discos", font="Helvetica 12 bold", bg="LightSteelBlue4", relief=RAISED)
listaDiscos = tk.Listbox(ventana, font="Helvetica 12 bold", bg="#237F90", fg="white", selectmode=tk.SINGLE)

lDiscos.place(relx=0.25, rely=0, relwidth=0.25, relheight=0.05)
listaDiscos.place(relx=0.25, rely=0.05, relwidth=0.25, relheight=0.65)


#--CANCIONES--

lCanciones = tk.Label(text= "Canciones", font="Helvetica 12 bold", bg="LightSteelBlue4", relief=RAISED)
apartadoCanciones = tk.Listbox(ventana, font="Helvetica 12 bold", bg="#237F90", fg="white", selectmode=tk.SINGLE)

lCanciones.place(relx=0.5, rely=0, relwidth=0.25, relheight=0.05)
apartadoCanciones.place(relx=0.5, rely=0.05, relwidth=0.25, relheight=0.65)

#--LISTAS DE REPRODUCCION--

lListas = tk.Label(text= "Listas de Reproducción", font="Helvetica 12 bold", bg="LightSteelBlue4", relief=RAISED)
listasReproduccion = tk.Listbox(ventana, font="Helvetica 12 bold", bg="#237F90", fg="white", selectmode=tk.SINGLE)

lListas.place(relx=0.75, rely=0, relwidth=0.25, relheight=0.05)
listasReproduccion.place(relx=0.75, rely=0.1, relwidth=0.25, relheight=0.65)

# style = ttk.Style()    #SE SUPONE QUE CAMBIA EL ESTILO DEL COMBOBOX 
# style.theme_use('clam')
# style.configure("TCombobox", fieldbackground= "#237F90")


############################### COMBOBOX #################################
comboListas = ttk.Combobox(state="readonly",  values=listasRepro, font="gadugi")
comboListas.place(relx=0.75, rely=0.05, relwidth=0.25, relheight=0.05)
comboListas.current(0)




#--------------------------------------------------------------------------------------------------------------------------------------------


############################### IMAGEN CANCION #################################

imagenCancion = tk.Label(bg="LightSteelBlue4", relief=RAISED)
imagenCancion.place(relx=0, rely=0.7, relwidth=0.25, relheight=0.3)




############################### ZONA FUNCIONES #################################

zonaReproduccion = tk.Label(bg="LightSteelBlue4", relief=RAISED)
zonaReproduccion.place(relx=0.25, rely=0.7, relwidth=0.5, relheight=0.3)

#Boton que selecciona la cancion anterior
botonAnt = tk.Button(ventana, width=3, height=1, font="Helvetica 20 bold", text="Ι◀", bg="#239089", fg="white")
botonAnt.place(relx=0.32, rely=0.75)

#Boton que pausa la cancion actual
botonPause = tk.Button(ventana, width=3, height=1, font="Helvetica 20 bold", text="ΙΙ", bg='#8ae0db', fg="white")
botonPause.place(relx=0.4, rely=0.75)

#Boton que reproduce la cancion seleccionada
botonPlay = tk.Button(ventana, width=3, height=1, font="Helvetica 20 bold", text="⫸", bg='#8ae0db', fg="white")
botonPlay.place(relx=0.48, rely=0.75)

#Boton que para la cancion actual 
botonStop = tk.Button(ventana, width=3, height=1, font="Helvetica 20 bold", text="■", bg="#8ae0db", fg="white")
botonStop.place(relx=0.56, rely=0.75)

#Boton que selecciona la cancion posterior
botonNext = tk.Button(ventana, width=3, height=1, font="Helvetica 20 bold", text="▶Ι", bg='#239089', fg="white")
botonNext.place(relx=0.64, rely=0.75)



lineaTiempo = tk.Scale(ventana, bg="#239089", troughcolor="#8ae0db", from_=0, to=100, orient=HORIZONTAL, length=350, showvalue=0)
lineaTiempo.place(relx=0.35, rely=0.9)

sliderLabel = Label(ventana, text=0)
sliderLabel.place(relx=0.485, rely=0.85)


############################### ZONA VOLUMEN (?) #################################

otraZona = tk.Label(text="Usuario000",font="Helvetica 12 bold", bg="LightSteelBlue4", relief=RAISED)
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
    
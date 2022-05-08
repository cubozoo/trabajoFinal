from tkinter import * 
import tkinter as tk
from tkinter import ttk
import os

def ventanaPrincipal():
    ventana = tk.Tk()
    ventana.geometry('1200x800')
    ventana.minsize(1200,800)
    ventana.maxsize(1200,800)
    ventana.title('MuWusica')
    listasRepro = []
    listasRepro.append("Selecciona la lista") 
    listasRepro.append("Lista 1")


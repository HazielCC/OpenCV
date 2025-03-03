# -*- coding: utf-8 -*-
"""
Created on Mon May 25 20:35:49 2020

@author: Jesus-Mtz
"""


import tkinter
from tkinter import messagebox
from tkinter import filedialog
from tkinter.filedialog import askopenfilename

window = tkinter.Tk()
window.wm_withdraw()
window.wm_attributes("-topmost", True)


def warning(t,m):
    # window.iconbitmap('./icons/warning.ico')
    messagebox.showerror(message=m, title=t)
    
def borrarQuestion(m):
    # window.iconbitmap('./icons/warning.ico')
    respuesta=messagebox.askokcancel(message=m, title="ATENCIÓN")
    return respuesta

def selectDirectorio(title):
    # window.iconbitmap('./icons/warning.ico')
    tmpdir = filedialog.askdirectory(title = title, initialdir = "C:/DADES")
    return tmpdir

def mensaje(title,mensaje):
    messagebox.showinfo(message=mensaje, title=title)
    
def selectFile():
    filename = askopenfilename()
    return filename

# print(selectDirectorio("Selecciona la ruta de gaurdado"))
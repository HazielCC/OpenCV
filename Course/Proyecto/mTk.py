# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 20:39:59 2022

@author: Jesus-Mtz
"""

import tkinter
from tkinter import filedialog
from tkinter.filedialog import askopenfilename

window = tkinter.Tk()
window.wm_withdraw()
window.wm_attributes("-topmost", True)

def selectFile():
    filename = askopenfilename()
    return filename
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 09:42:32 2021

@author: A.Martinez
"""

import sqlite3
from sqlite3 import Error


def sql_connection(ruta,dataBase):
    try:
        con = sqlite3.connect(ruta+"/"+dataBase+'.db')
        return con
    except Error:
        print(Error)

def crearDB(ruta,dataBase):
    con=sql_connection(ruta,dataBase)
    cursorObj = con.cursor()
    cursorObj.execute(""" CREATE TABLE IF NOT EXISTS color (
                                        porcentaje integer,
                                        hbajo integer,
                                        halto integer,
                                        sbajo integer,
                                        salto integer,
                                        vbajo integer,
                                        valto integer,
                                        totalPixeles integer,
                                        aplica integer
                                    ); """)

    cursorObj.execute(""" CREATE TABLE IF NOT EXISTS presencia (
                                        porcentaje integer,
                                        plantilla blob,
                                        x1 integer,
                                        y1 integer,
                                        x2 integer,
                                        y2 integer,
                                        aplica integer
                                    ); """)
    
    cursorObj.execute(""" CREATE TABLE IF NOT EXISTS forma (
                                        porcentaje integer,
                                        hbajo integer,
                                        halto integer,
                                        sbajo integer,
                                        salto integer,
                                        vbajo integer,
                                        valto integer,
                                        totalPixeles integer,
                                        aplica integer
                                    ); """)
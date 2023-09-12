# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 17:44:48 2023

@author: Roberto Anotnio García Cham

"""

#copiar un directorio completo
import shutil
import os
from io import open
import re
import random
import string

def crear_copia(origen, destino):
    # Copiar el directorio de origen al directorio de destino
    shutil.copytree(origen, destino)

def get_in_folder(path):
    direccion = path
    files = [f for f in os.listdir(direccion) if os.path.isfile(os.path.join(direccion, f))] #enlistamos los archivos, o los que no son carpetas
    subcarpetas= [d for d in os.listdir(direccion) if os.path.isdir(os.path.join(direccion, d))] # creamos una lista de las carpetas

    for archivo in files:
        extension = archivo.split('.')
        print(archivo)
        nueva_linea = ''
        if(extension[1] == 'txt'):
            leer_txt = open(direccion + "/" + archivo, 'r')
            lineas = leer_txt.readlines()
            archivo_nuevo = open(direccion + "/temp.txt", "w")

            for l in lineas:
                for c in l:
                    if re.match(r'^[-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?$', c):
                        random_index = random.randint(0, len(mayusculas) - 1)
                        nueva_linea += mayusculas[random_index] 
                    else:
                        no_random = random.randint(0,9)
                        nueva_linea += str(no_random) 
            
            print(nueva_linea)
            archivo_nuevo.write(nueva_linea)
            nueva_linea = ''
            leer_txt.close()
            archivo_nuevo.close() 
            os.remove(direccion + "/" + archivo)
            os.rename(direccion + "/temp.txt", direccion + "/" + archivo)
            
            
    print(direccion, files, subcarpetas)
    for actual in subcarpetas:
        print(actual)
        direccion = direccion + '/' + actual
        directory_path = direccion
        get_in_folder(directory_path)

    
                   
            
    

# Directorio de origen que deseas copiar
origen = './raiz'
# Directorio de destino donde deseas copiar el contenido del directorio de origen
destino = './copia'
crear_copia(origen, destino)

#empezamos de la copia para leer el directorio
directory_path = './copia'
mayusculas = string.ascii_uppercase #traemos un arreglo de letras mayusculas
#le hablamos a nuestra función recursiva
get_in_folder(directory_path)
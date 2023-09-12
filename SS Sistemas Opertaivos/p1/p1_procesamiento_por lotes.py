# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 17:19:45 2023

@author: Roberto Antonio García Cham
"""

from io import open
import re

archivoR = open("prueba2.txt", "r") #de aqui sacamos la info
archivoNuevo = open("resultado.txt", "w") #creamos el archivo donde pondremos el nuevo formato

lista = archivoR.readlines()
for l in lista:
    res_l = ''
    hexa_2_decimal = ''
    cadena_decimales = ''
    band_hexa = True
    cadenas_a_eliminar = ''
    l = re.sub(r'\/[^,]*,', ',', l) #usamos expresión regular para eliminar la mascara de red
    separados = l.split(',')
    separados[0] += ':'     #para que transforme el último
    
    for h2d in separados[0]:
        if(h2d != ':'):
            hexa_2_decimal += h2d
        else:
            decimales = int(hexa_2_decimal, 16)
            cadena_decimales = cadena_decimales + str(decimales) + ':'
            hexa_2_decimal = ''   
    #print(cadena_decimales) #ya tengo los hexa a decimales
    cadena2 = separados[2]

    #direccion ipv4 to ipv6
    numbers = list(map(int, separados[5].split('.')))
    dir_ipv6 = '{:02x}.{:02x}.{:02x}.{:x}'.format(*numbers).upper()

    #concatenamos    
    cadena_final = cadena2 + ':' + cadena_decimales + dir_ipv6
    
    print(cadena_final)
    archivoNuevo.write(cadena_final + "\n")

archivoNuevo.close()
archivoR.close()


    
    
""" sin split
    for r in l:
        #transformamos de hexadecimal a decimal
        if(r != ':'):
            hexa_2_decimal += r
        else:
            if(r == ','):
                band_hexa = False
            if(band_hexa):
                decimales = int(hexa_2_decimal, 16)
                cadena_decimales = cadena_decimales + str(decimales) + ':'
                print(cadena_decimales)
                hexa_2_decimal = ''
                
            if(band_hexa == False):
                tipo = isinstance(r, str)
                print(tipo)
                if(tipo):
                    cadenas_a_eliminar += r

    for j in i:
        print (j)
"""
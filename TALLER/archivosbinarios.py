#!/usr/bin/env python3
# -*- coding: utf-8-*- 


f = open("data.txt", "r")
# el párameto con el que vamos a abrir el archivo según la nomenclatura append como a 
# Si es binario como una imagen u otra cosa es b , según sea el formato verás cómo la abres como un writeline con ayuda de alguna librería, etc. 
# f es escriptor del archivo
# 
data = midata.readlines()
#readlines lee la lista y 
# 

midata.close()
print(data) #regresa la lista de líneas; data es una lista de lineas
print("-"*72)
print(data[2])
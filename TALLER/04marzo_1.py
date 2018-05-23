#!/usr/bin/env python3
# -*- coding: utf-8-*- 

d1= dict()  #se asigna un diccionario vaío a dl
d2= {} 		#d2 también es un diccionario vacío
d3= {1: 'a', 2: 'b', 3: 'c'} #Se inicializa un diccionario con 3 valores
d4= {'a' : 1, 'b': 2, 'c': 3, 'd': (1,2,3,4,5)}		#Un diccionario está compuesto por parejas de valores

print(d1)
print(d2)
print(d3)
print(d4)
print(type(d4))
try:
	print(d4['1'])
except KeyError:
	print("La llave '1' de tipo string no existe en el dict")
	print("FIN")
print(d4['d'])
print(d4['d'][4])

persona1 = {    
	'nombre':'rctorr',    
	'email': 'rictor@cuhrt',
	'edad':45
	}
	
persona2 = {
	'nombre':'Melisa',    
	'email':'soymelisa@yahoo.com',    
	'edad':23
	}

print(persona1)
print(persona2)
print(persona1['nombre'])
print(persona1['edad'])# Escribir hasta aquí, ejecutar el script y comentar resultados
# Vayamos un poco más allá de los diccionarios…

personas = [persona1, persona2]
print(personas)
print(personas[0])
print(personas[0]['nombre'])
print(personas[1]['nombre'])# Escribir hasta aquí, ejecutar el script y comentar resultado

# O podemos crear una lista de diccionarios desde el inicio

personas = [
	{
	'nombre':'rctorr',    
	'email': 'rictor@cuhrt',
	'edad':45
	},
	{
	'nombre':'Athenas',    
	'email':'athepuppe@gmail.com',    
	'edad':23
	}
]
print (personas[1], ['nombre'])

#Para crear reportes podemos formatear un diccionario a STRING
strpersonas = ["{:12} | {:15} | {:4d}".format(x['nombre'], x['email'], x['edad']) 
for x in personas ]
print(strpersonas)
print(strpersonas[0])

#podemos imprimir la tabla  usando una sola línea de código


tabla = "\n".join(strpersonas)
print(tabla)






















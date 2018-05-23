#!/usr/bin/env python3
# -*- coding: utf-8-*- 

#Super intro a la POO.

#Objeto: Persona
#Atributos:

# - nombre
# - ap_paterno
# - ap_materno

# - edad
# - sexo
# - email
# - obtener_nombre_completo
# - agregar
# - eliminar
# - editar
# un objeto se puede crear de tipo class- no existe objeto tal cuál
# UML el diagrama de clases

import datetime
#modulo que se encataga de las fechas y horas
class Persona():
	#pass
	def __init__(self, nombre, ap_paterno="", edad=0, ap_materno="", email="", sexo=""):	#estructura básica
								#si declaramos cadena vacía significa que es opcional el campo 
		self.nombre = nombre
		self.ap_paterno = ap_paterno
		#todo lo podemos referir a partir de self. Del atributo de la persona 
		self.edad =edad
		self.ap_materno = ap_materno
		self.email =email
		self.sexo = sexo
		#self.anio_actual= anio_actual
		
	def __str__ (self):
		return self.nombre + "" + self.ap_paterno + "" +  self.ap_materno + ""
		#función str que puedo manejar como str para ponerlo en formato cadena 
		
	def anio_nacimiento(self):
		anio_actual = datetime.date.today().year
		anio= anio_actual - self.edad if self.edad >=0 else None	#año de nacimiento
		return anio
#if __name__ == "__main__":
#	persona = Persona

persona1 = Persona("Juan", ap_paterno="Perez")
persona2 = Persona("María","Becerra")
persona3 = Persona("Ana")
persona4 = Persona("Paco", edad=3)
#el orden de los atributos es importante pero en python esto no es necesario aunque sí lo tenemos que definir en la parte de arriba

persona5 = Persona("Luis", email="luis@disney.com")
#ya creo un elemento de la persona real haciendo una variable o tipo persona. Eso ya es una instancia, es decir algo que ya existe y tiene datos con atributos

print (persona1)
suma =persona1.edad +persona2.edad + persona3.edad + persona4.edad + persona5.edad
print ("Suma de edades:", suma)
print (persona4, persona4.anio_nacimiento())
#los atributos no llevan paretntesis, si es 

personas= [persona1, persona2]
print("-" *72)
for per in personas:
	print(per, per.edad, per.sexo, per.email, per.anio_nacimiento())








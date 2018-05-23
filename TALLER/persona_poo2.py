#!/usr/bin/env python3
# -*- coding: utf-8-*- 

#Super intro a la POO.

class Producto():
	#pass
	def __init__(self, nombre, precio_mnx, precio_usd=0, tipo_cambio=0):	#estructura básica
	
		self.nombre = nombre
		self.precio_mnx = precio_mnx
		self.precio_usd = precio_usd / tipo_cambio if tipo_cambio > 0 else precio_usd
		
		
	def __str__ (self):
		return self.nombre
		


if __name__ == "__main__":
	prod = Producto("Lapiz", 20,0,18.75)
	print(prod, prod.precio_mnx, prod.precio_usd)
	prod = Producto("Lapiz", 20,1,0)
	print(prod, prod.precio_mnx, prod.precio_usd)
	prod = Producto("Lapiz", 20,1,18.75)
	print(prod, prod.precio_mnx, prod.precio_usd)
	
#!/usr/bin/env python3
# -*- coding: utf-8-*- 

productos = [
	{
		'nombre':'lapiz',    
		'precio':10
	},
	{
		'nombre':'cuaderno',    
		'precio':50
	},
	{
		'nombre':'libro',    
		'precio':200
	},
	{
		'nombre':'mochila',    
		'precio':350
	},
	{
		'nombre':'ranita',    
		'precio':20
	},
	{
		'nombre':'diurex',    
		'precio':13
	},
	{
		'nombre':'globo',    
		'precio':5
	}
]
# a= a + 1 			--> a += 10
precios = [ x['precio'] for x in productos ]
subtotal= sum(precios)
impuesto = subtotal * 0.16
total = subtotal + impuesto

lineas = ["{:>12} | {:>12.2f}".format(x['nombre'], x['precio']) for x in productos ]
tabla = "\n".join(lineas)
print(tabla)

print("{:12} | {:>15}".format("Producto", "Precio (MNX)"))
print("-"*38)
#temp = [subtotal == subtotal + x['precio'] for x in productos] 
print("{:12} | {:>12}".format("subtotal", "${:.2f}".format(subtotal)))
print("{:12} | {:>12}".format("impuesto", "${:.2f}".format(impuesto)))
print("-"*26)

print("{:12} | {:>12}".format("total", "${:.2f}".format(total)))



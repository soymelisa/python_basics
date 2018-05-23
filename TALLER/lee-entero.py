#!/usr/bin/env python3
# -*- coding: utf-8-*- 
#num= None
esNumero= False
while not esNumero: # not False --> True
	op = input("Dame un nÃºmero: ")
	if op.isdigit():
		num = int(op)
		esNumero = True
	else:
		print()
		print ("Por favor escribe un entero")
		print()


#num= None
#while not num:

	
#mensaje = int(input("DÃ­game una frase: "))
print("el numero es: ", num, "un entero")

#while mensaje != numero:
#	print mensaje
#	print ("AQUÃ ESTÃS INCLUYENDO NÃšMEROS!!!")

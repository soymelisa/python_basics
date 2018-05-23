#PRODUCTOS
#SOLO EL NOMBRE DE LA CLASE VA EN MAYUSCULAS, ES DECIR, PRODUCTO y métodos son con minúsculas
#Atributos
# - nombre
# - precio_mnx
# - precio_usd
#Creo que no hay métdos en este caso
# ======
# Lapiz		 $10.00
# Cuaderno	 $50.00
# Libro		$200.00
# Mochila	$350.00
# Ranita	 $20.00
# 	       ----------
# Subtotal	$630.00
# IVA (16%)	$100.80
# 	       ----------
# Total		$730.80

class Producto():
	#pass
	def __init__(self, nombre, precio_mnx, precio_usd=0, tipo_cambio=0):	#estructura básica
	
		self.nombre = nombre
		self.precio_mnx = precio_mnx
		self.precio_usd = precio_usd /tipo_cambio if tipo_cambio > else precio_usd
		
		
	def __str__ (self):
		return self.nombre + "" + self.precio_mnx + "" +  self.precio_usd + ""
		#función str que puedo manejar como str para ponerlo en formato cadena 
		
	

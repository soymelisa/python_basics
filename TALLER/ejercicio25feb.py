#!/usr/bin/env python3
# -*- codi: utf-8-*- 

prod1 = "Lápiz"
prod2 = "Cuaderno"
prod3 = "libro"
prod4 = "mochila"
prod5 = "ranita"

lapiz= 10.00
cuaderno= 50.00
libro= 200.00
mochila = 350.00
ranita= 20.00
subtotal = lapiz + cuaderno + libro+ mochila+ ranita
impuesto = subtotal * 0.16
total = subtotal + impuesto
dolar = *15.41

print("{:12} | {:12} | {:12}".format("Producto", "Precio (MNX)", "Precio (DLRS)"))
print("-"*26)
print("{:12} | {:12.2f}|  {:12.2f}".format(prod1, lapiz, (lapiz*dolar)))
print("{:12} | {:12.2f}|  {:12.2f}".format(prod2, cuaderno, (cuaderno*dolar) ))
print("{:12} | {:12.2f}|  {:12.2f}".format(prod3, libro, (libro*dolar)))
print("{:12} | {:12.2f}|  {:12.2f}".format(prod4, mochila, (mochila*dolar)))
print("{:12} | {:12.2f}|  {:12.2f}".format(prod5, ranita, (ranita*dolar) ))
print("-"*26)

subtotal2= (lapiz *15.41) + (cuaderno*15.41) + (libro*15.41) + (mochila*15.41) + (ranita*15.41)
print("{:12} | {:>12}| {:>12}".format("subtotal", "${:.2f}".format(subtotal), "${:.2f}".format(subtotal*dolar)"))
print("{:12} | {:>12}".format("impuesto", "${:.2f}".format(impuesto)))
print("-"*26)


print("{:12} | {:>12}".format("total", "${:.2f}".format(total)))


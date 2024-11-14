# Escribir un programa que pregunte al usuario por las ventas de un rango de años y muestre por pantalla una serie con los datos de las ventas indexada por los años,
#  antes y después de aplicarles un descuento del 10%.

import pandas as pd

inicio = int(input('Introduce el ano donde empezaste: '))
fin = int(input('Introduce el ano donte se termina: '))

ventas = {}

for i in range(inicio, fin+1):
    ventas[i] = float(input(f'Introduce las ventas del ano {i}: '))

ventas = pd.Series(ventas)

print(f'Ventas del ano {inicio} a {fin} \n {ventas}')
print(f'Ventas del ano con descuento {inicio} a {fin} \n {ventas*.9}')

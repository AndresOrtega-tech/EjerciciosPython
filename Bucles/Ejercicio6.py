# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.

# *
# **
# ***
# ****
# *****

numero = int(input('Escribe el numero de altura de tu piramide: '))

for n in range(numero):
    print('*'*(n+1))
# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

numero = int(input('Escribe un numero par: '))

if numero%2 == 0:
    print('El numero es par')
else: 
    print('El numero no es par')
# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.

numero = int(input('Escribe un numero: '))
n = 1

while n <= numero:
    if n % 2 == 1:
        print(n, end=', ')

    n += 1
    
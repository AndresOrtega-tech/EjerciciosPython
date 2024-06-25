# Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.

palabra = (input('Escribe un palindromo: '))
palabra = list(palabra)

palindromo = list(palabra)
palindromo.reverse()


if palabra == palindromo:
    print('Si es palindromo')
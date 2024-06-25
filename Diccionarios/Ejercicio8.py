# Escribir un programa que cree un diccionario de traducción español-inglés. El usuario introducirá las palabras en español e inglés separadas por dos puntos, 
# y cada par <palabra>:<traducción> separados por comas. El programa debe crear un diccionario con las palabras y sus traducciones. Después pedirá una frase en 
# español y utilizará el diccionario para traducirla palabra a palabra. Si una palabra no está en el diccionario debe dejarla sin traducir.

traductor = {}
continuar = 'si'

while continuar == 'si':
    palabras = input('Escribe una palbra y su traduccion en formato <palabra>:<traduccion>: ')
    clave, valor = palabras.split(':')
    traductor[clave] = valor

    continuar = input('desea continuar si/no: ')

frase = input('Escribe una frase en espanol: ')

for i in frase.split():
    if i in traductor:
        print(traductor[i], end=' ')
    else: 
        print(i, end=' ')
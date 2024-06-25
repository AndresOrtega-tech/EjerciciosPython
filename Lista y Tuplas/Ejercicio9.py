# Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.

nombre = input('Escribe tu nombre: ')
vocales = ['a', 'e', 'i', 'o', 'u']

nombre = list(nombre)

for i in range(len(vocales)):
    veces = 0
    for n in range(len(nombre)):
        if vocales[i] == nombre[n]:
            veces += 1
    print(f'La vocal {vocales[i]}, aparece {veces} veces')
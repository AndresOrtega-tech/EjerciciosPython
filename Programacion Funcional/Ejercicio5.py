# Escribir una función que reciba una frase y devuelva un diccionario con las palabras que contiene y su longitud.

def funcion(frase):
    f = frase.split()
    d = {}
    for i in f:
        d[i] = len(i)
    return d

fraseUsuario = input('Escribe una frase: ')
print(funcion(fraseUsuario))
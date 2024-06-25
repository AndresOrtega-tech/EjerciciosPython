# Escribir una función que reciba una muestra de números en una lista y devuelva su media.

def media(lista=[]):
    n = 0

    for i in lista:
        n += i
    
    promedio = n/len(lista)
    return promedio

mediaLista = media([1,2,3,4,5,6,7,8])

print(mediaLista)
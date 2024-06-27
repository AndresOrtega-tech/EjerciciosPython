# Escribir una función que reciba otra función y una lista, y devuelva otra lista con el resultado de aplicar la función dada a cada uno de los elementos de la lista.

def cuadrado(n):
    return n**2

def listaCuadrados(funcion, lista):
    l = []
    for i in lista:
        l.append(funcion(i))
    return l

print(listaCuadrados(cuadrado, [1,2,3,4,5,6,7,8]))
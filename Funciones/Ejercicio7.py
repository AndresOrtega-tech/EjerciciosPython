# Escribir una función que reciba una muestra de números en una lista y devuelva otra lista con sus cuadrados.

def listaCuadrados(lista=[]):
    cuadrados=[]
    for i in lista:
        cuadrados.append(i**2)
    return cuadrados

resultado = listaCuadrados([1,2,3,4,5,6,7])

print(resultado)
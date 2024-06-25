# Escribir una función que reciba una muestra de números en una lista y devuelva un diccionario con su media, varianza y desviación típica.
import statistics

def estadistica(lista=[]):
    diccionario = {}
    diccionario['media'] = statistics.mean(lista)
    diccionario['varianza'] = statistics.variance(lista)
    diccionario['desviacion estandar'] = statistics.stdev(lista)

    return diccionario

resultado = estadistica([1,2,3,4,5,6,7,8,9,10])
print(resultado)
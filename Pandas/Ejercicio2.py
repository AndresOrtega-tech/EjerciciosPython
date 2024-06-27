# Escribir una función que reciba un diccionario con las notas de los alumno de un curso y devuelva una serie con la nota mínima, la máxima, media y la desviación 
# típica.

import pandas as pd

calificaciones = {
    'Matematicas':90,
    'Bases de Datos':85,
    'Apps Moviles':87,
    'Estructura de Datos':100
}

def estadisticaNotas(calificacion):
    calificacion = pd.Series(calificacion)
    estadistica = pd.Series([calificacion.min(), calificacion.max(), calificacion.mean(), calificacion.std()], index=['Min', 'Max', 'Media', 'Desviacion tipica'])
    return estadistica

print(estadisticaNotas(calificaciones))
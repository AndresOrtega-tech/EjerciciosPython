# Escribir una función que reciba un diccionario con las notas de los alumnos de un curso y devuelva una serie con las notas de los alumnos aprobados ordenadas 
# de mayor a menor.

import pandas as pd

notas = {
    'Andres':10,
    'Paulina':8,
    'Jose':9
}

def ordenarMayorMenor(lista):
    lista = pd.Series(lista)
    return lista.sort_values(ascending=False)

print(ordenarMayorMenor(notas))
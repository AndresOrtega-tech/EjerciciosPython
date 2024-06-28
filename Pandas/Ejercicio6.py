# El fichero cotizacion.csv contiene las cotizaciones de las empresas del IBEX35 con las siguientes columnas: nombre (nombre de la empresa), 
# Final (precio de la acción al cierre de bolsa), Máximo (precio máximo de la acción durante la jornada), Mínimo (precio mínimo de la acción durante la jornada), 
# volumen (Volumen al cierre de bolsa), Efectivo (capitalización al cierre en miles de euros). Construir una función que construya un DataFrame a partir del un fichero 
# con el formato anterior y devuelva otro DataFrame con el mínimo, el máximo y la media de dada columna.

import pandas as pd


def resumen_cotizaciones(df):
    df = pd.read_csv(df, sep=';', decimal=',', thousands='.', index_col=0)
    return pd.DataFrame([df.min(), df.max(), df.mean()], index=['Minimo', 'Maximo', 'Media'])

resumen_cotizaciones('cotizacion.csv')
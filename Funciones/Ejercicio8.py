# Escribir una función que reciba una muestra de números en una lista y devuelva un diccionario con su media, varianza y desviación típica.
import statistics

def estadistica(lista=[]):
    """
    Calcula estadísticas descriptivas básicas de una lista de números.
    
    Args:
        lista (list): Lista de números sobre la que calcular las estadísticas.
                     Por defecto es una lista vacía.
    
    Returns:
        dict: Diccionario con las siguientes estadísticas:
              - 'media': Media aritmética de los números
              - 'varianza': Varianza de la muestra
              - 'desviacion estandar': Desviación estándar de la muestra
    
    Example:
        >>> estadistica([1,2,3,4,5])
        {'media': 3.0, 'varianza': 2.5, 'desviacion estandar': 1.5811388300841898}
    """
    diccionario = {
        'media': statistics.mean(lista),
        'varianza': statistics.variance(lista),
        'desviacion estandar': statistics.stdev(lista)
    }
    return diccionario

# Nueva función para calcular la mediana de la lista
def mediana(lista=[]):
    """
    Calcula la mediana de una lista de números.
    
    Args:
        lista (list): Lista de números sobre la que calcular la mediana.
                     Por defecto es una lista vacía.
    
    Returns:
        float: Mediana de los números en la lista.
    
    Example:
        >>> mediana([1, 2, 3, 4, 5])
        3.0
    """
    return statistics.median(lista)

resultado = estadistica([1,2,3,4,5,6,7,8,9,10])
print(resultado)
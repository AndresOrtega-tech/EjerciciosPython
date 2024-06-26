# Escribir una función que simule una calculadora científica que permita calcular el seno, coseno, tangente, exponencial y logaritmo neperiano. 
# La función preguntará al usuario el valor y la función a aplicar, y mostrará por pantalla una tabla con los enteros de 1 al valor introducido 
# y el resultado de aplicar la función a esos enteros.

from math import sin, cos, tan, exp, log

def funciones(f, n):
    funcion = {'sin':sin, 'cos':cos, 'tan':tan, 'exp':exp, 'log':log}
    resultado = {}
    for i in range(1, n+1):
        resultado[i] = funcion[f](i)
    return resultado

def calculator():
    f = input('Introduce la función a aplicar (sin, cos, tan, exp, log): ')
    n = int(input('Introduce un entero positivo: '))
    for i, j in funciones(f, n).items():
        print (i, '\t', j)
    return

calculator()
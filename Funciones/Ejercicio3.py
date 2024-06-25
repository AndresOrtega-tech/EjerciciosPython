# Escribir una función que reciba un número entero positivo y devuelva su factorial.

def factorial(numero):
    n = 1
    for i in range(1, numero+1):
        n *= i
    print(n)

factorial(5)
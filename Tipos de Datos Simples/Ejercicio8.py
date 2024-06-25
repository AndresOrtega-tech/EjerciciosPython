# Escribir un programa que pida al usuario dos numeros enteros y muestre por pantalla <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los numeros
# introducidos por el ususario y <c> y <r> son el ciciente y el reto de la division

n = int(input('Dale un valor a N: '))
m = int(input('Dale un valor a M: '))

c = n//m
r = n%m

print(c)
print(r)
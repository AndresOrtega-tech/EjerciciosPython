# Escribir una función que reciba otra función booleana y una lista, y devuelva otra lista con los elementos de la lista que devuelvan True al aplicarles la 
# función booleana.

def funcion(n):
    if n % 2 == 0:
        return n

def filtro(funcion, lista):
    l = []
    for i in lista:
        if funcion(i):
            l.append(i)

    return l

print(filtro(funcion, [1,2,3,4,5,6]))
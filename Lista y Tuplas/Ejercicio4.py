# Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de 
# menor a mayor.

lista = []

for i in range(5):
    lista.append(input(f'Escribe un numero: '))

lista.sort()

print(lista)
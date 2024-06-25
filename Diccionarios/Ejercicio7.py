# Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe preguntar el artículo y su precio y añadir el par al diccionario, 
# hasta que el usuario decida terminar.

carrito = {}
costeTotal = 0

bandera = True

while bandera:
    producto = input('Que producto deseas introducir: ')
    coste = int(input('Escribe el coste: '))
    carrito[producto] = coste
    print(carrito)

    continuar = input('Deseas continuar si/no: ')
    if continuar != 'si': 
        bandera = False 

for producto, coste in carrito.items():
    print(f'{producto} \t {coste}')
    costeTotal += coste

print(costeTotal)
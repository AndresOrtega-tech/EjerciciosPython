# Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un 
# mensaje de aviso si la divisa no está en el diccionario.

monedas = {
    'Euro':'€',
    'Dollar':'$',
    'Yen':'¥'
}

divisa = input("Escribe una divisa: ")

if divisa in monedas:
    print(monedas[divisa])
else:
    print('No esta esa divisa en el diccionario')
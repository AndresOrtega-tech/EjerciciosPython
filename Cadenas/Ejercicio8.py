# Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla el número de euros y
# el número de céntimos del precio introducido.

costo = input('Escribe el costo de un producto con dos decimales: ')

print(f'{costo[:costo.find('.')]} euros')
print(f'{costo[costo.find('.')+1:]} centimos')
# Escribir una función que aplique un descuento a un precio y otra que aplique el IVA a un precio. Escribir una tercera función que reciba un diccionario 
# con los precios y porcentajes de una cesta de la compra, y una de las funciones anteriores, y utilice la función pasada para aplicar los descuentos o 
# el IVA a los productos de la cesta y devolver el precio final de la cesta.

def descuento(precio, descuento):
    precioDescuento = precio - precio*descuento/100
    return precioDescuento

def iva(precio, iva):
    precioIVA = precio + precio*iva/100
    return precioIVA

def calcularTotal (compra, funcion):
    total = 0
    for precio, aplicante in compra.items():
        total += funcion(precio, aplicante)
    return total

print(calcularTotal({1000:20, 500:10, 100:1}, descuento))
print(calcularTotal({1000:20, 500:10, 100:1}, iva))
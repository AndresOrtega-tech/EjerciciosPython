# Escribir un programa que pregunte al ususario una cantidad a invertir, el interes anual y el nuermo de annos, y muestre por pantalla el capital obtenido en la inversion

cantidadInvertida = int(input('Cual es la cantidad que vas a invertir: '))
annos = int(input('Durante cuantos annos vas a invertir: '))
interes = int(input('Cual es el interes anual que te da la inversion: '))

print(round(cantidadInvertida * (interes / 100 + 1) ** annos, 2))

print(round(cantidadInvertida * (interes / 100 + 1) ** annos, 2))
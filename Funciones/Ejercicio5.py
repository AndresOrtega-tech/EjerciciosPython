import math
# Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando la primera función.

def circulo(radio):
    area = math.pi * (radio**2)
    return area

def cilindro( altura):
    volumen = areaCirculo * altura
    return volumen

areaCirculo = circulo(3)
volumenCilindro = cilindro(10)

print(volumenCilindro, areaCirculo)


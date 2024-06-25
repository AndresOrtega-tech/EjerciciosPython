# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la 
# inversión cada año que dura la inversión.

cantidadInvertida = int(input('Escribe la cantidad que vas a invertir: '))
annos = int(input('Escrube la cantidad de annos que vas a invertir: '))
interes = int(input('Escribe el interes que recibes: '))

n = 1

while n <= annos:
    cantidadInvertida = round(cantidadInvertida * (interes / 100 + 1), 2)
    print(f'{n} - {cantidadInvertida}')
    n += 1
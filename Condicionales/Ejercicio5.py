# Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. 
# Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.

edad = int(input('Cual es tu edad: '))
ingreso = int(input('Cual es tu ingreso: '))

if edad >= 16 and ingreso >= 1000:
    print('Puedes tributar')
else:
    print('no puedes tributar')
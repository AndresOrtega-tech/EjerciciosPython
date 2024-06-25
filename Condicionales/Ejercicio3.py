# Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.


dividendo = int(input('Escribe el dividendo: '))
divisor = int(input('Escribe el divisor: '))

if divisor == 0:
    print('Hay un error en el divisor')
else:
    print(dividendo/divisor)
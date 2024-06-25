# Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
 
for n in range(1, 11):
    print(f'Tabla de multiplicar de {n}')
    for j in range (1,11):
        print(j*n)

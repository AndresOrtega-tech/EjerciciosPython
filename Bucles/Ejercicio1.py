# Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.

palabra = input('Escribe una palabra: ')
# Initialize counter variable to 0
n = 0
while n <= 10:
    # Print the word with its current iteration number
    print(f' {n} {palabra}')
    # Increment counter
    n += 1
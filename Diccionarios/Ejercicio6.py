# Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, 
# etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.

persona = {}

bandera = True

while bandera:
    clave = input('Que tipo dato deseas introducir: ')
    dato = input('Escribe la respuesta al dato: ')
    persona[clave] = dato
    print(persona)

    continuar = input('Deseas continuar si/no: ')
    if continuar != 'si': 
        bandera = False 
        print(persona)

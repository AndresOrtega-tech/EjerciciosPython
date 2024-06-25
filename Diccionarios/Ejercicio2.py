# Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje 
# <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.

nombre = input('Escribe tu nombre: ')
edad = int(input('Escribe tu edad: '))
direccion = input('Escribe tu direccion: ')
telefono = input('Escribe tu telefono: ')

persona = {
    'nombre' : nombre,
    'edad' : edad,
    'direccion' : direccion,
    'telefono' : telefono
}


print(persona)
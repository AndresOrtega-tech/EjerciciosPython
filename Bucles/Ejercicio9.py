# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

v = 'contrasena'

bandera = False

while bandera == False:
    pregunta = input('escribe la contrasena: ')
    if pregunta == v:
        bandera = True
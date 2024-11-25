# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

# Store the correct password
v = 'contrasena'

# Initialize flag variable to False
bandera = False

# Keep asking for password until correct one is entered
while bandera == False:
    # Get password input from user
    pregunta = input('escribe la contrasena: ')
    # Check if entered password matches stored password
    if pregunta == v:
        # Set flag to True to exit loop when correct
        bandera = True
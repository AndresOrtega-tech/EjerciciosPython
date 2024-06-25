# Escribir un programa que pida al usuario un peso (en kg) y estatura (en metros), calcule el indice de masa corporal y lo almacene en una variable, y muestre por
# pantalla la frase tu indice de masa corporal es un <IMC> donde <IMC> es el indice de masa corporal calculado redondeado con dos decimales.

peso = input("¿Cuál es tu peso en kg? ")
estatura = input("¿Cuál es tu estatura en metros?")
imc = round(float(peso)/float(estatura)**2,2)
print("Tu índice de masa corporal es " + str(imc))
###
#/*
# * Crea una función que simule las condiciones climáticas (temperatura y probabilidad de lluvia)
# * de un lugar ficticio al pasar un número concreto de días según estas reglas:
# * - La temperatura inicial y el % de probabilidad de lluvia lo define el usuario.
# * - Cada día que pasa:
# *   - 10% de posibilidades de que la temperatura aumente o disminuya 2 grados.
# *   - Si la temperatura supera los 25 grados, la probabilidad de lluvia al día
# *     siguiente aumenta en un 20%.
# *   - Si la temperatura baja de 5 grados, la probabilidad de lluvia al día
# *     siguiente disminuya en un 20%.
# *   - Si llueve (100%), la temperatura del día siguiente disminuye en 1 grado.
# * - La función recibe el número de días de la predicción y muestra la temperatura
# *   y si llueve durante todos esos días.
# * - También mostrará la temperatura máxima y mínima de ese periodo y cuántos días va a llover.
# */
###

import random

# Variables
# Valores creador por el usuario
dias = int(input("Cuantos dias va a ser la simulacion: "))
temperatura = int(input("Ingrese la temperatura inicial: "))

probabilidad_lluvia = 0
temperatura_bajando = 0
probabilidad_temperatura = 0

# Función para simular el clima
def simulacionClima (dias, temperatura, probabilidad_lluvia, probabilidad_temperatura):
    dias_llovio = 0
    temperatura_max = temperatura
    temperatura_min = temperatura

    for i in range(dias):
        probabilidad_temperatura = random.randint(1, 10)
        if probabilidad_temperatura <= 1:
            temperatura +=  random.choice([-2, 2])

        if temperatura >= 25:
            probabilidad_lluvia += 20
        elif temperatura <= 5:
            probabilidad_lluvia -= 20

        if probabilidad_lluvia >= 100:
            dias_llovio += 1
            temperatura -= 1
            probabilidad_lluvia = 0
        elif probabilidad_lluvia <= 0:
            probabilidad_lluvia = 0

        if temperatura > temperatura_max:
            temperatura_max = temperatura
        
        if temperatura < temperatura_min:
            temperatura_min = temperatura
    
    return f"La temperatura maxima fue de {temperatura_max}, la temperatura minima fue de {temperatura_min}, y se llovio {dias_llovio} dias."

print("Temperatura final: ", simulacionClima(dias, temperatura, probabilidad_lluvia, probabilidad_temperatura))
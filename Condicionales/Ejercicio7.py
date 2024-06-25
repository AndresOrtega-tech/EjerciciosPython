# Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:

# Renta	Tipo                 impositivo
# Menos de 10000€	         5%
# Entre 10000€ y 20000€	     15%
# Entre 20000€ y 35000€	     20%
# Entre 35000€ y 60000€	     30%
# Más de 60000€	             45%

# Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.

rentaAnual = int(input('Escribe tu renta anual: '))

if rentaAnual < 10000:
    print('5%')
elif 10000 <= rentaAnual < 20000:
    print('15%')
elif 20000 <= rentaAnual < 35000:
    print('20%')
elif 35000 <= rentaAnual < 60000:
    print('30%')
elif rentaAnual >= 60000:
    print('45%')
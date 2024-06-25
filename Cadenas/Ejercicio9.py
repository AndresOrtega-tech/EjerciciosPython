# Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año.
# Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.

nacimiento = input('Escribe el anno en que naciste: ')

dia = nacimiento[:nacimiento.find('/')]
mesanno = nacimiento[nacimiento.find('/')+1:]
mes = mesanno[:mesanno.find('/')]
anno = mesanno[mesanno.find('/')+1:]

print(dia)
print(mes)
print(anno)
# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota
# que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene
# que repetir.

lista = ['Matematicas', 'Fisica', 'Quimica', 'Historia', 'Lengua']
calificacion = []

for i in range(len(lista)):
    calificacion = int(input(f'Que calificacion sacaste en {lista[i]}: '))
    if calificacion < 70:
        lista.pop(i)

print(lista)
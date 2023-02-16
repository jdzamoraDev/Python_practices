print()
print('CALCULADORA DE PROMEDIOS')
estudiantes = int(input('Escriba la cantidad de estudiantes: '))
nombres = []
notas = []
mejores_estudiantes = []
promedio = 0
contador = 1
print()
while contador <= estudiantes:
    registro_nombre = input('Escriba el nombre del estudiante: ')
    registro_nota = int(input('Escriba la nota del estudiante: '))

    nombres.append(registro_nombre)
    notas.append(registro_nota)
    promedio += registro_nota
    contador += 1

promedio = promedio / estudiantes
print('El promedio de notas es: ', promedio)

for i in range(estudiantes):
    if notas[i] >= promedio:
        mejores_estudiantes.append(nombres[i])

print('Los mejores estudiantes son: ', mejores_estudiantes)

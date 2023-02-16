print()
print('Calculadora de Nota Media')
print('(Calificando del 1 al 10)')
print()
n_alumnos = int(input('Digite la cantidad de estudiantes a evaluar: '))
print()
nombres = []  # Nombre de Estudiantes
e_aprob = []  # Estudiantes Destacados
promedio = 0  # Promedio de notas
notas = []  # Notas de estudiantes

c = 1

while c <= n_alumnos:
    nombre = input('Escriba el nombre del estudiante: ')
    nota = int(input('Ingrese la nota del estudiante: '))
    nombres.append(nombre)
    notas.append(nota)
    promedio += nota
    c += 1
print()
print()
promedio = promedio / n_alumnos
print('Promedio de notas ', promedio)

for i in range(n_alumnos):
    if notas[i] >= promedio:
        e_aprob.append(nombres[i])

print(f'Estudiantes destacados: {e_aprob}')
print()

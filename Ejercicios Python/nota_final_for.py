e = int(input('Ingrese la cantidad de estudiantes a evaluar: '))
print('')
c = 0

p1 = int(input('Escriba el porcentaje del examen: '))

p2 = int(input('Escriba el porcentaje del segundo examen: '))

p3 = int(input('Escriba el porcentaje del proyecto: '))

p4 = int(input('Escriba el porcentaje de la tarea: '))
print('')

for c in range(e):
    nombre = input('Digite el nombre del estudainte: ')

    v1 = float(input('Escriba los puntos obtenido del examen: '))

    v2 = float(input('Escriba los puntos obtenido del segundo examen: '))

    v3 = float(input('Escriba los puntos obtenido del proyecto: '))

    v4 = float(input('Escriba los puntos obtenido de la tarea: '))

    print()

    n1 = (v1 / p1) * 100
    n2 = (v2 / p2) * 100
    n3 = (v3 / p3) * 100
    n4 = (v4 / p4) * 100

    print(f'Nombre del estudiante              : {nombre}')
    print(f'Nota del primer examen % {p1}      : {n1}')
    print(f'Nota del segundo examen %  {p2}    : {n2}')
    print(f'Nota del proyeto % {p3}            : {n3}')
    print(f'Nota de la tarea % {p4}            : {n4}')
    print()
    c = c + 1

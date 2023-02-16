print('-------------------------------------------------------------------------------------------------------------------------')
print('EXPORTACIONES E IMPORTACIONES')
contador_e = 1  # Contador para la solicitud de los nombres de paises exportadores 2020
contador_i = 1  # Contador para la solicitud de los nombres de paises importadores 2020
contador_a = 1  # Contador para la solicitud de los nombres de paises exportadores 2021
contador_b = 1  # Contador para la solicitud de los nombres de paises importadores 2021
exportadores = []
importadores = []
# Grupo1
pais1 = []
pais2 = []
pais3 = []
# Grupo2
pais4 = []
pais5 = []
pais6 = []
# CALCULO 2020
while contador_e <= 3:  # Solicitud de nombres 1
    print(
        '-------------------------------------------------------------------------------------------------------------------------')
    pais_e = input('Escriba el nombre del pais exportador: ')
    exportadores.append(pais_e)
    contador_e += 1
    print(
        '-------------------------------------------------------------------------------------------------------------------------')
while contador_i <= 3:  # Solicitud de nombres 2
    print(
        '-------------------------------------------------------------------------------------------------------------------------')
    pais_i = input('Escriba el nombre del pais importador: ')
    importadores.append(pais_i)
    contador_i += 1
    print(
        '-------------------------------------------------------------------------------------------------------------------------')
print('-------------------------------------------------------------------------------------------------------------------------')
print(f'Escriba las exportaciones de: {exportadores[0]} del año 2020')
op1 = int(input('Escriba el primer numero de exportaciones: '))
op2 = int(input('Escriba el segundo numero de exportaciones: '))
op3 = int(input('Escriba el tercero numero de exportaciones: '))
pais1.append(op1)
pais1.append(op2)
pais1.append(op3)
pais4.append(op1)
pais5.append(op2)
pais6.append(op3)
print('-------------------------------------------------------------------------------------------------------------------------')
print(f'Escriba las exportaciones de: {exportadores[1]} del año 2020')
op4 = int(input('Escriba el primer numero de exportaciones: '))
op5 = int(input('Escriba el segundo numero de exportaciones: '))
op6 = int(input('Escriba el tercero numero de exportaciones: '))
pais2.append(op4)
pais2.append(op5)
pais2.append(op6)
pais4.append(op4)
pais5.append(op5)
pais6.append(op6)
print('-------------------------------------------------------------------------------------------------------------------------')
print(f'Escriba las exportaciones de: {exportadores[2]} del año 2020')
op7 = int(input('Escriba el primer numero de exportaciones: '))
op8 = int(input('Escriba el segundo numero de exportaciones: '))
op9 = int(input('Escriba el tercero numero de exportaciones: '))
pais3.append(op7)
pais3.append(op8)
pais3.append(op9)
pais4.append(op7)
pais5.append(op8)
pais6.append(op9)
print('-------------------------------------------------------------------------------------------------------------------------')
# print(exportadores)
# print(importadores)
# print(pais1)
# print(pais2)
# print(pais3)
# print(pais4)
# print(pais5)
# print(pais6)

# Grupo1
pais_a = []
pais_b = []
pais_c = []
# Grupo2
pais_d = []
pais_e = []
pais_f = []

print('-------------------------------------------------------------------------------------------------------------------------')
# CALCULO 2021
print(f'Escriba las exportaciones de: {exportadores[0]} del año 2021')
op_a = int(input('Escriba el primer numero de exportaciones: '))
op_b = int(input('Escriba el segundo numero de exportaciones: '))
op_c = int(input('Escriba el tercero numero de exportaciones: '))
pais_a.append(op_a)
pais_a.append(op_b)
pais_a.append(op_c)
pais_d.append(op_a)
pais_e.append(op_b)
pais_f.append(op_c)
print('-------------------------------------------------------------------------------------------------------------------------')
print(f'Escriba las exportaciones de: {exportadores[1]} del año 2021')
op_d = int(input('Escriba el primer numero de exportaciones: '))
op_e = int(input('Escriba el segundo numero de exportaciones: '))
op_f = int(input('Escriba el tercero numero de exportaciones: '))
pais_b.append(op_d)
pais_b.append(op_e)
pais_b.append(op_f)
pais_d.append(op_d)
pais_e.append(op_e)
pais_f.append(op_f)
print('-------------------------------------------------------------------------------------------------------------------------')
print(f'Escriba las exportaciones de: {exportadores[2]} del año 2021')
op_g = int(input('Escriba el primer numero de exportaciones: '))
op_h = int(input('Escriba el segundo numero de exportaciones: '))
op_i = int(input('Escriba el tercero numero de exportaciones: '))
pais_c.append(op_g)
pais_c.append(op_h)
pais_c.append(op_i)
pais_d.append(op_g)
pais_e.append(op_h)
pais_f.append(op_i)
print('-------------------------------------------------------------------------------------------------------------------------')
# print(exportadores)
# print(importadores)
# print(pais_a)
# print(pais_b)
# print(pais_c)
# print(pais_d)
# print(pais_e)
# print(pais_f)

# SUMA DE EXPORTADORES 2020
ex1 = sum(pais1)
ex2 = sum(pais2)
ex3 = sum(pais3)
# SUMA DE EXPORTADORES 2021
ex_a = sum(pais_a)
ex_b = sum(pais_b)
ex_c = sum(pais_c)
# SUMA DE IMPORTADORES 2020
im1 = sum(pais4)
im2 = sum(pais5)
im3 = sum(pais6)
# SUMA DE IMPORTADORES 2021
im_d = sum(pais_d)
im_e = sum(pais_e)
im_f = sum(pais_f)

# SUMA DE AMBOS AÑOS EXPORTADORES
s1a = ex1 + ex_a
s2b = ex2 + ex_b
s3c = ex3 + ex_c
# SUMA DE AMBOS AÑOS IMPORTADORES
s4d = im1 + im_d
s5e = im2 + im_e
s6f = im3 + im_f

# PROMEDIO EXPORTADORES
p1 = s1a / 2
p2 = s2b / 2
p3 = s3c / 2
# PROMEDIO IMPORTADORES
p4 = s4d / 2
p5 = s5e / 2
p6 = s6f / 2

print('')
# CONSULTAS1
print('CONSULTAS GENERALES')
print('1 - ¿Cuánto exportó cada país del GRUPO 1 en cada año?')
print(
    f'{exportadores[0]} Exporto en 2020: {ex1} y en 2021: {ex_a} millones de dolares')
print(
    f'{exportadores[1]} Exporto en 2020: {ex2} y en 2021: {ex_b} millones de dolares')
print(
    f'{exportadores[2]} Exporto en 2020: {ex3} y en 2021: {ex_c} millones de dolares')
print('-------------------------------------------------------------------------------------------------------------------------')
print('2 - ¿Cuánto exportó cada país del GRUPO 1 en total en ambos años?')
print(
    f'{exportadores[0]} Exporto entre 2020 y 2021: {s1a} millones de dolares')
print(
    f'{exportadores[1]} Exporto entre 2020 y 2021: {s2b} millones de dolares')
print(
    f'{exportadores[2]} Exporto entre 2020 y 2021: {s3c} millones de dolares')
print('-------------------------------------------------------------------------------------------------------------------------')
print('3 - ¿Cuánto exportó cada país del GRUPO 1 en promedio de ambos años?')
print(
    f'{exportadores[0]} Promedio entre 2020 y 2021: {p1} millones de dolares')
print(
    f'{exportadores[1]} Promedio entre 2020 y 2021: {p2} millones de dolares')
print(
    f'{exportadores[2]} Promedio entre 2020 y 2021: {p3} millones de dolares')
print('-------------------------------------------------------------------------------------------------------------------------')
print('4 - ¿Cuánto exportó cada país del GRUPO 2 en cada año?')
print(
    f'{importadores[0]} Importo en 2020: {im1} y en 2021: {im_d} millones de dolares')
print(
    f'{importadores[1]} Importo en 2020: {im2} y en 2021: {im_e} millones de dolares')
print(
    f'{importadores[2]} Importo en 2020: {im3} y en 2021: {im_f} millones de dolares')
print('-------------------------------------------------------------------------------------------------------------------------')
print('5 - ¿Cuánto exportó cada país del GRUPO 2 en total en ambos años?')
print(
    f'{importadores[0]} Importo entre 2020 y 2021: {s4d} millones de dolares')
print(
    f'{importadores[1]} Importo entre 2020 y 2021: {s5e} millones de dolares')
print(
    f'{importadores[2]} Importo entre 2020 y 2021: {s6f} millones de dolares')
print('-------------------------------------------------------------------------------------------------------------------------')
print('6 - ¿Cuánto exportó cada país del GRUPO 2 en promedio de ambos años?')
print(
    f'{importadores[0]} Promedio entre 2020 y 2021: {p4} millones de dolares')
print(
    f'{importadores[1]} Promedio entre 2020 y 2021: {p5} millones de dolares')
print(
    f'{importadores[2]} Promedio entre 2020 y 2021: {p6} millones de dolares')
print('-------------------------------------------------------------------------------------------------------------------------')
print('')

# CONSULTAS2
print('-------------------------------------------------------------------------------------------------------------------------')
print('La sigiente tabla asigna una letra a cada pais exportador')
print(f'A = {exportadores[0]}')
print(f'B = {exportadores[1]}')
print(f'C = {exportadores[2]}')
opcion1 = input('Seleccione una letra: ')
print('-------------------------------------------------------------------------------------------------------------------------')
if opcion1 == ('A'):
    print('La sigiente tabla asigna una letra a cada pais importador')
    print(f'X = {importadores[0]}')
    print(f'Y = {importadores[1]}')
    print(f'Z = {importadores[2]}')
    opcion2 = input('Seleccione una letra: ')
    if opcion2 == ('X'):
        print(
            '-------------------------------------------------------------------------------------------------------------------------')
        print(
            f'¿Cuántos millones de dólares exportó {exportadores[0]} al país {importadores[0]} en 2020?')
        print(
            f'{exportadores[0]} Le exporto a {importadores[0]} la suma de {op1} millones de dolares')
        print(
            '-------------------------------------------------------------------------------------------------------------------------')
        print(
            f'¿Cuántos millones de dólares exportó {exportadores[0]} al país {importadores[0]} en 2021?')
        print(
            f'{exportadores[0]} Le exporto a {importadores[0]} la suma de {op_a} millones de dolares')
        print(
            '-------------------------------------------------------------------------------------------------------------------------')

        print(f'¿Las exportaciones crecieron o decrecieron del 2020 al 2021? ¿En cuánto?')
        resta = op_a - op1
        if op1 < op_a:
            print(f'Las exportaciones crecieron {resta} millones de dolares')
            print(
                '-------------------------------------------------------------------------------------------------------------------------')
        elif op1 > op_a:
            print(f'Las exportaciones decrecieron {resta} millones de dolares')
            print(
                '-------------------------------------------------------------------------------------------------------------------------')
        elif op1 == op_a:
            print(f'Las exportaciones se mantuvieron igual')
            print(
                '-------------------------------------------------------------------------------------------------------------------------')

        print(
            f'¿Cuánto en promedio exportó {exportadores[0]} al país {importadores[0]} en ambos años?')
        promedio = (op1 + op_a) / 2
        print(
            f'El promedio de exportacion fue de: {promedio} millones de dolares')
        print(
            '-------------------------------------------------------------------------------------------------------------------------')

        print(
            f'¿Cuánto exportó en total {exportadores[0]} en 2020 y cuánto en 2021?')
        print(
            f'{exportadores[0]} Exporto en 2020: {ex1} y en 2021: {ex_a} millones de dolares')
        print(
            '-------------------------------------------------------------------------------------------------------------------------')

        print(
            f'¿Cuánto importó en total {importadores[0]} en 2020 y cuánto en 2021?')
        print(
            f'{importadores[0]} Importo en 2020: {im1} y en 2021: {im_d} millones de dolares')
        print(
            '-------------------------------------------------------------------------------------------------------------------------')

    elif opcion2 == ('Y'):
        print(
            '-------------------------------------------------------------------------------------------------------------------------')
        print(
            f'¿Cuántos millones de dólares exportó {exportadores[0]} al país {importadores[1]} en 2020?')
        print(
            f'{exportadores[0]} Le exporto a {importadores[1]} la suma de {op2} millones de dolares')
        print(
            '-------------------------------------------------------------------------------------------------------------------------')

        print(
            f'¿Cuántos millones de dólares exportó {exportadores[0]} al país {importadores[1]} en 2021?')
        print(
            f'{exportadores[0]} Le exporto a {importadores[1]} la suma de {op_b} millones de dolares')
        print(
            '-------------------------------------------------------------------------------------------------------------------------')

        print(f'¿Las exportaciones crecieron o decrecieron del 2020 al 2021? ¿En cuánto?')
        resta = op_b - op2
        if op2 < op_b:
            print(f'Las exportaciones crecieron {resta} millones de dolares')
            print(
                '-------------------------------------------------------------------------------------------------------------------------')
        elif op2 > op_b:
            print(f'Las exportaciones decrecieron {resta} millones de dolares')
            print(
                '-------------------------------------------------------------------------------------------------------------------------')
        elif op2 == op_b:
            print(f'Las exportaciones se mantuvieron igual')
            print(
                '-------------------------------------------------------------------------------------------------------------------------')

        print(
            f'¿Cuánto en promedio exportó {exportadores[0]} al país {importadores[1]} en ambos años?')
        promedio = (op2 + op_b) / 2
        print(
            f'El promedio de exportacion fue de: {promedio} millones de dolares')
        print(
            '-------------------------------------------------------------------------------------------------------------------------')

        print(
            f'¿Cuánto exportó en total {exportadores[0]} en 2020 y cuánto en 2021?')
        print(
            f'{exportadores[0]} Exporto en 2020: {ex1} y en 2021: {ex_a} millones de dolares')
        print(
            '-------------------------------------------------------------------------------------------------------------------------')

        print(
            f'¿Cuánto importó en total {importadores[1]} en 2020 y cuánto en 2021?')
        print(
            f'{importadores[1]} Importo en 2020: {im2} y en 2021: {im_e} millones de dolares')
        print(
            '-------------------------------------------------------------------------------------------------------------------------')

    elif opcion2 == ('Z'):
        print(
            '-------------------------------------------------------------------------------------------------------------------------')
        print(
            f'¿Cuántos millones de dólares exportó {exportadores[0]} al país {importadores[2]} en 2020?')
        print(
            f'{exportadores[0]} Le exporto a {importadores[2]} la suma de {op3} millones de dolares')
        print(
            '-------------------------------------------------------------------------------------------------------------------------')

        print(
            f'¿Cuántos millones de dólares exportó {exportadores[0]} al país {importadores[2]} en 2021?')
        print(
            f'{exportadores[0]} Le exporto a {importadores[2]} la suma de {op_c} millones de dolares')
        print(
            '-------------------------------------------------------------------------------------------------------------------------')

        print(f'¿Las exportaciones crecieron o decrecieron del 2020 al 2021? ¿En cuánto?')
        resta = op_c - op3
        if op3 < op_c:
            print(f'Las exportaciones crecieron {resta} millones de dolares')
            print(
                '-------------------------------------------------------------------------------------------------------------------------')
        elif op3 > op_c:
            print(f'Las exportaciones decrecieron {resta} millones de dolares')
            print(
                '-------------------------------------------------------------------------------------------------------------------------')
        elif op3 == op_c:
            print(f'Las exportaciones se mantuvieron igual')
            print(
                '-------------------------------------------------------------------------------------------------------------------------')

        print(
            f'¿Cuánto en promedio exportó {exportadores[0]} al país {importadores[0]} en ambos años?')
        promedio = (op3 + op_c) / 2
        print(f'El promedio de exportacion fue de: {promedio}')
        print(
            '-------------------------------------------------------------------------------------------------------------------------')

        print(
            f'¿Cuánto exportó en total {exportadores[0]} en 2020 y cuánto en 2021?')
        print(
            f'{exportadores[0]} Exporto en 2020: {ex1} y en 2021: {ex_a} millones de dolares')
        print(
            '-------------------------------------------------------------------------------------------------------------------------')

        print(
            f'¿Cuánto importó en total {importadores[2]} en 2020 y cuánto en 2021?')
        print(
            f'{importadores[2]} Importo en 2020: {im3} y en 2021: {im_f} millones de dolares')
        print(
            '-------------------------------------------------------------------------------------------------------------------------')

elif opcion1 == ('B'):
    print('La sigiente tabla asigna una letra a cada pais importador')
    print(f'X = {importadores[0]}')
    print(f'Y = {importadores[1]}')
    print(f'Z = {importadores[2]}')
    opcion2 = input('Seleccione una letra: ')
    if opcion2 == ('X'):
        print(
            '-------------------------------------------------------------------------------------------------------------------------')
        print(
            f'¿Cuántos millones de dólares exportó {exportadores[1]} al país {importadores[0]} en 2020?')
        print(
            f'{exportadores[1]} Le exporto a {importadores[0]} la suma de {op4} millones de dolares')
        print(
            '-------------------------------------------------------------------------------------------------------------------------')

        print(
            f'¿Cuántos millones de dólares exportó {exportadores[1]} al país {importadores[0]} en 2021?')
        print(
            f'{exportadores[1]} Le exporto a {importadores[0]} la suma de {op_d} millones de dolares')
        print(
            '-------------------------------------------------------------------------------------------------------------------------')

        print(f'¿Las exportaciones crecieron o decrecieron del 2020 al 2021? ¿En cuánto?')
        resta = op_d - op4
        if op4 < op_d:
            print(f'Las exportaciones crecieron {resta} millones de dolares ')
            print(
                '-------------------------------------------------------------------------------------------------------------------------')
        elif op4 > op_d:
            print(f'Las exportaciones decrecieron {resta} millones de dolares')
            print(
                '-------------------------------------------------------------------------------------------------------------------------')
        elif op4 == op_d:
            print(f'Las exportaciones se mantuvieron igual')
            print(
                '-------------------------------------------------------------------------------------------------------------------------')

        print(
            f'¿Cuánto en promedio exportó {exportadores[1]} al país {importadores[0]} en ambos años?')
        promedio = (op4 + op_d) / 2
        print(
            f'El promedio de exportacion fue de: {promedio} millones de dolares')
        print(
            '-------------------------------------------------------------------------------------------------------------------------')

        print(
            f'¿Cuánto exportó en total {exportadores[1]} en 2020 y cuánto en 2021?')
        print(
            f'{exportadores[1]} Exporto en 2020: {ex2} y en 2021: {ex_b} millones de dolares')
        print(
            '-------------------------------------------------------------------------------------------------------------------------')

        print(
            f'¿Cuánto importó en total {importadores[0]} en 2020 y cuánto en 2021?')
        print(
            f'{importadores[0]} Importo en 2020: {im1} y en 2021: {im_d} millones de dolares')
        print(
            '-------------------------------------------------------------------------------------------------------------------------')
    elif opcion2 == ('Y'):
        print(
            '-------------------------------------------------------------------------------------------------------------------------')
        print(
            f'¿Cuántos millones de dólares exportó {exportadores[1]} al país {importadores[1]} en 2020?')
        print(
            f'{exportadores[1]} Le exporto a {importadores[1]} la suma de {op5} millones de dolares')
        print(
            '-------------------------------------------------------------------------------------------------------------------------')

        print(
            f'¿Cuántos millones de dólares exportó {exportadores[1]} al país {importadores[1]} en 2021?')
        print(
            f'{exportadores[1]} Le exporto a {importadores[1]} la suma de {op_e} millones de dolares')
        print(
            '-------------------------------------------------------------------------------------------------------------------------')

        print(f'¿Las exportaciones crecieron o decrecieron del 2020 al 2021? ¿En cuánto?')
        resta = op_e - op5
        if op5 < op_b:
            print(f'Las exportaciones crecieron {resta} millones de dolares')
            print(
                '-------------------------------------------------------------------------------------------------------------------------')
        elif op5 > op_e:
            print(f'Las exportaciones decrecieron {resta} millones de dolares')
            print(
                '-------------------------------------------------------------------------------------------------------------------------')
        elif op5 == op_e:
            print(f'Las exportaciones se mantuvieron igual')
            print(
                '-------------------------------------------------------------------------------------------------------------------------')

        print(
            f'¿Cuánto en promedio exportó {exportadores[1]} al país {importadores[1]} en ambos años?')
        promedio = (op5 + op_e) / 2
        print(
            f'El promedio de exportacion fue de: {promedio} millones de dolares')
        print(
            '-------------------------------------------------------------------------------------------------------------------------')

        print(
            f'¿Cuánto exportó en total {exportadores[1]} en 2020 y cuánto en 2021?')
        print(
            f'{exportadores[1]} Exporto en 2020: {ex2} y en 2021: {ex_b} millones de dolares')
        print(
            '-------------------------------------------------------------------------------------------------------------------------')

        print(
            f'¿Cuánto importó en total {importadores[1]} en 2020 y cuánto en 2021?')
        print(
            f'{importadores[1]} Importo en 2020: {im2} y en 2021: {im_e} millones de dolares')
        print(
            '-------------------------------------------------------------------------------------------------------------------------')
    elif opcion2 == ('Z'):
        print(
            '-------------------------------------------------------------------------------------------------------------------------')
        print(
            f'¿Cuántos millones de dólares exportó {exportadores[1]} al país {importadores[2]} en 2020?')
        print(
            f'{exportadores[1]} Le exporto a {importadores[2]} la suma de {op6} millones de dolares')
        print(
            '-------------------------------------------------------------------------------------------------------------------------')

        print(
            f'¿Cuántos millones de dólares exportó {exportadores[1]} al país {importadores[2]} en 2021?')
        print(
            f'{exportadores[1]} Le exporto a {importadores[2]} la suma de {op_f} millones de dolares')
        print(
            '-------------------------------------------------------------------------------------------------------------------------')

        print(f'¿Las exportaciones crecieron o decrecieron del 2020 al 2021? ¿En cuánto?')
        resta = op_f - op6
        if op6 < op_f:
            print(f'Las exportaciones crecieron {resta} millones de dolares')
            print(
                '-------------------------------------------------------------------------------------------------------------------------')
        elif op6 > op_f:
            print(f'Las exportaciones decrecieron {resta} millones de dolares')
            print(
                '-------------------------------------------------------------------------------------------------------------------------')
        elif op6 == op_f:
            print(f'Las exportaciones se mantuvieron igual')

        print(
            f'¿Cuánto en promedio exportó {exportadores[1]} al país {importadores[2]} en ambos años?')
        promedio = (op6 + op_f) / 2
        print(
            f'El promedio de exportacion fue de: {promedio} millones de dolares')
        print(
            '-------------------------------------------------------------------------------------------------------------------------')
        print(
            f'¿Cuánto exportó en total {exportadores[1]} en 2020 y cuánto en 2021?')
        print(
            f'{exportadores[1]} Exporto en 2020: {ex2} y en 2021: {ex_b} millones de dolares')
        print(
            '-------------------------------------------------------------------------------------------------------------------------')
        print(
            f'¿Cuánto importó en total {importadores[2]} en 2020 y cuánto en 2021?')
        print(
            f'{importadores[2]} Importo en 2020: {im3} y en 2021: {im_f} millones de dolares')
        print(
            '-------------------------------------------------------------------------------------------------------------------------')
elif opcion1 == ('C'):
    print('La sigiente tabla asigna una letra a cada pais importador')
    print(f'X = {importadores[0]}')
    print(f'Y = {importadores[1]}')
    print(f'Z = {importadores[2]}')
    opcion2 = input('Seleccione una letra: ')
    if opcion2 == ('X'):
        print(
            '-------------------------------------------------------------------------------------------------------------------------')
        print(
            f'¿Cuántos millones de dólares exportó {exportadores[2]} al país {importadores[0]} en 2020?')
        print(
            f'{exportadores[2]} Le exporto a {importadores[0]} la suma de {op7} millones de dolares')
        print(
            '-------------------------------------------------------------------------------------------------------------------------')

        print(
            f'¿Cuántos millones de dólares exportó {exportadores[2]} al país {importadores[0]} en 2021?')
        print(
            f'{exportadores[2]} Le exporto a {importadores[0]} la suma de {op_g} millones de dolares')
        print(
            '-------------------------------------------------------------------------------------------------------------------------')

        print(f'¿Las exportaciones crecieron o decrecieron del 2020 al 2021? ¿En cuánto?')
        resta = op_g - op7
        if op7 < op_g:
            print(f'Las exportaciones crecieron {resta} millones de dolares')
            print(
                '-------------------------------------------------------------------------------------------------------------------------')
        elif op7 > op_g:
            print(f'Las exportaciones decrecieron {resta} millones de dolares')
            print(
                '-------------------------------------------------------------------------------------------------------------------------')
        elif op7 == op_g:
            print(f'Las exportaciones se mantuvieron igual')
            print(
                '-------------------------------------------------------------------------------------------------------------------------')

        print(
            f'¿Cuánto en promedio exportó {exportadores[2]} al país {importadores[0]} en ambos años?')
        promedio = (op7 + op_g) / 2
        print(
            f'El promedio de exportacion fue de: {promedio} millones de dolares')
        print(
            '-------------------------------------------------------------------------------------------------------------------------')
        print(
            f'¿Cuánto exportó en total {exportadores[2]} en 2020 y cuánto en 2021?')
        print(
            f'{exportadores[2]} Exporto en 2020: {ex3} y en 2021: {ex_c} millones de dolares')
        print(
            '-------------------------------------------------------------------------------------------------------------------------')
        print(
            f'¿Cuánto importó en total {importadores[0]} en 2020 y cuánto en 2021?')
        print(
            f'{importadores[0]} Importo en 2020: {im1} y en 2021: {im_d} millones de dolares')
        print(
            '-------------------------------------------------------------------------------------------------------------------------')
    elif opcion2 == ('Y'):
        print(
            '-------------------------------------------------------------------------------------------------------------------------')
        print(
            f'¿Cuántos millones de dólares exportó {exportadores[2]} al país {importadores[1]} en 2020?')
        print(
            f'{exportadores[2]} Le exporto a {importadores[1]} la suma de {op8} millones de dolares')
        print(
            '-------------------------------------------------------------------------------------------------------------------------')
        print(
            f'¿Cuántos millones de dólares exportó {exportadores[2]} al país {importadores[1]} en 2021?')
        print(
            f'{exportadores[2]} Le exporto a {importadores[1]} la suma de {op_h} millones de dolares')
        print(
            '-------------------------------------------------------------------------------------------------------------------------')
        print(f'¿Las exportaciones crecieron o decrecieron del 2020 al 2021? ¿En cuánto?')
        resta = op_h - op8
        if op8 < op_h:
            print(f'Las exportaciones crecieron {resta} millones de dolares')
            print(
                '-------------------------------------------------------------------------------------------------------------------------')
        elif op8 > op_h:
            print(f'Las exportaciones decrecieron {resta} millones de dolares')
            print(
                '-------------------------------------------------------------------------------------------------------------------------')
        elif op8 == op_h:
            print(f'Las exportaciones se mantuvieron igual')
            print(
                '-------------------------------------------------------------------------------------------------------------------------')
        print(
            f'¿Cuánto en promedio exportó {exportadores[2]} al país {importadores[1]} en ambos años?')
        promedio = (op8 + op_h) / 2
        print(
            f'El promedio de exportacion fue de: {promedio} millones de dolares')
        print(
            '-------------------------------------------------------------------------------------------------------------------------')
        print(
            f'¿Cuánto exportó en total {exportadores[2]} en 2020 y cuánto en 2021?')
        print(
            f'{exportadores[2]} Exporto en 2020: {ex3} y en 2021: {ex_c} millones de dolares')
        print(
            '-------------------------------------------------------------------------------------------------------------------------')
        print(
            f'¿Cuánto importó en total {importadores[1]} en 2020 y cuánto en 2021?')
        print(
            f'{importadores[1]} Importo en 2020: {im2} y en 2021: {im_e} millones de dolares')
        print(
            '-------------------------------------------------------------------------------------------------------------------------')

    elif opcion2 == ('Z'):
        print('-------------------------------------------------------------------------------------------------------------------------')
        print(
            f'¿Cuántos millones de dólares exportó {exportadores[2]} al país {importadores[2]} en 2020?')
        print(
            f'{exportadores[2]} Le exporto a {importadores[2]} la suma de {op9} millones de dolares')
        print(
            '-------------------------------------------------------------------------------------------------------------------------')
        print(
            f'¿Cuántos millones de dólares exportó {exportadores[2]} al país {importadores[2]} en 2021?')
        print(
            f'{exportadores[2]} Le exporto a {importadores[2]} la suma de {op_i} millones de dolares')
        print(
            '-------------------------------------------------------------------------------------------------------------------------')
        print(f'¿Las exportaciones crecieron o decrecieron del 2020 al 2021? ¿En cuánto?')
        resta = op_i - op9
        if op9 < op_f:
            print(f'Las exportaciones crecieron {resta} millones de dolares')
            print(
                '-------------------------------------------------------------------------------------------------------------------------')
        elif op9 > op_i:
            print(f'Las exportaciones decrecieron {resta} millones de dolares')
            print(
                '-------------------------------------------------------------------------------------------------------------------------')
        elif op9 == op_i:
            print(f'Las exportaciones se mantuvieron igual')
            print(
                '-------------------------------------------------------------------------------------------------------------------------')

        print(
            f'¿Cuánto en promedio exportó {exportadores[2]} al país {importadores[2]} en ambos años?')
        promedio = (op9 + op_i) / 2
        print(
            f'El promedio de exportacion fue de: {promedio} millones de dolares')
        print(
            '-------------------------------------------------------------------------------------------------------------------------')

        print(
            f'¿Cuánto exportó en total {exportadores[2]} en 2020 y cuánto en 2021?')
        print(
            f'{exportadores[2]} Exporto en 2020: {ex3} y en 2021: {ex_c} millones de dolares')
        print(
            '-------------------------------------------------------------------------------------------------------------------------')

        print(
            f'¿Cuánto importó en total {importadores[2]} en 2020 y cuánto en 2021?')
        print(
            f'{importadores[2]} Importo en 2020: {im3} y en 2021: {im_f} millones de dolares')

        print('-------------------------------------------------------------------------------------------------------------------------')

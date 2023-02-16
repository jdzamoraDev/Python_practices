lista1 = []
lista2 = []
contador1 = 1
contador2 = 1
print('Complete una lista con 10 datos')
while contador1 <= 10:
    p = input('Escriba una palabra o digito: ')
    lista1.append(p)
    contador1 += 1
print(f'Lista con rango de 10 datos: {lista1}')
lista_variable = int(
    input('Ingrese la cantidad de elementos que desea agregar: '))
while contador2 <= lista_variable:
    d = input('Escriba una palabra o digito: ')
    lista2.append(d)
    contador2 += 1
print(f'Lista con rango de {lista_variable} datos: {lista2}')

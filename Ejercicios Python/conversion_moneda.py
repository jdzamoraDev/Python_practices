dolar = 670
euro = 727
libra = 860

colones = int(input('Digite el monto en colones: '))
print('')

print('Seleccione la moneda a convertir: ')
print('1 - Dolares')
print('2 - Euros')
print('3 - Libras')
option = int(input())
print('')

if option == 1:
    conv = colones / dolar
    print(f'El monto {colones} en dolares es de: {conv}')

elif option == 2:
    conv = colones / euro
    print(f'El monto {colones} en dolares es de: {conv}')

elif option == 3:
    conv = colones / libra
    print(f'El monto {colones} en dolares es de: {conv}')

else:
    print('Digite una opcion valida')

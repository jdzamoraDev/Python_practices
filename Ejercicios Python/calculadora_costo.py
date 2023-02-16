value = int(input('Digite el value del producto: '))
print('------------------------------------------')
print('')

print('Seleccione a que grupo pertenece: ')
print('1 - Canasta Basica 1%')
print('2 - Educacion 2%')
print('3 - Canasta Salud 3%')
print('4 - Servicios 13%')
print('------------------------------------------')
option = int(input())
print('')

if option == 1:
    discount_percentage = value * 0.01
    final_amount = value - discount_percentage
    print('--------------------------------------')
    print(f'Monto cancelado: {value}')
    print('Porcentaje aplicado: 1%')
    print(f'value sin el porcentaje: {final_amount}')
    print('--------------------------------------')

elif option == 2:
    discount_percentage = value * 0.02
    final_amount = value - discount_percentage
    print('--------------------------------------')
    print(f'Monto cancelado: {value}')
    print('Porcentaje aplicado: 2%')
    print(f'value sin el porcentaje: {final_amount}')
    print('--------------------------------------')

elif option == 3:
    discount_percentage = value * 0.03
    final_amount = value - discount_percentage
    print('--------------------------------------')
    print(f'Monto cancelado: {value}')
    print('Porcentaje aplicado: 3%')
    print(f'value sin el porcentaje: {final_amount}')
    print('--------------------------------------')

elif option == 4:
    discount_percentage = value * 0.013
    final_amount = value - discount_percentage
    print('--------------------------------------')
    print(f'Monto cancelado: {value}')
    print('Porcentaje aplicado: 13%')
    print(f'value sin el porcentaje: {final_amount}')
    print('--------------------------------------')

elif option < 1 or option > 4:
    print('Digite una opcion valida')

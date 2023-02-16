# Menu
print('Menu de zapateria')
name = input('Escriba su nombre completo: ')
print()
print(f'¡Bienvenido {name} a Zapateria Descalzos , es un gusto atenderte!')
print('Para comenzar, digite su presupuesto de compra en colones')
budget = int(input('Presupuesto: '))

# VARIABLES
option = 0
amount = 0
products_amount = 0
products_value = 0
products_type = [0, 0, 0, 0, 0]


# MENU Y FASE DE COMPRA

while option != 6:
    print()
    print('Productos Disponibles (Sin Impuestos): ')
    print('1 - Sandalias ****** 5,300 ')
    print('2 - Tennis ******* 12,000')
    print('3 - Calzado Deportivo **** 30,500')
    print('4 - Zapato de vestir ***** 20,050')
    print('5 - Botas ******** 25,750')
    print('6 - Salir')
    print()
    option = int(input('Opcion: '))
    print()

# OPCIONES
    if option == 1:
        quantity_calc = 0
        value_calc = 0
        quantity_calc = int(input('Digite la cantidad a cancelar: '))
        value_calc = quantity_calc * 5300
        products_amount = products_amount + quantity_calc
        products_value = products_value + value_calc
        products_type[0] = products_type[0] + quantity_calc
        budget = budget - value_calc
        print(f'Su saldo actual es de: {budget}')

    elif option == 2:
        quantity_calc = 0
        value_calc = 0
        quantity_calc = int(input('Digite la cantidad a cancelar: '))
        value_calc = quantity_calc * 12000
        products_amount = products_amount + quantity_calc
        products_value = products_value + value_calc
        products_type[1] = products_type[1] + quantity_calc
        budget = budget - value_calc
        print(f'Su saldo actual es de: {budget}')

    elif option == 3:
        quantity_calc = 0
        value_calc = 0
        quantity_calc = int(input('Digite la cantidad a cancelar: '))
        value_calc = quantity_calc * 30500
        products_amount = products_amount + quantity_calc
        products_value = products_value + value_calc
        products_type[2] = products_type[2] + quantity_calc
        budget = budget - value_calc
        print(f'Su saldo actual es de: {budget}')

    elif option == 4:
        quantity_calc = 0
        value_calc = 0
        quantity_calc = int(input('Digite la cantidad a cancelar: '))
        value_calc = quantity_calc * 20050
        products_amount = products_amount + quantity_calc
        products_value = products_value + value_calc
        products_type[3] = products_type[3] + quantity_calc
        budget = budget - value_calc
        print(f'Su saldo actual es de: {budget}')

    elif option == 5:
        quantity_calc = 0
        value_calc = 0
        quantity_calc = int(input('Digite la cantidad a cancelar: '))
        value_calc = quantity_calc * 25750
        products_amount = products_amount + quantity_calc
        products_value = products_value + value_calc
        products_type[4] = products_type[4] + quantity_calc
        budget = budget - value_calc
        print(f'Su saldo actual es de: {budget}')

    elif option < 1 or option > 6:
        print('Seleccione una opcion valida.')

# CANCELACION DE FACTURA
iva = products_value * 0.13
total = products_value + iva
budget = budget - iva
if budget >= total:
    print()
    print('*********CANCELADA*********')
    print()
    print(f'FACTURA DE {name}')
    print()
    print('Productos seleccionados: ')
    print(f'Sandalias ****** 5,300  c/u ** {products_type[0]}')
    print(f'Tennis ******* 12,000 c/u ** {products_type[1]}')
    print(f'Deportivo ****** 30,500 c/u*** {products_type[2]}')
    print(f'Zapato de Vestir *** 20,050 c/u ** {products_type[3]}')
    print(f'Botas ******* 25,750 c/u *** {products_type[4]}')
    print()
    print(f'Total de productos seleccuionados:{products_amount}')
    print(f'Monto total a cancelar (SIN IVA):{products_value}')
    print(f'Monto total a cancelar (CON IVA 13%):{total}')
    print(f"Saldo Final: {budget}")
    print()
    print('*********CANCELADA*********')
else:
    print(
        f'ATENCION: Presupuesto insuficiente para confirmar compra. Saldo {budget}')

print()
print('CALCULADORA DE discountS')
print(' 0 a 500 = 0%')
print(' 501 a 1000 = 5%')
print(' 1001 a 7000 = 11%')
print(' 7001 a 15000 = 18%')
print(' 15000 + = 25%')
print()
amount = int(input('Digite el monto a cancelar: '))
if amount > 0 and amount < 500:
    print('Este rango no posee discount.')
elif amount > 501 and amount < 1000:
    discount = amount * 0.05
    final_amount = amount - discount
    print()
    print(f'Monto a cancelar sin discount: {amount}')
    print(f'discount disponible: 5%')
    print(f'Monto a cancelar con discount: {final_amount}')
    print()
elif amount > 1001 and amount < 7000:
    discount = amount * 0.11
    final_amount = amount - discount
    print()
    print(f'Monto a cancelar sin discount: {amount}')
    print(f'discount disponible: 11%')
    print(f'Monto a cancelar con discount: {final_amount}')
    print()
elif amount > 7001 and amount < 15000:
    discount = amount * 0.18
    final_amount = amount - discount
    print()
    print(f'Monto a cancelar sin discount: {amount}')
    print(f'discount disponible: 18%')
    print(f'Monto a cancelar con discount: {final_amount}')
    print()
elif amount > 15001:
    discount = amount * 0.25
    final_amount = amount - discount
    print()
    print(f'Monto a cancelar sin discount: {amount}')
    print(f'discount disponible: 25%')
    print(f'Monto a cancelar con discount: {final_amount}')
    print()

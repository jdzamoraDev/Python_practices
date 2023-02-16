num1 = input('Escriba el primer numero: ')
num2 = input('Escriba el segundo numero: ')

print('Seleccione una opcion: ')
print('1 = Suma')
print('2 = Resta')
print('3 = Multiplicacion')
print('4 = Divicion')
print('5 = Operador Modulo')
print('6 = Operador Exponente')
print('7 = Operador de division entero')
print('En la ultima opcion el primer dato debe ser float y el segundo entero')
op = int(input('Opcion: '))

if op == 1:
    suma = num1 + num2
    print(f'El resultado de la suma es {suma}')
elif op == 2:
    resta = num1 - num2
    print(f'El resultado de la rest es {resta}')
elif op == 3:
    multp = num1 * num2
    print(f'El resultado de la multp es {multp}')
elif op == 4:
    div = num1 / num2
    print(f'El resultado de la div es {div}')
elif op == 5:
    opmodulo = num1 % num2
    print(f'El resultado de la opmodulo es {opmodulo}')
elif op == 6:
    opexponente = num1 ** num2
    print(f'El resultado de la opexponente es {opexponente}')
elif op == 7:
    if float.is_integer(num1):
        div_entero = num1 // num2
        print(f'El resultado de la div entera es {div_entero}')

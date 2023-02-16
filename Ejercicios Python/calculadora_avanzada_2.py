print('Seleccione una opcion: ')
print('1 = El área de un triángulo rectángulo')
print('2 = El perímetro de un cuadrado')
print('3 = El volumen de una esfera.')
print('4 = Volumen de un cilindro')
op = int(input('Opcion: '))
if op == 1:
    alt = int(input('Ingrese la altura:  '))
    base = int(input('Ingrese la base:  '))
    area = base * alt
    print(f'El area del triangulo es: {area}')
elif op == 2:
    l1 = int(input('Ingrese el primer lado:  '))
    l2 = int(input('Ingrese el segundo lado:  '))
    l3 = int(input('Ingrese el tercer lado:  '))
    l4 = int(input('Ingrese el cuarto lado:  '))
    perimetro = l1 + l2 + l3 + l4
    print(f'El perimetro de un cuadrado es: {perimetro}')
elif op == 3:
    radio = int(input('Escriba el radio de la esfera: '))
    volumen = 4/3 * 3.141592653589793 * radio
    print(f'El volumen de la esfera es: {volumen} unidades cubicas')
elif op == 4:
    r = int(input('Ingrese el radio del cilindro: '))
    altura = int(input('Ingrese el radio del cilindro: '))
    v = 3.141592653589793*(r)*altura
    print(f'El volumen del terreno es: {v} cm')

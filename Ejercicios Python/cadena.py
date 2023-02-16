cadena = input('Escriba una cadena:')
if cadena.isalpha():
    print("Los caracteres son de texto")
elif cadena.isdigit():
    print("Los caracteres son numericos")
else:
    print('La cadena es mixta o incluye caracteres especiales')

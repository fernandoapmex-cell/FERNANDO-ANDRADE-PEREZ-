area=int(input('Dame un número impar para la altura: '))
if area % 2 == 0:
    print('Ingresa un numero impar!')
else:
    caracter=input('¿Qué carácter quieres usar? ')
    area = area // 2  
    for i in range(area + 1):
        espacios = area - i
        print(" " * espacios + caracter * (2 * i + 1))
    for i in range(area - 1, -1, -1):
        espacios = area - i
        print(" " * espacios + caracter * (2 * i + 1))
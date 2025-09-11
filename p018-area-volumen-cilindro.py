import math
radio_cilindro=float(input('Ingresa el radio de el cilindro: '))
altura_cilindro=float(input('Ingresa la altura de el cilindro: '))
volumen_cilindro=math.pi*(radio_cilindro * radio_cilindro)*altura_cilindro
print(f'El volumen del cilindro es: {volumen_cilindro:.2f} unidades elevadas al cuadrado')

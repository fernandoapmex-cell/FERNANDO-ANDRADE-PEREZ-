edad=int(input('Ingresa tu edad: '))
if edad < 5:
    print('Tu entrada es gratis')
elif 5 <= edad <= 12:
    print('El precio de tu entrada es de 5$')
elif 13 <= edad <= 64:
    print('El precio de tu entrada es de 10$')
elif edad >= 65:
    print('El precio de tu entrada es de 7$')

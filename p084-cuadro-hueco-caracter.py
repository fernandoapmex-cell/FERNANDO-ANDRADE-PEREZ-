lado=int(input('¿De qué tamaño será el lado del cuadrado? '))
caracter=input('¿Qué carácter quieres usar? ')
for i in range (lado):
    if i == 0 or i == lado - 1:
        print((caracter + " ") * lado)
    else:
        print(caracter + " " + "  " * (lado - 2) + caracter)
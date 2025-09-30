while True:
    sumatoria = 0
    contador = 0

    while True:
        numero = int(input('Introduce números (0 para terminar): '))
        if numero == 0:
            break
        sumatoria += numero
        contador += 1
    promedio =sumatoria / contador
    print(f'Se introdujeron {contador} numeros')
    print(f'La suma de los numeros es : {sumatoria}')
    print(f'El promedio es {promedio}') 
    continuar = input("¿Desea continuar (Si/No)? ").strip().lower()
    if continuar != "s":
        break
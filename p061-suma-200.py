while True:
    sumatoria = 0
    contador=0
    while True:
        if sumatoria < 200:
            numero = int(input(f'Suma actual: {sumatoria}. Introduce un número: '))
            sumatoria += numero
            contador += 1
        else:
            break
    print(f'''
    Meta de 200 alcanzada.
    Suma final: {sumatoria}
    Total de números introducidos: {contador}
    ''')
    continuar = input("¿Desea continuar (Si/No)? ").strip().lower()
    if continuar != "s":
        break
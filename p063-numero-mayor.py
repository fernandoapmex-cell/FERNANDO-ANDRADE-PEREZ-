while True:
    num_mayor=0
    while True:
        numero = int(input('Introduce números (0 para terminar): '))
        if numero == 0:
            break
        else:
            if num_mayor is None or numero > num_mayor:
               num_mayor = numero
    print(f"El número mayor fue: {num_mayor}")
    continuar = input("¿Desea continuar (S/N)? ").strip().upper()
    if continuar == "N":
        break
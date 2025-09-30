while True:
    limite = int(input("Introduce un número límite: "))
    numero = 1
    suma_acumulada = 0
    primero = True
    print("Números impares:", end=" ")
    while numero <= limite:
        if numero % 2 != 0:  
            if not primero:
                print(",", end=" ")
            print(numero, end=" ")
            suma_acumulada += numero
            primero = False
        numero += 1
    print("\nLa suma de los impares es:", suma_acumulada)
    continuar = input("¿Desea continuar (Si/No)? ").strip().lower()
    if continuar != "s":
        break
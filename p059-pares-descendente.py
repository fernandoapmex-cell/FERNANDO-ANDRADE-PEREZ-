while True:
    limite = int(input("Introduce un número límite (menor a 100):"))
    if limite > 100:
        print('El numero ingresado es mayor porfavor ingesa otro respetando la regla')
    else:
        numero = 100
        suma_acumulada = 0
        primero = True
        print("Números pares:", end=" ")
        while numero >= limite:
            if numero % 2 == 0:  
                if not primero:
                    print(",", end=" ")
                print(numero, end=" ")
                suma_acumulada += numero
                primero = False
            numero -= 1
        print("\nLa suma de los impares es:", suma_acumulada)
        continuar = input("¿Desea continuar (Si/No)? ").strip().lower()
        if continuar != "s":
            break
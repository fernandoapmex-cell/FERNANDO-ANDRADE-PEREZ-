anio=int(input('Ingresa el añoa  calcular si es bisiesto: '))
if anio % 4 == 0 and anio %100 != 0 :
    print(f'El año {anio} es año bisiesto por que es divible entre 4 pero no entre 100')
elif anio % 400 == 0:
    print(f'El año es bisiesto por que es divisble entre 400')
else:
    if anio % 100 == 0:
        print(f"El año {anio} no es bisiesto. (Porque es divisible por 100 pero no por 400).")
    elif anio % 4 != 0:
        print(f"El año {anio} no es bisiesto. (Porque no es divisible por 4).")
    else:
        print(f"El año {anio} no es bisiesto.")  # Caso general

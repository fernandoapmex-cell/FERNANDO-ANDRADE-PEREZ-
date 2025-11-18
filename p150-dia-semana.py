def dia_semana(dia):
    if dia == 1:
        return 'El día es: Lunes'
    elif dia == 2:
        return 'El día es: Martes'
    elif dia == 3:
        return 'El día es: Miercoles'
    elif dia == 4:
        return 'El día es: Jueves'
    elif dia == 5:
        return 'El día es: Viernes'
    elif dia == 6:
        return 'El día es: Sabado'
    elif dia == 7:
        return 'El día es: Domingo'
    else:
        return 'Error: El número debe estar entre 1 y 7.'
dia=int(input('Introduce un número del 1 al 7: '))
print(dia_semana(dia))
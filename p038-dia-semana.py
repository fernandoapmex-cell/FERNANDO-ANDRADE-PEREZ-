dia_semana=int(input('ingresa un numero del 1 al 7 : '))
if dia_semana <= 7:
    if dia_semana == 1:
        print('Domingo')
    elif dia_semana == 2:
        print('Lunes')
    elif dia_semana == 3:
        print('Martes')
    elif dia_semana == 4:
        print('Miercoles')
    elif dia_semana == 5:
        print('Jueves')
    elif dia_semana == 6:
        print('Viernes')
    elif dia_semana == 7:
        print('Sabado')
else:
    print('Dia Invalido')
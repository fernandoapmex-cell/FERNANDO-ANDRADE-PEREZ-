print('*Programa de gastos*')
opcion = None
gastos=[]
while opcion != 6:
    try:
        print('''
            1.-Ver gastos
            2.-Agregar gasto
            3.-Modificar gasto
            4.-Eliminar gasto
            5.-Ver total
            6.-Salir
        ''')
        opcion=int(input('\nIngresa una opcion \n'))
        if opcion == 1:
            for i,gasto in enumerate(gastos):
                print(f'Gasto {i+1} :',gasto)
        elif opcion == 2:
            gasto=float(input('Ingresa un nuevo gasto '))
            gastos.append(gasto)
        elif opcion == 3:
            for i,gasto in enumerate(gastos):
                print(f'Gasto {i+1} :',gasto)
            gasto_pocision=int(input('Ingresa el gasto a actualizar (pocision) '))
            gasto_nuevo=float(input(f'Ingresa la nueva cantidad para el gasto {gasto_pocision} : '))
            gastos[gasto_pocision-1] = gasto_nuevo
            print('Gasto actualizado')
        elif opcion == 4:
            for i,gasto in enumerate(gastos):
                print(f'Gasto {i+1} :',gasto)
            gasto_pocision=int(input('Ingresa el gasto a eliminar (pocision) '))
            gastos.pop(gasto_pocision-1)
            print('Gasto eliminados')
        elif opcion == 5:
            total_gastos=sum(gastos)
            print(f'El total de tus gastos es : {total_gastos}')
        else:
            print('Saliendo del programa')
    except Exception as e:
        print ('Valor Incorrecto')

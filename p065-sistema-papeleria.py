#----------------------------------------------------
#Nombre del Programa: Sistema de Ventas de Papelería
#Archivo: p065-sistema-papeleria
#Autor: Fernando Andrade Pérez
#----------------------------------------------------
#Objetivo:
#El objetivo del sistema es registrar multiples ventas ,calcular los subtotales con los descuentos de cada una de las ventas y separarlos por tipo de copias y en el ticket desglosar la informacion 
# de cuantas copias fueron vendidas por cada tipo, su suma de todas, la venta de cada tipo de copia y indicar si tuvo descuento, y sumar el total , al igual que indicar si la venta fue un exito marcado
#por los parametros asignados si cumplio la venta esperada.






#Procesos:
cantidad_vendido=0
cantidad_ventas =1
cantidad_copias_totales =0

cantidad_carta=0
cantidad_oficio=0
cantidad_dobleof=0
cantidad_plano=0

cantidad_vendido_carta=0
cantidad_vendido_oficio=0
cantidad_vendido_dobleof=0
cantidad_vendido_plano=0

cadena_venta=None
cadena_descuento_carta=" "
cadena_descuento_oficio=" "
cadena_descuento_dobleof=" "
cadena_descuento_plano=" "


print(f'---------------------------------\nPapelería la Malena, SA. de CV.\n Sistema de ventas de copias \n---------------------------------')

while True:
    print(f'Venta: {cantidad_ventas}')
    #Entradas:
    tipo_copia = input('Tipo de copia (C)arta $3, (O)ficio $4, (D)oble Of $6, (P)lano $12 (C,O,D,P)?').strip().lower()
    if tipo_copia == 'c':
        #Entradas:
        cantidad_copias =int(input('Cantidad? '))
        #Procesos
        cantidad_carta+=cantidad_copias
        cantidad_vendido_parcial = cantidad_copias * 3
        if cantidad_copias >= 50:
            cadena_descuento_carta="#"            
            print('*** Descuento del 10% aplicado por volumen! ***')
            descuento=cantidad_vendido_parcial*.10
            cantidad_vendido_parcial = cantidad_vendido_parcial - descuento
        cantidad_vendido += cantidad_vendido_parcial
        cantidad_vendido_carta+=cantidad_vendido_parcial
        cantidad_copias_totales+=cantidad_copias
        cantidad_ventas+=1

        
    elif tipo_copia == 'o':
        #Entradas:
        cantidad_copias =int(input('Cantidad? '))
         #Procesos
        cantidad_oficio+=cantidad_copias
        cantidad_vendido_parcial = cantidad_copias * 4
        if cantidad_copias >= 50:
            cadena_descuento_oficio="#"
            print('*** Descuento del 10% aplicado por volumen! ***')
            descuento=cantidad_vendido_parcial*.10
            cantidad_vendido_parcial = cantidad_vendido_parcial - descuento
        cantidad_vendido += cantidad_vendido_parcial
        cantidad_vendido_oficio+=cantidad_vendido_parcial
        cantidad_copias_totales+=cantidad_copias
        cantidad_ventas+=1


    elif tipo_copia == 'd':
        #Entradas:
        cantidad_copias =int(input('Cantidad? '))
         #Procesos
        cantidad_dobleof+=cantidad_copias
        cantidad_vendido_parcial = cantidad_copias * 6
        if cantidad_copias >= 50:
            cadena_descuento_dobleof="#"
            print('*** Descuento del 10% aplicado por volumen! ***')
            descuento=cantidad_vendido_parcial*.10
            cantidad_vendido_parcial = cantidad_vendido_parcial - descuento
        cantidad_vendido += cantidad_vendido_parcial
        cantidad_vendido_dobleof+=cantidad_vendido_parcial
        cantidad_copias_totales+=cantidad_copias
        cantidad_ventas+=1    


    elif tipo_copia == 'p':
        #Entradas:
        cantidad_copias =int(input('Cantidad? '))
        #Procesos
        cantidad_plano+=cantidad_copias
        cantidad_vendido_parcial = cantidad_copias * 12
        if cantidad_copias >= 50:
            cadena_descuento_plano="#"
            print('*** Descuento del 10% aplicado por volumen! ***')
            descuento=cantidad_vendido_parcial*.10
            cantidad_vendido_parcial = cantidad_vendido_parcial - descuento
        cantidad_vendido += cantidad_vendido_parcial
        cantidad_vendido_plano+=cantidad_vendido_parcial
        cantidad_copias_totales+=cantidad_copias  
        cantidad_ventas+=1    
    else:
        print('Opcion Invalida,ingresa una opcion valida')
    #Entradas:   
    continuar = input("¿Desea continuar (S/N)? ").strip().upper()
    #Procesos
    if continuar == "N":
        cantidad_ventas -= 1
        if cadena_descuento_carta == '#':
            cadena_descuento_carta=f'(Precio original: ${cantidad_carta * 3})'
        if cadena_descuento_oficio == '#':
            cadena_descuento_oficio=f'(Precio original: ${cantidad_oficio * 4})'
        if cadena_descuento_dobleof == '#':
            cadena_descuento_dobleof=f'(Precio original: ${cantidad_dobleof * 6})'
        if cadena_descuento_plano == '#': 
            cadena_descuento_plano=f'(Precio original: ${cantidad_plano* 12})'
        if cantidad_vendido < 50:
            cadena_venta='Venta Moderada'
        elif 50 <= cantidad_vendido < 150: 
            cadena_venta='Venta Frecuente'
        elif cantidad_vendido >=150 :
            cadena_venta='Venta Superada'
        break
#Salidas
print(f'''
        ---------------------------------------\n
        Resumen diario de ventas\n
        ---------------------------------------\n
        Ventas realizadas: {cantidad_ventas}\n
        -------------------------\n
        Carta :    {cantidad_carta}   - $ {cantidad_vendido_carta}  {cadena_descuento_carta}\n
        Oficio :   {cantidad_oficio}  - $ {cantidad_vendido_oficio}  {cadena_descuento_oficio}\n
        Doble Of.: {cantidad_dobleof} - $ {cantidad_vendido_dobleof}  {cadena_descuento_dobleof}\n
        Plano :    {cantidad_plano}   - $ {cantidad_vendido_plano}  {cadena_descuento_plano}\n
        -------------------------\n
        Tot. Ventas : {cantidad_copias_totales} - $ {cantidad_vendido}\n
        Esta venta es una : {cadena_venta}\n
''')
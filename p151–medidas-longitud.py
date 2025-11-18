def conversor(unidad,opcion):
    if opcion == 1: 
        resultado = unidad * 2.54
        cadena_resultado=f'{unidad} pulgadas equivalen a {resultado} centímetros.'
    elif opcion ==2:
        resultado = unidad * 3.28
        cadena_resultado=f'{unidad} metros equivalen a {resultado} pies.'
    return cadena_resultado


opcion=int(input('''
      *** Conversor de Unidades ***
        1. Pulgadas a Centímetros
        2. Metros a Pies
        3. Salir
        Elige una opción:'''))
if opcion == 1:
    pulgadas =float(input('Introduce la cantidad en pulgadas :'))
    print(conversor(pulgadas,opcion))
elif opcion == 2:
    metros =float(input('Introduce la cantidad en metros :'))
    print(conversor(metros,opcion))
elif opcion == 3:
    print('Saliendo del programa...')


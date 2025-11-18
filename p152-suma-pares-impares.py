def suma_pares_impares(numero_inicio, numero_fin,modo):
    suma = 0
    numeros=[]
    if modo.upper() == 'P':
        for numero in range(numero_inicio, numero_fin ):
            if numero % 2 == 0:
                suma += numero
                numeros.append(numero)
    elif modo.upper() == 'I':
        for numero in range(numero_inicio, numero_fin ):
            if numero % 2 != 0:
                suma += numero
                numeros.append(numero)

    return numeros, suma
    
print('*** Suma en Rango ***')
numero_inicio = int(input('Introduce el número inicial: '))
numero_fin = int(input('Introduce el número final: '))
modo=input('¿Qué desea sumar? (P)ares o (I)mpares: ')
if modo.upper() == 'P':
    numeros, suma = suma_pares_impares(numero_inicio, numero_fin, modo)
    print(f'La suma de los números pares entre{numero_inicio} y {numero_fin} es: {suma}')
    cadena = '(Calculo:'
    for numero in numeros:
        cadena += f' {numero} +'
    cadena = cadena[:-1] + f' = {suma})'
    print(cadena)
elif modo.upper() == 'I':
    numeros, suma = suma_pares_impares(numero_inicio, numero_fin, modo)
    print(f'La suma de los números impares entre{numero_inicio} y {numero_fin} es: {suma}')
    cadena = '(Calculo:'
    for numero in numeros:
        cadena += f' {numero} +'
    cadena = cadena[:-1] + f' = {suma})'
    print(cadena)
else:
    print('Modo no válido. Use "P" para pares o "I" para impares.')

    

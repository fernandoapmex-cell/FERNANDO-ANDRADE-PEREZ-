def numeros_separados(numeros):
    numeros_separados=numeros.split()
    return numeros_separados
def numeros_sumados(numeros_separados):
    numeros_sumados=[]
    for numero in numeros_separados:
        suma_digitos=0
        for digito in numero:
            suma_digitos += int(digito)
        numeros_sumados.append(suma_digitos)
    return numeros_sumados

numeros=input('Dame los números (separados por espacio): ')
numeros_separados=numeros_separados(numeros)
print('La lista de numeros original: ',numeros_separados)
numeros_sumados=numeros_sumados(numeros_separados)
print('La lista con las suma de dígitos de los números: ',numeros_sumados)

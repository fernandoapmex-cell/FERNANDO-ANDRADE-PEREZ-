import math
def numeros_separados(numeros):
    numeros_separados=numeros.split()
    return numeros_separados
def numeros_factoriales(numeros_separados):
    factoriales=[]
    for numero in numeros_separados:
        factorial=math.factorial(int(numero))
        factoriales.append(factorial)
    return factoriales
numeros=input('Dame los números (separados por espacio): ')
numeros_separados=numeros_separados(numeros)
print('La lista de numeros original: ',numeros_separados)
numeros_factoriales=numeros_factoriales(numeros_separados)
print('La lista con los factoriales:',numeros_factoriales)
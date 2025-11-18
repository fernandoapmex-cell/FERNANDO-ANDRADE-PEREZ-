import statistics
def numeros_separados(numeros):
    numeros_separados=numeros.split()
    return numeros_separados
def media(numeros_separados):
    suma=0
    for numero in numeros_separados:
        suma += int(numero)
    promedio = suma / len(numeros_separados)
    return promedio
def mayor(numeros_separados):
    mayor=max(int(numero) for numero in numeros_separados)
    return mayor
def menor(numeros_separados):
    menor=min(int(numero) for numero in numeros_separados)
    return menor
def desviacion_estandar(numeros_separados):
    numeros_separados = list(map(int, numeros_separados))
    desviacion_estandar = statistics.stdev(numeros_separados)
    return desviacion_estandar
def varianza(numeros_separados):
    numeros_separados = list(map(int, numeros_separados))
    varianza = statistics.variance(numeros_separados)
    return varianza




numeros=input('Dame los números (separados por espacio): ')
numeros_separados=numeros_separados(numeros)
print('La lista de numeros original: ',numeros_separados)
print(f'''
      Estadisticas:
      Media:{media(numeros_separados)}
      Mayor:{mayor(numeros_separados)}
      menor:{menor(numeros_separados)}
      Varianza:{varianza(numeros_separados):.2f}
      Desviación Estándar:{desviacion_estandar(numeros_separados):.2f}
      ''')
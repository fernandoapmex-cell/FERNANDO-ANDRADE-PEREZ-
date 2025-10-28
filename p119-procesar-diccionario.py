nombres = ['Juan', 'Pedro', 'Manuel', 'Elias', 'Maria', 'Felipe', 'Julia', 'Roberto']
sueldos = [4550.22, 8456.88, 1235.12, 9998.00, 12345.50, 29456.55, 12234.00, 2000.00]
combinado={}
suma=0
contador=0
for llave, valor in zip(nombres, sueldos):
    combinado[llave] = valor
print(combinado)
print('\nllaves:\n')
for llave in combinado.keys():
    print(llave,end=' ')
print('\nValores:\n')
for valor in combinado.values():
    print(valor,end=' ')
print('\niterando por llave - valor\n')
for llave in combinado:
    valor = combinado[llave]
    print(llave,valor)
print()
print('Mostrando la llave y el valor simultáneamente (usando items()).')
for llave,valor in combinado.items():
    print(f'{llave} - {valor}')
    suma += valor
    contador+=1
print(f'suma de sueldos:{suma:.2f}')
print(f'Promedio de sueldos{suma/contador}')
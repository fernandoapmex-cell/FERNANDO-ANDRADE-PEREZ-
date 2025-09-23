cantidad=int(input('Ingresa cuantos numeros quieres acomodar: '))
numeros=[]
for indice in range(cantidad):
    numero=int(input(f'Ingresa el numero {indice+ 1} :  '))
    numeros.append(numero)

numeros_acomodados = sorted(numeros)
 # Obtener el número mínimo y máximo de la lista
min_num = numeros_acomodados[0]
max_num = numeros_acomodados[-1]
rango_consecutivo = list(range(min_num, max_num + 1))


if  numeros_acomodados == rango_consecutivo:
    print(f'Los numeros: {numeros_acomodados} ,son consecutivos')
else:
    print(f'Los numeros: {numeros_acomodados} ,no son consecutivos')



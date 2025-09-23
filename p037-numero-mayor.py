cantidad=int(input('Ingresa cuantos numeros quieres acomodar: '))
numeros=[]
for indice in range(cantidad):
    numero=int(input(f'Ingresa el numero {indice+ 1} :  '))
    numeros.append(numero)
numeros_acomodados = sorted(numeros)

print(f'El numero mayor de los numeros:{numeros} es: {numeros[-1]} ')

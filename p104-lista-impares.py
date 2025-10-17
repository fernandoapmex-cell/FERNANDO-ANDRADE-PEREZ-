cantidad_impares=int(input('Introduzca la cantidad de numeros impares: '))
numeros_impares=[]
divisibles_tres=[]
for i in range (1,cantidad_impares+1):
    numero_impar=2*i-1
    numeros_impares.append(numero_impar)   
promedio=sum(numeros_impares)/len(numeros_impares)

print('--Calculos--')
print(f'Lista de los primeros {cantidad_impares} numeros impares:{numeros_impares}')
print(f'Suma de los numeros: {sum(numeros_impares)}')
print(f'Promedio de los numeros: {promedio}')
print('---Divisible entre 3---')
for i in range(len(numeros_impares)):
    if numeros_impares[i]%3==0:
        divisibles_tres.append(numeros_impares[i])
print(f'Numeros divisibles entre 3: {len(divisibles_tres)}')
print(f'Suma de los numeros divisibles entre 3: {divisibles_tres}')
print(f'Suma de los numeros divisibles entre 3: {sum(divisibles_tres)}')
print('-- Busqueda --')
numero_buscar=int(input('Ingresa un numero a buscar: '))
for i in range(len(numeros_impares)):
    if numeros_impares[i] == numero_buscar:
        print(f'Result: El elemento {numero_buscar} está en la lista en la posición (índice) {[i]}.')
        break

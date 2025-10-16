numerosA=input('Introduzca 5 números para la Lista A (separados por un espacio):').split()
numerosB=input('Introduzca 5 números para la Lista B (separados por un espacio):').split()
lista_de_enteros_A = [int(numero) for numero in numerosA]
lista_de_enteros_B = [int(numero) for numero in numerosB]
print(lista_de_enteros_A)
print(lista_de_enteros_B)
numerosC=[]
for i in range(len(lista_de_enteros_A)):
    numerosC.append(lista_de_enteros_A[i]*lista_de_enteros_B[i])
print(f'''
    --- Resultados ---
Lista A: {numerosA}
Lista B: {numerosB}
Lista C (A * B): {numerosC}
    ''')
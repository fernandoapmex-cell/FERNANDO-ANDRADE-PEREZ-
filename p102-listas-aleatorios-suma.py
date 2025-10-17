import random
lista_A=[]
lista_B=[]
lista_C=[]
for i in range(10):
    numero=random.randint(1,100)
    lista_A.append(numero)
    numero=random.randint(1,100)
    lista_B.append(numero)
print('--- Listas Generadas ---')
print(lista_A)
print(lista_B)

for i in range (len(lista_A)):
    if lista_A[i]%2==1 and lista_B[i]%2==1:
        suma=lista_A[i]+lista_B[i]
        lista_C.append(suma)
    else:
        lista_C.append(0)  
print('--- Resultados (Suma solo si A[i] y B[i] son ambos impares) ---')  
print(lista_C)
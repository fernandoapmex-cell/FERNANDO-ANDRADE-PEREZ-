def numero_menor(numero1,numero2,numero3):
    menor=min(numero1,numero2,numero3)
    return menor

n1=int(input('Ingresa el primer numero : '))
n2=int(input('Ingresa el segundo numero : '))
n3=int(input('Ingresa el tercer numero : '))
print(f'El numero menor es : {numero_menor(n1,n2,n3)}')
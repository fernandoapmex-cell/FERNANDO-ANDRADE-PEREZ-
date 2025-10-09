numero=int(input('Dame un número: '))
for i in range(numero,0,-1):
    for j in range(1,i+1):
            print(j,end=" ")
    print()
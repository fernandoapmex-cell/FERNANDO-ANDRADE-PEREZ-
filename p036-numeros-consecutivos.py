a,b,c=input('Ingresa 3 numeros numeros quieres acomodar separados por un espacio: ').split()
a = int(a)
b = int(b)
c = int(c)
min_num = min(a,b,c)
max_num = max(a,b,c)
medio = a + b + c - min_num - max_num 


if medio == min_num + 1 and max_num == medio + 1:
    print(f'Los numeros: {a,b,c} ,son consecutivos')
else:
    print(f'Los numeros no {a,b,c} son consecutivos')



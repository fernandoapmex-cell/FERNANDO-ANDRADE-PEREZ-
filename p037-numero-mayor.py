a,b,c=input('Ingresa 3 numeros numeros quieres acomodar separados por un espacio: ').split()
a = int(a)
b = int(b)
c = int(c)

mayor = a
if b > mayor:
    mayor = b
if c > mayor:
    mayor = c

print("El número mayor es", mayor)
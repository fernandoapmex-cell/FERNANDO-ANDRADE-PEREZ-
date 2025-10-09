# p081-suma-potencias.py
# Suma las potencias de un número x desde x^1 hasta x^n
print("\033[H\033[J")
print("--- Suma de Potencias ---\n")
x = float(input("Introduce el valor de x: "))
n = int(input("Introduce el número de términos (n): "))
suma_total = 0
print(f"\nCalculando la serie S = x^1 + ... + x^{n}")
termino_actual=1
for j in range(n+1):
    suma_total += termino_actual
    print(f'Termino {x}^{j} ={termino_actual}')
    termino_actual *= x
print('\n Suma de toda la serie:',suma_total)
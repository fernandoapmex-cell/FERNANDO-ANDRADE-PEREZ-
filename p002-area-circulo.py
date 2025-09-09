# m2•area-circulo.py
# Calcular el area de un circulo
import math
print("Calculando el area de un circulo")
radio=float(input("Dame el radio: "))
area = math.pi * math.pow(radio,2)
print(f'El circulo de radio {radio:.2f} tiene un area de {area:.2f} cm2')
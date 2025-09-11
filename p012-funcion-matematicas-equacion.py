import math as mt # Importar la biblioteca math para funciones matemáticas con un alias

# Definir los valores de x , y para la evaluación
x = 2
y = 2

fxy = 3 * mt.pow(x,2) + mt.sqrt( mt.pow(x,2) + mt.pow(y,2) + mt.pow( mt.e, mt. log(x)) )
# Evaluar la misma función usando la función pow()
fxy2 =3 *x**2 + mt.sqrt( x**2+ +y**2)+mt.e**mt.log(x)
print(f"Resultado con el operador ** : {fxy:.2f}")
print(f"Resultado con la función pow() : {fxy2:.2f}")
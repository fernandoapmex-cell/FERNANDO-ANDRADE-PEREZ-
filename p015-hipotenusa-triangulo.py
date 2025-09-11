import math
cateto1 = float(input("Introduce valor cateto a: "))
cateto1**=2
cateto2 = float(input("Introduce valor cateto b: "))
cateto2**=2
hipotenusa = math.sqrt( cateto1 * cateto1 + cateto2 * cateto2 )
if (cateto1 <= 0 or cateto2 <= 0):
    print("EL VALOR DEL CATETO ES INCORRECTO,INTRODUCE UN VALOR VALIDO")
else:
    print(hipotenusa)
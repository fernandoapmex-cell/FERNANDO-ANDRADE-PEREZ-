resistencia1,resistencia2,resistencia3,resistencia4 = input('Ingresa el valor de las 4 resistencias separado por un espacio cada una : ').split()
resistencia1=float(resistencia1)
resistencia2=float(resistencia2)
resistencia3=float(resistencia3)
resistencia4=float(resistencia4)
resistencia_equivalente=((1)/(1/resistencia1+1/resistencia2+1/resistencia3+1/resistencia4))

print(f'La resistencia total del circuito en paralelo es : {resistencia_equivalente:.2f}')
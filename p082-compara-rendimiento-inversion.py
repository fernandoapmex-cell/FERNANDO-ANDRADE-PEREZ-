print('--- Fondo de Inversión A ---')
monto_inicial_A=float(input('Monto inicial: '))
tasa_interes_anual=float(input('Tasa de interés anual (%): '))
print('--- Fondo de Inversión B ---')
monto_inicial_B=float(input('Monto inicial: '))
tasa_interes_anual_segundo=float(input('Tasa de interés anual (%): '))
anios=int(input('Años a proyectar: '))
print('--- Comparación de Rendimientos Anuales ---')
print('Año | Fondo A | Fondo B')
for anio in range (anios+1):
    if anio > 0:
        monto_inicial_A *= (1 + tasa_interes_anual / 100)
        monto_inicial_B*= (1 + tasa_interes_anual_segundo / 100)
        print(f'{anio}     |  ${monto_inicial_A:.2f} | ${monto_inicial_B:.2f}')
        
if monto_inicial_B > monto_inicial_A:
    print(f'Resultado final: El fondo B (${monto_inicial_B}) supero al Fondo A(${monto_inicial_A})')
elif monto_inicial_A > monto_inicial_B:
        print(f'Resultado final: El fondo A (${monto_inicial_A}) supero al Fondo B(${monto_inicial_B})')
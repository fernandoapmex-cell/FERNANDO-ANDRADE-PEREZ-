monto_inicial= float(input('Monto inicial de ahorro: '))
deposito_mensual=float(input('Depósito mensual: '))
tasa_interes_mensual=float(input('Tasa de interés mensual (%): '))
meses= int(input('Número de meses a simular: '))


print('--- Plan de Ahorro Detallado ---')
for mes in range(meses + 1):
    if mes > 0:
        interes=(tasa_interes_mensual / 100)*monto_inicial
        print(f'Mes {mes}:Saldo Inicial:${monto_inicial:.2f} | Interés:${interes:.2f} | Saldo Final:${monto_inicial+interes+deposito_mensual:.2f}')
        monto_inicial += deposito_mensual+interes

print(f'\nAl final de {meses} meses, tendrás ${monto_inicial:.2f}')
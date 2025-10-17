mes = int(input('Introduzca un número de mes (1-12):'))
meses=["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31,30, 31, 30, 31]
print('--- Resultados ---')
print(f'Mes: {meses[mes-1]}')
print(f'Dias: {dias_por_mes[mes-1]}')

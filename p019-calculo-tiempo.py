cantidad_horas=int(input('Ingresa la cantidad de horas: '))
cantidad_en_dias=cantidad_horas / 24
cantidad_en_minutos=cantidad_horas * 60
cantidad_en_segundos=cantidad_horas * 60 * 60 
print(f'''

La cantidad de horas : {cantidad_horas} es equivalente a:

Dias:{cantidad_en_dias:.2f}
Minutos:{cantidad_en_minutos}
Segundos:{cantidad_en_segundos}
''')
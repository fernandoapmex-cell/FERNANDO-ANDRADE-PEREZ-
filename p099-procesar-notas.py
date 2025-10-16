notas=[]
while True:
    print(f'Introduzca nota (0 para detener): ',end='')
    nota=float(input())
    if 0< nota <= 100:
        notas.append(nota)
    elif nota > 100:
        print('!Entrada inválida, debe ser 0-100!')
    elif nota == 0:
        break
promedio=sum(notas)/len(notas)
notas_menores_promedio = [nota for nota in notas if nota < promedio]
print(f'''
--- Resultados ---
Total de notas introducidas: {len(notas)}
Lista de notas: {notas}
Suma de notas: {sum(notas)}
Promedio de notas: {promedio}
Nota máxima: {max(notas)}
Nota mínima: {min(notas)}
Notas menores al promedio {promedio}: {len(notas_menores_promedio)}
Lista de notas menores al promedio:{notas_menores_promedio}
''')

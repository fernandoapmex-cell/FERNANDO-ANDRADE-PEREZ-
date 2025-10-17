ciudades =[]
VOCALES = {'a', 'e', 'i', 'o', 'u'}
ciudades_consonante=[]
while True:
    ciudad=input('Introduzca nombre de ciudad ($ para detener):')
    if ciudad == '$':
        break
    else:
        ciudades.append(ciudad)
print('--- Resultados ---')
print(f'Total de ciudades introducidas:{len(ciudades)}')
print(f'Lista original:{ciudades}')
print(f'Lista en orden descendente:{sorted(ciudades,reverse=True)}')
for ciudad in ciudades:
    primera_letra = ciudad[0].lower()
    if primera_letra not in VOCALES:
        ciudades_consonante.append(ciudad)       
print(f'Ciudades que empiezan con consonate:{len(ciudades_consonante)}')
print(f'Lista de ciudades que empiezan con consonante:{ciudades_consonante}')
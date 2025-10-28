paises = {'Argentina': 100, 'Brasil': 200, 'Colombia': 300, 'Chile': 400, 'Ecuador': 500 ,'Bolivia': 600, 'Jamaica': 700}
print('Diccionario inicial:\n')
print(paises)

paises['Brasil'] = 250
paises['Chile'] = 450
paises.update({'Bolivia':450})
paises.update({'Jamaica':750})
print(paises)

datos= {'Apozol': 1863, 'Calera': 1868, 'Fresnillo': 1554, 'Guadalupe':1821, 'Jalpa': 1824, 'Jerez': 1824, 'Loreto': 1931, 'Mazapil': 1824, 'Momax': 1857}
print(datos)
del datos['Apozol']
datos.pop('Fresnillo')
datos.popitem()
print(datos)
datos.clear()
print(datos)
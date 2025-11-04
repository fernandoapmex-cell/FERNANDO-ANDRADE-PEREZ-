lista1={'Juan','Maria','Pedro','Jose','Rocio'}
lista2={'Pedro','Juan','Pablo','Mateo','Esther'}
#crear y mostrar los conjuntos A (basado en la Lista 1) y B (basado en la Lista 2).
print(f'Conjunto A :{lista1}')
print(f'Conjunto B :{lista2}')
print(f'Union (A|B) : {lista1.union(lista2)}')
print(f'Interseccion (A&B) : {lista1.intersection(lista2)}')
print(f'Diferencia simetrica (A^B) : {lista1.symmetric_difference(lista2)}')
comprobacion={'Pablo','Mateo'}.issubset(lista2)
print(f'¿Es Pablo, Mateo un subconjunto de B?:{comprobacion}')
comprobacion=lista1.issuperset({'Reynaldo','Angelica'})
print(f'¿Es A un superconjunto de Reynaldo, Angelica?:{comprobacion}')
comprobacion='Pedro' in lista1
print(f'¿Está "Pedro" en el conjunto A?:{comprobacion}')
comprobacion='Lilia' not in lista2
print(f'¿No está "Lilia" en el conjunto B?:{comprobacion}')
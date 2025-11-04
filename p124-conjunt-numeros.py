lista1={50, 60, 70, 80, 90, 100, 200}
lista2={60, 90, 100, 300, 400, 500}
lista3={10, 20, 60, 90, 70, 100, 600, 700}
print(f'''
      Lista de conjuntos A,B,C
      Conjunto A:{lista1}
      Conjunto B:{lista2}
      Conjunto C:{lista3}
      ''')
print(f'Union (A|B) : {lista1.union(lista2)}')
print(f'Union (B|C) : {lista2.union(lista3)}')
print(f'Diferencia (A-C) : {lista1.difference(lista3)}')
print(f'Diferencia Simetrica (B^C) : {lista2.symmetric_difference(lista3)}')
print(f'Interseccion (B&C):{lista2.intersection(lista3)}')
comprobacion=lista1.issubset(lista2)
print(f'¿Es A subconjunto de B?:{comprobacion}')
comprobacion=lista3.issubset(lista1)
print(f'¿Es C subconjunto de A?:{comprobacion}')
comprobacion=100 in lista1
print(f'¿Está el número 100 en A?:{comprobacion}')
comprobacion=60 in lista1&lista2&lista3
print(f'¿Está el número 60 en A, B y C?:{comprobacion}')
comprobacion=900 not in lista3
print(f'¿No está el número 900 en C?:{comprobacion}')
dias = {1: 'Lunes', 2: 'Martes', 3: 'Miércoles', 4: 'Jueves', 5: 'Viernes', 6: 'Sábado', 7:
'Domingo'}
print(f'''
      LLave 1 (con []):{dias[1]}
      LLave 7 (con []):{dias[7]}
      Llave 5 (con get()): {dias.get(5)}
      Llave 7 (con get()): {dias.get(7)}
      ''')
# p128-funcion-parametros.py

def saluda(apaterno: str, nombre: str) -> None:
    print(f'Hola {nombre} {apaterno}')

saluda('Perez', 'Juan')
# saluda('Juan') # Genera error (pocos)
# saluda('Juan','Diaz,'Perez') # Genera error (muchis)
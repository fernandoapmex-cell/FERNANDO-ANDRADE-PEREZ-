while True:
    numero =input('Introduce un número para verificar si es palíndromo: ')
    if numero == numero[::-1]:
        print(f'El número {numero} es un palíndromo.')
    else:
        print(f'El número {numero} no es un palíndromo.')
    continuar = input("¿Desea continuar (Si/No)? ").strip().lower()
    if continuar != "s":
        break
    
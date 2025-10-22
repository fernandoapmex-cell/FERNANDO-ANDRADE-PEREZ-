# p108-conversor-unidades.py
# Conversor de unidades de longitud usando diccionarios
print('\033[H\033[J')
print('Conversor de unidades de longitud usando diccionarios\n')
conversiones = {
'km': 1000,
'm': 1,
'cm': 0.01,
'mm': 0.001
}
longitud = int(input("Dame la longitud ?"))
while True:
    try:
        unidad = input("Unidad (km, m, cm ,mm) ? ")
        if unidad in conversiones:
            break
        else:
            print("Unidad no válida. Intente de nuevo.")
    except ValueError:
        print("Error: Debe ingresar un valor numérico.")

resultado = longitud * conversiones[unidad]
print(f"{longitud:,.2f} {unidad} son {resultado:,.2f} metros")
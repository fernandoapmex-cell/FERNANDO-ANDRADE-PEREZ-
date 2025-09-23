nombre=input('Ingresa tu nombre: ')
edad=int(input('Ingresa tu edad: '))
sexo=input('Eres mujer?(Si/No)').lower().strip()
calificaciones=[]
for indice in range(3):
    numero=float(input(f'Ingresa la calificacion numero {indice+ 1} :  '))
    calificaciones.append(numero)
promedio=sum(calificaciones)/len(calificaciones)
print(f'tu promedio es: {promedio:.2f}')

if  sexo != 'si':
    print(f"Lo sentimos, {nombre}. La universidad solo acepta mujeres.")    
elif edad < 21:
    print(f"Lo sentimos, {nombre}. No cumples con la edad requerida (mayores de 21 años).")   
elif not  8 <= promedio <=9.5:
    print(f"Lo sentimos, {nombre}. Tu promedio de {promedio:.2f} no alcanza el mínimo requerido de 8 a 9.5.")
else:
    print(f"¡Felicidades, {nombre}! Has sido aceptada. Cumples con la edad y tu promedio de {promedio:.2f} está dentro del rango permitido.")

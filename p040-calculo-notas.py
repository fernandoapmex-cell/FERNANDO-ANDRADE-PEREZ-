cantidad=int(input('Ingresa cuantas calificaciones quieres ingresar: '))
calificaciones=[]
for indice in range(cantidad):
    numero=float(input(f'Ingresa la calificacion numero {indice+ 1} :  '))
    calificaciones.append(numero)
promedio=sum(calificaciones)/len(calificaciones)

print(f'tu promedio es: {promedio:.2f}')
if promedio < 6:
    print("Quedas reprobado")
elif promedio < 7:
    print("Pasas de panzazo")    
elif promedio < 8:
    print("Muy bien, puedes mejorar")  
elif promedio < 9:
    print("Excelente,Sigue asi")    
elif promedio < 10:
    print("Perfecto ,Tu esfuerzo valio la pena")    
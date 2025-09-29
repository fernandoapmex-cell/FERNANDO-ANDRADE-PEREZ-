calificacion1= float(input('Ingresa la calificacion 1: '))
calificacion2= float(input('Ingresa la calificacion 2: '))
calificacion3= float(input('Ingresa la calificacion 3: '))
calificacion4= float(input('Ingresa la calificacion 4: '))
calificacion5= float(input('Ingresa la calificacion 5: '))

promedio = (calificacion1 + calificacion2 + calificacion3 + calificacion4 + calificacion5)/5

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
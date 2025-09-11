import math
punto_a_x,punto_a_y=input('Ingresa las coordenadas X,Y del punto A separadas por un espacio: ').split()
punto_b_x,punto_b_y=input('Ingresa las coordenadas X,Y del punto B separadas por un espacio: ').split()
punto_a_x=int(punto_a_x)
punto_a_y=int(punto_a_y)
punto_b_x=int(punto_b_x)
punto_b_y=int(punto_b_y)
distancia_entre_dos_puntos=math.sqrt(pow((punto_a_x-punto_b_x),2)+pow((punto_a_y-punto_b_y),2))
print(f'La distancia entre el punto A y B es de : {distancia_entre_dos_puntos} unidades')
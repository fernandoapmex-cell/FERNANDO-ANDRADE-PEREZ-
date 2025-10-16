# p097-procesar-datos-sensores.py
# Simulación de recolección y procesamiento de datos de sensores
import random
# --- 1. Generación de Datos Simulados ---
print('\033[H\033[J')
print("Simulando la recolección de datos de dos sensores...")
sensor_a_datos = []
sensor_b_datos = []
for _ in range(10):
    sensor_a_datos.append(random.randint(1, 100)) # Llena la lista del sensor A
    
    sensor_b_datos.append(random.randint(1, 100)) # Llena la lista del sensor B 
print("\n--- Datos Originales de los Sensores ---")
print(f"Sensor A: {sensor_a_datos}")
print(f"Sensor B: {sensor_b_datos}")
# -- 2. Transformación y Combinación de Datos ---

datos_combinados = []
for i in range(10):
    # Transforma (eleva al cuadrado) el dato de cada sensor
    sensor_a_datos[i] = sensor_a_datos[i] ** 2
    sensor_b_datos[i] = sensor_b_datos[i] ** 2
    # Suma los datos ya transformados y los añade a la tercera lista
    suma_transformada = sensor_a_datos[i] + sensor_b_datos[i]
    datos_combinados.append(suma_transformada)
# --- 3. Muestra de Resultados ---
print("\n--- Datos Procesados ---")
print(f"Sensor A (Transformados): {sensor_a_datos}")
print(f"Sensor B (Transformados): {sensor_b_datos}")
print(f"Datos Combinados: {datos_combinados}")
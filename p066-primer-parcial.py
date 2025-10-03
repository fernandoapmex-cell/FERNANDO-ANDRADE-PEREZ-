"""
Nombre del Programa : p086-primer-parcial.py
Objetivo: El programa debe controlar la venta de boletos, gestionar el aforo y calcular los ingresos
generados.
Nombre del Alumno: Fernando Andrade Pérez
Matrícula: 42405310
Materia: Computación Aplicada
Examen: Primer Parcial
"""

# --- Inicialización de Contadores y Acumuladores ---
# Aquí se declaran todas las variables que necesitarás para guardar los datos
edad=int
tipo_comprador=int
sexo=str
precio_boleto_parcial=float
# --- Contadores de Asistentes ---
total_estudiantes = 0
total_adultos = 0
total_tercera_edad = 0
total_academicos = 0
total_asistentes = 0
# ... (agrega los demás contadores de tipo de comprador y de sexo)
venta_contador= 0
total_rechazados = 0
suma_edades = 0
contador_mujeres=0
contador_hombres=0
# --- Acumuladores de Ingresos ---
ingresos_estudiantes = 0.0
ingresos_adultos = 0.0
ingresos_tercera_edad = 0.0
ingresos_academicos=0.0
ingresos_totales = 0.0
# ... (agrega los demás acumuladores de ingresos)

# --- Precios de los Boletos (constantes) ---
PRECIO_ESTUDIANTE = 50.0
PRECIO_ADULTO = 90.0
PRECIO_TERCERA_EDAD =60
PRECIO_ACADEMICO=70 
VENTAS_BAJAS = 1500.00
VENTAS_BUENAS=3500.00
# ... (agrega las demás constantes de precios)
print('\033[2J\033[H')
print("--- Sistema de Venta de Boletos de Cine ---\n\n")

# --- Ciclo Principal para la Venta de Boletos ---
# Usaremos un ciclo while para registrar ventas hasta que el usuario decida parar.
continuar_venta = "s"
while continuar_venta == "s":
    venta_contador += 1
    print(f"\n Venta {venta_contador}:")
    # --- 1. Solicitud de Datos ---
    # Pide la edad, el tipo de comprador y el sexo.
    # ¡Recuerda convertir la edad a un número entero! 
    edad = int(input("Edad: ") )
    if edad > 13:
             # ... (pide el tipo de comprador y el sexo)
        tipo_comprador=int(input(f'''
        Ingrese que tipo de comprador es usted
                            
        1.- Estudiante --------------------------------- $50
        2.- Adulto ------------------------------------- $90
        3.- Tercera Edad ------------------------------- $60
        4.- Académico (Nuevo tipo agregado) ------------ $70
        
        Seleccione un valor del (1 - 4):
        ''' ))
        sexo = input("Introduzca su sexo F para femenino M para masculino (F/M): ").lower().strip()
        # --- 2. Validación de Edad (Clasificación B) ---
        # La película es para mayores de 13 años.
        # Si la edad es permitida, procede con la venta.
        # Muestra el mensaje de bienvenida con los datos registrados
        print(f"¡Bienvenido(a)! Venta registrada ! : Edad:{edad},Sexo:{sexo},Tipo:{tipo_comprador}")
        # --- 3. Actualización de Estadísticas Generales ---
        # Incrementa el contador de asistentes y suma la edad para el promedio.
        total_asistentes += 1
        suma_edades += edad
        # Incrementa el contador de sexo correspondiente (hombre o mujer).
        if sexo == 'm':
            contador_hombres+=1
        elif sexo == 'f':
            contador_mujeres+=1
        # --- 4. Cálculo de Costo y Actualización de Contadores Específicos ---
        # Usa una estructura if/elif/else para determinar el precio y actualizar
        # los contadores del tipo de comprador y sus ingresos.
        if tipo_comprador == 1:
            total_estudiantes += 1
            ingresos_estudiantes += PRECIO_ESTUDIANTE
            precio_boleto_parcial = PRECIO_ESTUDIANTE
        elif tipo_comprador == 2:
            total_adultos +=1
            ingresos_adultos += PRECIO_ADULTO
            precio_boleto_parcial = PRECIO_ADULTO
        elif tipo_comprador == 3:
            total_tercera_edad+=1
            ingresos_tercera_edad +=PRECIO_TERCERA_EDAD
            precio_boleto_parcial = PRECIO_TERCERA_EDAD
        elif tipo_comprador == 4:
            total_academicos+=1
            ingresos_academicos += PRECIO_ACADEMICO
            precio_boleto_parcial = PRECIO_ACADEMICO
        # Suma el costo del boleto a los ingresos totales.
        ingresos_totales += precio_boleto_parcial

    else:
        # Si la edad no es permitida, muestra un mensaje y actualiza el contador ()
        print("ACCESO DENEGADO: El comprador es menor de 13 años.")
        # ... (incrementa el contador de personas rechazadas)
        total_rechazados += 1 

    # Pregunta al usuario si desea registrar otra venta.
    continuar_venta = input("\n¿Deseas registrar otra venta? (S/N): ").lower().strip()
# --- FIN DEL CICLO ---

# --- 5. Cálculo de Promedio ---
# Calcula el promedio de edad. Cuidado con la división entre cero si no hubo asistentes.
# if total_asistentes > 0:
#     promedio_edad = ... # (calcula el promedio aquí)
if (total_asistentes > 0 ):
    promedio_edad = suma_edades / total_asistentes
else:
    print('--------------NO HUBO ASISTENTES-------------')
# --- 6. Impresión del Reporte Final ---
print("\n*** REPORTE FINAL DE LA FUNCIÓN ***")

print("\n--- Estadísticas del Público ---")
# Imprime todos los totales de asistentes por tipo y sexo.
if(total_estudiantes > 0):
    print(f'Total Estudiantes: {total_estudiantes}')
if(total_adultos > 0):
    print(f'Total Adultos: {total_adultos}')
if(total_tercera_edad > 0):
    print(f'Total Tercera Edad: {total_tercera_edad}')
if(total_academicos > 0):
    print(f'Total Academicos: {total_academicos}') 
print('-'*20)   
if(contador_hombres > 0):
    print(f'Total de hombres : {contador_hombres}')
if(contador_mujeres > 0):
    print(f'Total de Mujeres : {contador_mujeres}')   
print('-'*20)   
if(total_asistentes >0):
    print(f'Total asistentes: {total_asistentes}')
    print(f'Promedio  de edad asistentes: {promedio_edad} años')
if(total_rechazados >0):
    print(f'Personas rechazadas por edad: {total_rechazados}')

print("\n--- Reporte de Ingresos ---")
# Imprime todos los ingresos por tipo de comprador y el total general.
# Utiliza formato para mostrar dos decimales en el dinero.
if(ingresos_estudiantes > 0):
    print(f'Ingresos por Estudiantes: ${ingresos_estudiantes:.2f}')
if(ingresos_adultos > 0):
    print(f'Ingresos por Adultos: ${ingresos_adultos:.2f}')
if(ingresos_tercera_edad > 0):
    print(f'Ingresos por Tercera Edad: ${ingresos_tercera_edad:.2f}')
if(ingresos_academicos > 0):
    print(f'Ingresos por Academico: ${ingresos_academicos:.2f}')
print('-'*20)
if(ingresos_totales > 0):
    print(f'TOTAL RECAUDADO: ${ingresos_totales:.2f}')

print("\n--- Rentabilidad ---")
# --- 7. Mensaje de Rentabilidad ---
# Usa una estructura if/elif/else para determinar si las ganancias
# fueron BAJAS, MODERADAS o BUENAS, basándote en los ingresos totales.
if (0 < ingresos_totales < VENTAS_BAJAS):
    print('La función generó BAJAS ganancias.')
elif(VENTAS_BAJAS <= ingresos_totales <= VENTAS_BUENAS):
    print('La función generó ganancias MODERADAS.')
elif(ingresos_totales > VENTAS_BUENAS):
    print('La función generó BUENAS ganancias.')
else:
    print('-----NO HUBO GANANCIAS-----')


""" ----------------- preguntas del examen ---------------------

1. Imagina que el cine decide implementar una promoción: los martes, todos los boletos de Adulto tendrán un 20% de descuento. ¿Qué cambios tendrías que hacer en tu código para agregar esta funcionalidad? Menciona qué nueva pregunta le harías al usuario y en qué parte del código agregarías la nueva lógica.

 Respuesta = Le preguntaria al usuario que dia y el valor lo meto a una variable dia es despues de que el ususario elija si quiere un boleto adulto en el if de tipo comprador == adulto agregaria otro if con la condicion de que dia == martes Si el dia conincide con la condicion calculo del descuento con descuento = PRECIO_ADULTO *.20 y saco precio_boleto_parcial = PRECIO_ESTUDIANTE - descuento y en el else todo como estaba. 

2. Supongamos que, al probar tu programa, el "Total Recaudado en General" siempre te da un resultado incorrecto, aunque los ingresos por cada tipo de comprador parecen correctos. Describe, paso a paso, qué harías para encontrar el error. #¿En qué líneas específicas de tu código pondrías atención para verificar los valores y solucionar el problema?

 Respuesta = Prmero checo en que linea de codigo se ejecuta el error , verifico en consola que tipo de error se esta mandando a imprimir, hago una ejecucion paso a paso para ver donde ocurre el error, si no es un error de programacion hago la comprobacion logica/matematica,encuentro y arreglo el error,verifico la funcionabilidad

"""
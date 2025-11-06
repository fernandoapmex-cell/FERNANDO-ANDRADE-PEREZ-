#agrego la opcion para salir
opcion=""
#declaro el array para guardar los diccionarios que seran productos
productos=[]
#hago un ciclo para agregar productos
#aca ire guardando la suma de stock
stock=0
#declaro un cont para la suma de precios
precios_suma=0
while opcion != "n":
    #aca declaro el diccionario que se ira almacenando en cada vuelta y se ira vaciando con nuevos valores
    producto={}
    #aca pido datos al usuario
    nombre_producto = input('Ingresa el nombre del proudcto: ')
    precio_producto=float(input('Ingresa el precio del producto: '))
    categoria_producto=input('Ingresa la categoria del producto: ')
    provedor_producto=input('Ingresa el provedor del producto: ')
    stock_producto=int(input('Ingresa el stock del producto: '))
    #agrego los datos a el diccionario
    producto['nombre']=nombre_producto
    producto['precio']=precio_producto
    producto['categoria']=categoria_producto
    producto['provedor']=provedor_producto
    producto['stock']=stock_producto
    #agrego el diccionario a la lista
    productos.append(producto)
    #pido al usuario si va a seguir agregando productos
    opcion=input('Desea agregar otro producto?(S/N): ').lower().strip()
#aca muestro la lista en bruto con los diccionarios
print('Datos(Lista de diccionarios)')
print(productos)
#aca muestro el header de la tabla
print('Tabla de datos:')
print(f"{'Nombre':20} {'Precio':>12} {'Categoría':15} {'Stock':>8} {'Proveedor':15}")
print("-" * 75)
#aca imprimo los datos de cada diccionario en el array
for producto in productos:
        stock = stock + producto['stock']
        precios_suma = precios_suma + producto['precio']
        print(f"{producto['nombre']:20} {producto['precio']:12,.2f} {producto['categoria']:15} {producto['stock']:8} {producto['provedor']:15}")
#aca muestro la cantidad de diccionarios en la lista
print(f'Productos totales : {len(productos)}')

#aca declaro 2 diccionarios cada uno guardara la cantidad de categorias que hay
categorias={}
provedores={}
#contar categorias y provedores
for producto in productos:
    categorias[producto['categoria']]=categorias.get(producto['categoria'],0)+1
    provedores[producto['provedor']]=provedores.get(producto['provedor'],0)+1
#imprimir categorias
print('Categorias:')
for categoria,contador in categorias.items():
    print(categoria,":",contador)
#imprimir los provedores
print('Provedores:')
for provedor,contador in provedores.items():
    print(provedor,":",contador)
#aca saco el promedio del stock
promedio = stock/len(productos)
promedio_precios=precios_suma/len(productos)
#imprimo el tock y su promedio
print(f'Stock -> {stock},Pomedio : {promedio:.2f}')
#imprimo la suma de precios y promedio
print(f'Precio -> Suma : {precios_suma:.2f} ,Promedio : {promedio_precios:.2f}')
#buscamos el valor maximo de precio y lo saco y su llave
producto_mas_caro = max(productos, key=lambda producto: producto["precio"])
#busco el valor mas barato y le saco su llave y valor
producto_mas_barato = min(productos, key=lambda producto: producto["precio"])
#imprimo el resultado de los diccionarios creados
print(f'El producto mas caro es {producto_mas_caro['nombre']},que cuesta ${producto_mas_caro['precio']}')
print(f'El producto mas barato  es {producto_mas_barato['nombre']},que cuesta ${producto_mas_barato['precio']}')
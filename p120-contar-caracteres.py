cadena=input('Ingrese una cadena: ')
diccionario={}
for valor in cadena:
    if valor in diccionario:
        diccionario[valor]+=1
    else:
        diccionario[valor]=1
print(diccionario)
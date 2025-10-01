while True:
    temperatura_temporal = 0
    temp_ini=float(input('Introduce la temperatura inicial en °C: '))
    tem_fin=float(input('Introduce la temperatura final en °C: '))
    temperatura_temporal = temp_ini
    print('------------------------------------------------------')
    while True:
        if(temperatura_temporal <= tem_fin):
            temperatura_temporal_f = (temperatura_temporal* 9/5) + 32
            print(f'{temperatura_temporal}°C = {temperatura_temporal_f}°F')
            temperatura_temporal += 1
        else:
            break
    continuar = input("¿Desea continuar (S/N)? ").strip().upper()
    if continuar == "N":
        break
    

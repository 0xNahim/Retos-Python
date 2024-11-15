def justificar(linea, tamaño):
    palabras = linea.split()
    total = 0
    for p in palabras:
        total += len(p)
    cantidad = len(palabras)-1 
    tamaño = tamaño - total
    espacios_nuevos = tamaño // cantidad
    restante = tamaño % cantidad 
    print(restante)
    res = ""
     
    for i in palabras:
        if i != palabras[-1]:
            res += i + " "*espacios_nuevos
            if restante != 0:
                res += " "
                restante -=1
        else:
            res += i

    print(len(res))
    
    return res
datos = [2, 4, 6, 8, 14]


def promedio(lista):
    suma = 0

    for x in lista:
        suma += x

    return suma / len(lista)



print(promedio(datos))

def maximo(lista):
    max = lista[0]

    for x in lista:
        if x > max:
            max = x

    return max


print(maximo(datos))
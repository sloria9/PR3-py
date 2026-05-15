# Mini programa para interpolar / predecir estados del juego
# Hecho con una estructura bien básica, similar al ejercicio de centroide.

# Idea general:
# - Cada archivo representa un estado del juego.
# - Cada línea del archivo tiene un número.
# - Para cada posición, miramos cómo cambia ese número entre los estados.
# - Con esos valores armamos una interpolación de Lagrange.
# - Después calculamos el valor del siguiente estado.


def leer_estado(nombre_archivo):
    # Lee un archivo y devuelve una lista con sus valores numéricos.
    estado = []

    with open(nombre_archivo, "r") as archivo:
        for linea in archivo:
            valor = float(linea.strip())
            estado.append(valor)

    return estado


def guardar_estado(nombre_archivo, estado):
    # Guarda la lista de valores en un archivo, un valor por línea.
    with open(nombre_archivo, "w") as archivo:
        for valor in estado:
            archivo.write(str(valor) + "\n")


def interpolar_lagrange(x_conocidos, y_conocidos, x_a_predecir):
    # Esta función calcula el valor interpolado usando Lagrange.
    # x_conocidos: son los números de estado conocidos, por ejemplo [1, 2]
    # y_conocidos: son los valores que tiene una posición en esos estados
    # x_a_predecir: es el estado que queremos calcular, por ejemplo 3

    resultado = 0

    for i in range(len(x_conocidos)):
        termino = y_conocidos[i]

        for j in range(len(x_conocidos)):
            if i != j:
                termino = termino * (x_a_predecir - x_conocidos[j]) / (x_conocidos[i] - x_conocidos[j])

        resultado += termino

    return resultado


def acomodar_valor(valor):
    # Como los estados parecen manejar valores entre 0 y 255,
    # redondeamos el resultado y lo dejamos dentro de ese rango.
    valor = round(valor)

    if valor < 0:
        valor = 0

    if valor > 255:
        valor = 255

    return int(valor)


def validar_estados(estados):
    # Verifica que todos los estados tengan la misma cantidad de valores.
    cantidad = len(estados[0])

    for estado in estados:
        if len(estado) != cantidad:
            return False

    return True


def interpolar_siguiente_estado(nombres_archivos, numero_estado_a_predecir):
    # nombres_archivos: lista con los archivos que vamos a usar.
    # Ejemplo para n = 2: ["1", "2"]
    # Ejemplo para n = 3: ["1", "2", "3"]

    estados = []

    # Primero leo todos los estados conocidos.
    for nombre in nombres_archivos:
        estado = leer_estado(nombre)
        estados.append(estado)

    if validar_estados(estados) == False:
        print("Error: los estados no tienen la misma cantidad de valores")
        return []

    # Los estados conocidos se numeran 1, 2, 3, etc.
    x_conocidos = []

    for i in range(len(estados)):
        x_conocidos.append(i + 1)

    prediccion = []
    cantidad_valores = len(estados[0])

    # Recorro posición por posición.
    for posicion in range(cantidad_valores):
        y_conocidos = []

        # Busco el valor de esa posición en cada estado conocido.
        for estado in estados:
            y_conocidos.append(estado[posicion])

        # Calculo el valor de esa posición para el estado siguiente.
        valor_predicho = interpolar_lagrange(x_conocidos, y_conocidos, numero_estado_a_predecir)

        # Redondeo y acomodo el valor para que sea válido.
        valor_predicho = acomodar_valor(valor_predicho)

        prediccion.append(valor_predicho)

    return prediccion


# -----------------------------
# Programa principal
# -----------------------------

# Caso n = 2
# Uso los estados 1 y 2 para predecir el estado 3.
prediccion_n2 = interpolar_siguiente_estado(["1", "2"], 3)
guardar_estado("prediccion_n2.txt", prediccion_n2)

print("Predicción usando n = 2 guardada en prediccion_n2.txt")
print("Primeros 10 valores n = 2:", prediccion_n2[:10])


# Caso n = 3
# Uso los estados 1, 2 y 3 para predecir el estado 4.
prediccion_n3 = interpolar_siguiente_estado(["1", "2", "3"], 4)
guardar_estado("prediccion_n3.txt", prediccion_n3)

print("Predicción usando n = 3 guardada en prediccion_n3.txt")
print("Primeros 10 valores n = 3:", prediccion_n3[:10])
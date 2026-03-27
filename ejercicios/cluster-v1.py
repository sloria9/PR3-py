#Crear una función (o funciones) en Python que calcule el radio y el diámetro de un cluster dado como parámetro.
#El cluster debe pasarse como:
#Una lista/arreglo de tuplas de longitud 2 (pares de coordenadas), o
#Dos arreglos separados de números reales
#El profesor especificó que pueden hacerlo para puntos de 2 coordenadas (dimensión 2), aunque mencionó que se podría generalizar a dimensión M.
#Para calcular:
#El radio: es la máxima distancia entre cualquier punto del cluster y su centroide
#El diámetro: es la máxima distancia entre dos puntos cualesquiera del cluster
#El profesor sugirió usar funciones de Python como math.sqrt para la raíz cuadrada, sum para sumas, max para máximos, y mencionó que pueden usar ciclos for o construcciones más ingeniosas según prefieran.

#representacion de cluster, cada elemento es un punto
#centroide Promedio de las x y promedio de las y.
#sumo todas las x
#sumo todas las y
#divido la suma total con la cantidad de puntos (x e y)
#promedio pero en 2 dimensiones
def calcularCentroide(cluster):

    sumax = 0
    sumay = 0

    for punto in cluster:
        sumax += punto[0]
        sumay += punto[1] #el index 1 es porque viene como segundo elemento la y

    return (sumax / len(cluster), sumay / len(cluster))

#diámetro Distancia entre dos puntos.
#resto x
#resto y
#elevo al cuadrado
#sumo
#raíz cuadrada
import math

def distancia(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

#radio la mayor distancia entre el centroide y los puntos
#1. calculo el centroide
#2. max = 0
#3. para cada punto:
#       calculo distancia al centroide
#       si es mayor que max:
#            lo guardo
#4. devuelvo max

def radio(cluster):
    centroide = calcularCentroide(cluster)
    max_dist = 0

    for punto in cluster:
       dist = distancia(punto, centroide)
       if dist > max_dist:
          max_dist = dist
    return max_dist

#diametro mayor distancia entre dos puntos
#por cada par de puntos debo fijarme cual tiene mas distancia
def diametro(cluster):
    max_dist = 0

    for i in range(len(cluster)):
        for j in range(i + 1, len(cluster)):
            d = distancia(cluster[i], cluster[j])
            if d > max_dist:
                max_dist = d

    return max_dist
#doble for → O(n²) → correcto


cluster = [(1, 2), (3, 4), (5, 1), (2, 3)]

print("Centroide:", calcularCentroide(cluster))
print("Radio:", radio(cluster))
print("Diámetro:", diametro(cluster))
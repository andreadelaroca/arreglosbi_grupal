# Crear un programa que permita la linealización de un arreglo
# bidimensional por columnas. 
# Los datos del arreglo bidimensional serán tomados de la tabla.

def linealizar_por_columnas(matriz):
    filas = len(matriz) # Obtenemos la cantidad de filas de la matriz
    columnas = len(matriz[0]) # Obtenemos la cantidad de columnas de la matriz
    resultado = [] # Lista vacía donde vamos a almacenar los elementos linealizados
    
    for columna in range(columnas):  # Recorremos cada columna primero
        for fila in range(filas):    # Por cada columna, recorremos todas las filas
            resultado.append(matriz[fila][columna])  # Agregamos el elemento de la posición [fila][columna] a la lista resultado
            
    return resultado
matriz = [
    [1, 2, 3, 7],
    [4, 5, 6, 8]
]
   
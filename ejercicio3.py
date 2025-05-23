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
    [1, 2, 3, 7],   # Definicion de la matriz
    [4, 5, 6, 8]
]

print("Matriz original:") #Se imprime la matriz original
for fila in matriz:
    print(fila)
    
linealizada = linealizar_por_columnas(matriz) # Se llama la función de linealización y se guarda el resultado

print("\nMatriz linealizada por columnas:") # Se imprime la matriz linealizada
print(linealizada)

   
# Crear un programa que permita la linealización de un arreglo
# bidimensional por columnas. 
# Los datos del arreglo bidimensional serán tomados de la tabla.

def linealizar_por_columnas(matriz):
    filas = len(matriz) # Obtenemos la cantidad de filas de la matriz
    columnas = len(matriz[0]) # Obtenemos la cantidad de columnas de la matriz
    resultado = [] # Lista vacía donde vamos a almacenar los elementos linealizados
    
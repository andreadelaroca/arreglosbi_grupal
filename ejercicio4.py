# ingresar cada uno de los valores de la matriz, luego mostrar:
#   a. suma de valores por fila
#   b. promedio de valores por columna
#   c. mayor valor almacenado en toda la matriz y su posición

print("Ingrese el valor de n y m (ambos positivos y menores que 10):")

# definir validación de n y m (enteros positivos y menores que 10)
def validar(mensaje):
    while True:
        num = int(input(mensaje))
        if 0 < num < 10:
            return num
        print("Valor inválido. Debe ser un número positivo menor que 10.\n")
        
# input de n y m
n = validar("Ingrese el número de filas de la matriz: ")
m = validar("Ingrese el número de columnas de la matriz: ")

# lista vacía para almacenar la matriz
matriz = []

# ingresar los elementos de la matriz
for i in range(n):
    matriz.append([])
    for j in range(m):
        elemento = int(input(f"Ingrese el elemento ({i + 1}), ({j + 1}): "))
        matriz[i].append(elemento)

# mostrar la matriz
print("\nLa matriz es:")
for fila in matriz:
    print(fila)

# mostrar suma de valores para cada fila
print("\nSuma de valores por fila:")
for i in range(n):
    suma_fila = sum(matriz[i])
    print(f"Fila {i + 1}: {suma_fila}")
    

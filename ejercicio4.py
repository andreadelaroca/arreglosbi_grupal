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
        

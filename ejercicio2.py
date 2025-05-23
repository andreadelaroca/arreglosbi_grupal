# Este programa captura el nombre y tres calificaciones de 5 estudiantes de la facultad de Ingeniería.
# Luego, calcula el promedio de las calificaciones de cada estudiante y muestra los resultados en pantalla.

# Lista bidimensional para almacenar los datos de los estudiantes
# Cada fila representará un estudiante: [nombre, calificación1, calificación2, calificación3, promedio]
estudiantes = []

# Bucle para capturar los datos de 5 estudiantes
for i in range(5):
    # Solicitar el nombre del estudiante
    nombre = input("Ingrese el nombre del estudiante: ")
    
    # Lista para almacenar las calificaciones del estudiante actual
    calificaciones = []
    
    # Bucle para capturar las 3 calificaciones del estudiante
    for j in range(3):
        # Solicitar cada calificación y convertirla a tipo float
        calificacion = float(input(f"Ingrese la calificación {j+1} de {nombre}: "))
        # Agregar la calificación a la lista de calificaciones
        calificaciones.append(calificacion)
    
    # Calcular el promedio de las calificaciones del estudiante
    promedio = sum(calificaciones) / len(calificaciones)
    
    # Agregar el nombre, las calificaciones y el promedio del estudiante a la lista bidimensional
    estudiantes.append([nombre] + calificaciones + [promedio])

# Mostrar los promedios de los estudiantes en pantalla
print("\nPromedios de los estudiantes:")
for estudiante in estudiantes:
    # El nombre está en la primera posición y el promedio en la última posición de cada fila
    nombre = estudiante[0]
    promedio = estudiante[-1]
    # Imprimir el nombre y el promedio con dos decimales
    print(f"{nombre}: {promedio:.2f}")
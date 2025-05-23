#Se desea realizar un programa en donde se capture el nombre y tres calificaciones para
#5 estudiantes de la facultad de Ingeniería, y después se pueda procesar dándonos el
#promedio final de cada uno de los alumnos, el resultado se mostrará en pantalla


# Lista para almacenar los datos de los estudiantes (nombre y promedio)
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
    
    # Agregar el nombre y el promedio del estudiante a la lista principal
    estudiantes.append((nombre, promedio))

# Mostrar los promedios de los estudiantes en pantalla
print("\nPromedios de los estudiantes:")
for estudiante in estudiantes:
    # Desempaquetar el nombre y el promedio de cada estudiante
    nombre, promedio = estudiante
    # Imprimir el nombre y el promedio con dos decimales
    print(f"{nombre}: {promedio:.2f}")
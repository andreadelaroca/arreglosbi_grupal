# 1. La Abarrotera ABSA tiene 4 sucursales en las cuales se realizaron diferentes ventas en los
# meses de Julio a diciembre del año 2022, se le ha solicitado a usted realizar un programa en
# donde pueda capturar la siguiente tabla de datos:

# Estado de cuenta de las Sucursales ABSA en el segundo semestre 2022
# Tienda/Mes Julio  Agosto Septiembre Octubre Noviembre Diciembre
# ABSA1      50,000 60,000  65,000    62,000   78,000    95,000
# ABSA2      89,000 90,000  98,000    80,000   85,000    90,000
# ABSA3      65,000 72,000  85,000    72,000   83,000    98,000
# ABSA4      92,000 88,000  90,000    76,000   82,000    93,000
# y nos presente los siguientes resultados:

# a. Venta total por todas las tiendas
# b. Venta total por tienda
# c. Tienda que más vendió en los 6 meses
# d. Tienda que menos vendió



#Franklin Callejas

# Definición de la función para limpiar la pantalla
import os
import time
os.system('cls || clear')
#Definimos las variables
ABSA1 = [50000, 60000, 65000, 62000, 78000, 95000]     #Tienda1
ABSA2 = [89000, 90000, 98000, 80000, 85000, 90000]     #Tienda2
ABSA3 = [65000, 72000, 85000, 72000, 83000, 98000]     #Tienda3
ABSA4 = [92000, 88000, 90000, 76000, 82000, 93000]     #Tienda4
# Definimos la cantidad de meses y las listas de tiendas y ventas
meses = 6
tiendas = ["ABSA1", "ABSA2", "ABSA3", "ABSA4"]
ventas = [ABSA1, ABSA2, ABSA3, ABSA4]

# Definimos la función para calcular la venta total por tienda
def suma_todas_ventas():
    total=0                             
    for i in range (len(tiendas)):      #Recorremos las tiendas
        for j in range (meses):         #Recorremos los meses
            total += ventas[i][j]       #Sumamos las ventas
    return total                        #Retornamos el total de ventas

# Definimos la función para calcular la venta total por tienda
def total_por_tienda(tienda):
    total = 0
    for i in range (meses):            
        total += ventas[tienda][i]     #Sumamos las ventas
    return total                       #Retornamos el total de ventas

# Definimos la función para calcular la tienda que más vendió
def tienda_mas_vendio():
    max_venta=0
    for i in range (len(tiendas)):
        total = total_por_tienda(i)    #Llamamos a la función para calcular el total por tienda
        if total > max_venta:           #Si el total es mayor que el máximo
            max_venta = total           #Actualizamos el máximo
            tienda = i                  #Guardamos la tienda
    return tienda                     #Retornamos la tienda que mas vendio

# Definimos la funcion para calcular la tienda que menos vendio
#Lo mismo que la anterior pero con el mínimo
def tienda_q_menos_vendio():
    min_venta = float('inf')           #Inicializamos el minimo 
                                       #Inf es para que no haya un numero menor que el infinito 
    for i in range (len(tiendas)):
        total = total_por_tienda(i)    #Llamamos a la función para calcular el total por tienda
        if total < min_venta:           #Si el total es menor que el mínimo
            min_venta = total           #Actualizamos el mínimo
            tienda = i                  #Guardamos la tienda
    return tienda                     #Retornamos la tienda que menos vendió 

# Submenu para continuar o salir del menu
def submenu():
    while True: #Mientras sea verdadero
        print("\n¿Qué desea hacer ahora?")
        print("1. Volver al menú")
        print("2. Salir del programa")
        try:
            opcion = int(input("Ingrese una opción\n-> "))
            if opcion == 1:
                return True  #Retorna verdadero para volver al menu
            elif opcion == 2:
                return False  #Retorna falso para salir del programa
            else: #Si no es ninguna de las anteriores te muestra un mensaje
                print("Opción no válida. Por favor, seleccione 1 o 2.")
                time.sleep(2)
                os.system('cls || clear')
        except ValueError: #Si no es un numero te muestra un mensaje de error
            print("Entrada no válida. Por favor, ingrese un número (1 o 2).")
            time.sleep(2)
            os.system('cls || clear')

#Hacemos el menu principal
def menu():
    print("Estado de cuenta de las Sucursales ABSA en el segundo semestre 2022")
    print("---- Menu de opciones ----")
    print("")
    print("1. Venta total por todas las tiendas")
    print("2. Venta total por tienda")
    print("3. Tienda que más vendió en los 6 meses")
    print("4. Tienda que menos vendió")
    print("5. Salir")
    print("")
    try:
        opcion = int(input("Ingrese una opción\n-> "))
        return opcion
    except ValueError:
        return -1  #Retorna -1 si no es un numero

#Hacemos el menu principal
def main():
    while True:
        os.system('cls || clear')  
        opcion = menu()
        
        if opcion == 1:
            print(f"La venta total por todas las tiendas es: {suma_todas_ventas():,} $")
            time.sleep(3)
            if not submenu():
                break
        elif opcion == 2:
            for i in range(len(ventas)):
                print(f"La venta total de la tienda {tiendas[i]} es: {total_tienda(i):,} $")
            time.sleep(3)
            if not submenu():
                break
        elif opcion == 3:
            print(f"La tienda que más vendió es: {tiendas[tienda_mas_vendio()]} con {total_tienda(tienda_mas_vendio()):,} $")
            time.sleep(3)
            if not submenu():
                break
        elif opcion == 4:
            print(f"La tienda que menos vendió es: {tiendas[tienda_menos_vendio()]} con {total_tienda(tienda_menos_vendio()):,} $")
            time.sleep(3)
            if not submenu():
                break
        elif opcion == 5:
            print("Saliendo del programa...")
            time.sleep(2)
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción entre 1 y 5.")
            time.sleep(3)

if __name__ == "__main__":
    main()


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
def total_ventas():
    total=0                             
    for i in range (len(tiendas)):      #Recorremos las tiendas
        for j in range (meses):         #Recorremos los meses
            total += ventas[i][j]       #Sumamos las ventas
    return total                        #Retornamos el total de ventas

# Definimos la función para calcular la venta total por tienda

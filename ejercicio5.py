#5. Escriba el programa que tenga un arreglo bidimensional que almacena la cantidad de
#computadores vendidos por tres vendedores en cuatro zonas diferentes. Se pide mostrar:
#a. La zona en la que más computadores se vendió.
#b. El vendedor que menos computadores vendió.
#c. La cantidad de computadores vendidos por todos los vendedores en todas las zonas.

vendedores = ["Vendedor 1","Vendedor 2","Vendedor 3"]
zonas = ["Zona 1 ","Zona 2","Zona 3","Zona 4"] # se hacen las listas bidimensionales para guardar datos 

matriz_ventas = [] #se inicializa la matriz 
 
#Se hace el rrecorido de las ventas de cada vendedor y las ventas de vendedores  por zona
print("\n------Bienvenido al sistema de ventas de HP store-----")
for vendedor in range(3):
        fila = []
        for zona in range(4):
           ventas = int(input(f"\nIngrese las ventas del vendedor {vendedor + 1} en la zona {zona + 1}:"))
           fila.append(ventas) # el append va agregando datos a la matriz segun los datos dados del usuario
        matriz_ventas.append(fila)
           
# se comienza a hacer la preparacion de la matriz 
print("\n------Ventas totales de vendedores x zona-----")
print("       ", end=" ")
for zona in zonas:
      print(f"{zona:^10}", end="")
print()
for i, fila in enumerate(matriz_ventas):
      print(f"{vendedores [i]:<10}", end =" ")
      for venta in fila:
            print(f"{ventas:^8}", end = " ")
print()

#Ahora se prosigue a calcular la zona con mas venta
zona_mayor = 0
max_ventas = 0
for z in range(4):
      total_zona = sum(matriz_ventas[v][z] for v in range(3))
      if total_zona > max_ventas:
            max_ventas = total_zona
            zona_mayor = z

#Ahora el vendedor que menos vendio
vendedor_menor = 0 
min_ventas = float('inf')
total_general = 0 

for v in range(3):
      total_vendedor = sum(matriz_ventas[v])
      total_general += total_vendedor
      if total_vendedor < min_ventas:
            min_ventas = total_vendedor
            vendedor_menor = v

#hora de mostrar los resultados 
print("\n---------Recopilacion de datos-------")
print(f"La zona que menos computadoras se vendieron fue : {zonas[zona_mayor]}")
print(f"El vendedor que menos ventas hizo fue : {vendedores[vendedor_menor]}")
print(f"El total de computadoras vendidas fue : {total_general}")
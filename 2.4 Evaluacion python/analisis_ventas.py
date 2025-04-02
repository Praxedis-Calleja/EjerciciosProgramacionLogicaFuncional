
from functools import reduce
ventas = [1500, 2500, 3200, 4500, 6000, 1200, 8000]

promedio = reduce(lambda acumulador, venta: acumulador + venta, ventas, 0 ) / len(ventas)
ventasDolares = list(map(lambda dolares: dolares/20.45, ventas))
ventasSuperadas = list(filter(lambda venta: venta>150, ventasDolares))
totalventasFiltradas = reduce(lambda acumulador, venta: acumulador + venta, ventasSuperadas, 0 ) 

print("Promedio de ventas: ", promedio)
print("Ventas a dolares: ",ventasDolares)
print("Ventas superan los 150$: ", ventasSuperadas)
print("Total de ventas en dolares: ", totalventasFiltradas)



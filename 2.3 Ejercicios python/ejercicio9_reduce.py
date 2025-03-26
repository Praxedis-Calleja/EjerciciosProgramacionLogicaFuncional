
from functools import reduce

jugadores = [
    { "nombre": "Ronaldo", "edad": 14},
    { "nombre": "Messi", "edad": 13},
    { "nombre": "Neymar", "edad": 12},
]
suma_edades = reduce(lambda acumulador, jugador: acumulador + jugador["edad"], jugadores, 0)
print(suma_edades)  # Output: 39
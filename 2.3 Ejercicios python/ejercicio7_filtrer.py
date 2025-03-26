jugadores = [
    { "nombre": "Ronaldo", "edad": 14},
    { "nombre": "Messi", "edad": 13},
    { "nombre": "Neymar", "edad": 12},
]

jugadores_mayores = list(filter(lambda jugador: jugador["edad"] > 13, jugadores))
print(jugadores_mayores)  # Output: [{'nombre': 'Ronaldo', 'edad': 14}]
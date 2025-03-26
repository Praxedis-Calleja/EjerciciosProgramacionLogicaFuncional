jugadores = [
    { "nombre": "Ronado", "edad": 14},
    { "nombre": "Messi", "edad": 13},
    { "nombre": "Neymar", "edad": 12},
]
nombre_jugadores = list(map(lambda jugador: jugador["nombre"], jugadores))

print(nombre_jugadores)
def saludo(nombre):
    return f"Hola, {nombre}!"

def ejecutar_funcion(funcion, argumento):
    return funcion(argumento)

# Pasamos la función 'saludo' como argumento
mensaje = ejecutar_funcion(saludo, "Praxedis")

print(mensaje)  # Salida: Hola, Praxedis!

def saludo_personalizado(funcion_saludo, nombre):
    return funcion_saludo(nombre)

def saludo_espanol(nombre):
    return f"Hola, {nombre}!"

def saludo_ingles(nombre):
    return f"Hello, {nombre}!"

# Usando la función de primer orden
print(saludo_personalizado(saludo_espanol, "Praxedis"))  # Salida: Hola, Praxedis!
print(saludo_personalizado(saludo_ingles, "Vinicio"))    # Salida: Hello, Vinicio!

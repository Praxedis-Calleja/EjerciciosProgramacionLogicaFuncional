def procesar_datos(data, callback):
    print("Procesando datos...")
    resultado = callback(data)
    print(f"Resultado procesado: {resultado}")

# Definimos una función callback
def mi_callback(data):
    return data.upper()

# Usamos la función procesar_datos con la función callback
datos = "hola mundo"
procesar_datos(datos, mi_callback)
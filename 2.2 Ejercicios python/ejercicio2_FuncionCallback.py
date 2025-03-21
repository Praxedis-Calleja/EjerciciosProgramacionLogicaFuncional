def procesar_dato(dato, callback):
    resultado = dato * 2 
    return callback(resultado) 

def imprimir_resultado(valor):
    print(f"El resultado es: {valor}")


procesar_dato(5, imprimir_resultado)  

# Salida: El resultado es: 10

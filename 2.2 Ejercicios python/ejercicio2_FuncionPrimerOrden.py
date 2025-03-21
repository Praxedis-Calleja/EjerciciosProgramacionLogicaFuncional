
def aplicar_funcion(funcion, valor):
    return funcion(valor)

def cuadrado(x):
    return x * x

# Usamos la función de primer orden
resultado = aplicar_funcion(cuadrado, 5)
print(f"El cuadrado de 5 es: {resultado}")
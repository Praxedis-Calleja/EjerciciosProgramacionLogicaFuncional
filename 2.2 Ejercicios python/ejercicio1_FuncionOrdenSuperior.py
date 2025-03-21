# Ejemplo de una función de orden superior en Python

# Definimos una función de orden superior que toma otra función como argumento
def aplicar_operacion(funcion, a, b):
    return funcion(a, b)

# Definimos algunas funciones que podemos pasar como argumento
def sumar(x, y):
    return x + y

def multiplicar(x, y):
    return x * y
    
# Usamos la función de orden superior
resultado_suma = aplicar_operacion(sumar, 5, 3)
resultado_multiplicacion = aplicar_operacion(multiplicar, 5, 3)

print(f"Resultado de la suma: {resultado_suma}")
print(f"Resultado de la multiplicación: {resultado_multiplicacion}")
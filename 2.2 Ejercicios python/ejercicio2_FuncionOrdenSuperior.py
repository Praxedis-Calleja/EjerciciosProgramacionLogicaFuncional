def cuadrado(x):
    return x ** 2

numeros = [1, 2, 3, 4, 5]

# Usamos map, que es una función de orden superior, aplicando cuadrado a cada número
resultado = list(map(cuadrado, numeros))

print(resultado)  # Salida: [1, 4, 9, 16, 25]

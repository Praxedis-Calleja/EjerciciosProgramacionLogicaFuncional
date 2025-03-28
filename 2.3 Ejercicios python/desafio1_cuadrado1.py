numeros_reales = [-3, 4.8, 5, 4, -3.2]
def cuadradosLista(arreglo):
    
    cuadrado_perfecto =  list(map(lambda x: x**2, filter(lambda x: x > 0 and int(x) == x, arreglo)))

    return cuadrado_perfecto
resultado = cuadradosLista(numeros_reales)
print(resultado)




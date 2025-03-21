def preparar_cafe_a():
    return "Café Americano"

def preparar_cafe_o():
    return "Café Olla"

def ordenar_cafe(funcion, numerotazas):
    tazas_cafe = [funcion() for _ in range(numerotazas)]
    return tazas_cafe

#seleccionarCafe = int(input("¿Qué tipo de café quieres? (Americano/Olla)"))

cafe_para_grupo_a = ordenar_cafe(preparar_cafe_a, int(input("¿Cuántas tazas quieres para el grupo a?")))
cafe_para_grupo_b = ordenar_cafe(preparar_cafe_o, int(input("¿Cuántas tazas quieres para el grupo b?")))
print(cafe_para_grupo_a)
print(cafe_para_grupo_b)

def preparar_pizza():
    return "🍕"

def preparar_hamburguesa():
    return "🍔"

def preparar_hotdog():
    return "🌭"

def bonos_pedido(numerocomida):
    if numerocomida >= 2:
        return "Coca gratis"
    else:
        return ""

def ordenar_comida(funcion, numerocomida):
    porciones_alimentos = [funcion() for _ in range(numerocomida)]
    return porciones_alimentos + [bonos_pedido(numerocomida)]


    
num_pizza = int(input("¿Cuántas porciones de pizza quieres para el grupo A?"))
num_hamburguesa = int(input("¿Cuántas hamburguesas quieres para el grupo B?"))
num_hotdog = int(input("¿Cuántos hotdogs quieres para el grupo C?"))
comida_para_grupo_pizza = ordenar_comida(preparar_pizza, num_pizza)
comida_para_grupo_hamburguesa = ordenar_comida(preparar_hamburguesa, num_hamburguesa)
comida_para_grupo_hotdog = ordenar_comida(preparar_hotdog, num_hotdog)







print(comida_para_grupo_pizza)
print(comida_para_grupo_hamburguesa)    
print(comida_para_grupo_hotdog)




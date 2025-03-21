def preparar_hotcake():
    return "🥞"

print(preparar_hotcake())


def ordenar_hotcakes(num_hotcakes):
    piezas_hotcakes =[preparar_hotcake() for _ in range(num_hotcakes)]
    return piezas_hotcakes

num_hotcakes = int(input("¿Cuántos hotcakes quieres?"))




print(ordenar_hotcakes(num_hotcakes))



    


def preparar_cafe():
    return "Café"

print(preparar_cafe());   

def ordenas_cafe(num_tazas):
    tazas_cafe = [  preparar_cafe() for _ in range(num_tazas)]
    return tazas_cafe
cafe_para_grupo = ordenas_cafe(10)
print(cafe_para_grupo)
    

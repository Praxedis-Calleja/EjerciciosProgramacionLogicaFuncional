AlimentosBebidas = [
    "Frijoles refritos",
    "Coca cola",
    "Zumo de naranja",
    "Cafe de olla",
    "Gorditas de chicharron",
    "Huevos motuleños"
]

AlimentosBebidas.sort()

convertirCadenas =  ", ".join(list(map(str, AlimentosBebidas)))

print(convertirCadenas)

ConversionSlug = list(map(lambda nueva: nueva.lower().replace(" ", "-"), AlimentosBebidas))
print(ConversionSlug)
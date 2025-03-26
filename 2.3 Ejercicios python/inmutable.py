variable_global = 10

def aumentar_variable():
    return variable_global +1

print(aumentar_variable()) 

def contar_palabras(texti):
    return len(texti.split())

oracion = "El tema de hoy es la inmotabilidad en Python"
print(contar_palabras(oracion)) 
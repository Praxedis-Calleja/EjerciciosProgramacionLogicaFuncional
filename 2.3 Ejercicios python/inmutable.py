variable_global = 10

def aumentar_variable():
    return variable_global +1

print(aumentar_variable()) 

def contar_palabras(texti):
    return len(texti.split())

oracion = "El tema de hoy es la inmotabilidad en Python"
print(contar_palabras(oracion)) 

contador_global = 0

def contador_palabras_no_funcional(texto):
    global contador_global
    contador_global = len(texto.split())
    
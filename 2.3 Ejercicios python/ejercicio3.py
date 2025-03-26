
asignitanuras_VIII = [
    "Matemáticas"
]

nueva_lista = [asignitanuras_VIII, "Fisica"]
  

print(asignitanuras_VIII)
print(nueva_lista)

def agregar_asignatura(funcion, asignatura):
    
    return funcion + [asignatura]

    
asignatura_dato = input("Ingrese la asignatura: ")
print(agregar_asignatura(asignitanuras_VIII, asignatura_dato))